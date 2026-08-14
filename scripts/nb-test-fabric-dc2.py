"""Mode B: create fabric-dc2 site + 4 leaf + 2 spine + ISL cables in NetBox.

Topology: each leaf has ethernet-1/49 → spine-01, ethernet-1/50 → spine-02 (8 ISL cables).
Device types: 7220 IXR-D3L (leaf), 7220 IXR-D4 (spine). Platform: srl.

Prerequisites: catalog seed (§4.1.1), namespace bootstrap (§5.2).
Set NODE_PROFILE from: kubectl get nodeprofiles -n fabric-dc2 -o jsonpath='{.items[0].metadata.name}'
Run before ApplyTopology (§5.6).
"""
from dcim.models import (
    Device, Site, Platform, DeviceRole, DeviceType,
    Interface, Cable, CableTermination,
)
from extras.models import Tag
from django.contrib.contenttypes.models import ContentType

SITE = "fabric-dc2"
NODE_PROFILE = "srlinux-ghcr-24.10.2"  # edit — must match bootstrap NodeProfile name

LEAF_DT = "7220 IXR-D3L"
SPINE_DT = "7220 IXR-D4"

platform, _ = Platform.objects.get_or_create(name="srl", defaults={"slug": "srl"})
site, _ = Site.objects.get_or_create(
    name=SITE, defaults={"slug": SITE, "status": "planned"},
)
leaf_role = DeviceRole.objects.get(name__iexact="leaf")
spine_role = DeviceRole.objects.filter(name__iexact="spine").first() or leaf_role
dtype_leaf = DeviceType.objects.get(model=LEAF_DT)
dtype_spine = DeviceType.objects.get(model=SPINE_DT)
ct = ContentType.objects.get_for_model(Interface)

links = [
    ("leaf-dc2-01", "ethernet-1/49", "spine-dc2-01", "ethernet-1/1"),
    ("leaf-dc2-01", "ethernet-1/50", "spine-dc2-02", "ethernet-1/1"),
    ("leaf-dc2-02", "ethernet-1/49", "spine-dc2-01", "ethernet-1/2"),
    ("leaf-dc2-02", "ethernet-1/50", "spine-dc2-02", "ethernet-1/2"),
    ("leaf-dc2-03", "ethernet-1/49", "spine-dc2-01", "ethernet-1/3"),
    ("leaf-dc2-03", "ethernet-1/50", "spine-dc2-02", "ethernet-1/3"),
    ("leaf-dc2-04", "ethernet-1/49", "spine-dc2-01", "ethernet-1/4"),
    ("leaf-dc2-04", "ethernet-1/50", "spine-dc2-02", "ethernet-1/4"),
]


def kv_tag(kv: str):
    slug = kv.replace("=", "-").replace("/", "-").replace(".", "-").lower()[:100]
    tag, _ = Tag.objects.get_or_create(name=kv, defaults={"slug": slug, "color": "9e9e9e"})
    return tag


isl_tag = kv_tag("eda.nokia.com/role=interSwitch")


def ensure_device(name, role, dtype, role_tag):
    tags = [
        kv_tag(f"eda.nokia.com/node-profile={NODE_PROFILE}"),
        kv_tag(f"eda.nokia.com/role={role_tag}"),
        kv_tag(f"site={SITE}"),
    ]
    dev = Device.objects.filter(name=name, site=site).first()
    if dev:
        dev.role = role
        dev.device_type = dtype
        dev.platform = platform
        dev.status = "planned"
        dev.save()
        created = False
    else:
        dev = Device.objects.create(
            name=name,
            site=site,
            role=role,
            device_type=dtype,
            platform=platform,
            status="planned",
        )
        created = True
    dev.tags.set(tags)
    print(f"device {name} created={created} id={dev.id}")
    return dev


def ensure_iface(dev, name):
    iface, created = Interface.objects.get_or_create(
        device=dev, name=name, defaults={"type": "100gbase-x-qsfp28", "enabled": True}
    )
    print(f"  iface {dev.name}/{name} created={created}")
    return iface


for i in range(1, 5):
    ensure_device(f"leaf-dc2-{i:02d}", leaf_role, dtype_leaf, "leaf")
ensure_device("spine-dc2-01", spine_role, dtype_spine, "spine")
ensure_device("spine-dc2-02", spine_role, dtype_spine, "spine")

ifaces = {}
for leaf, leaf_if, spine, spine_if in links:
    for dev_name, if_name in [(leaf, leaf_if), (spine, spine_if)]:
        key = (dev_name, if_name)
        if key not in ifaces:
            dev = Device.objects.get(name=dev_name, site=site)
            ifaces[key] = ensure_iface(dev, if_name)

for leaf, leaf_if, spine, spine_if in links:
    label = f"{leaf}-{leaf_if.replace('/', '-')}-{spine}-{spine_if.replace('/', '-')}"
    a = ifaces[(leaf, leaf_if)]
    b = ifaces[(spine, spine_if)]
    if Cable.objects.filter(label=label).exists():
        print(f"cable exists {label}")
        continue
    if CableTermination.objects.filter(termination_type=ct, termination_id__in=[a.id, b.id]).exists():
        print(f"cable skip (iface already connected) {label}")
        continue
    cable = Cable.objects.create(status="planned", label=label)
    cable.tags.set([isl_tag])
    CableTermination.objects.create(cable=cable, termination_type=ct, termination_id=a.id, cable_end="A")
    CableTermination.objects.create(cable=cable, termination_type=ct, termination_id=b.id, cable_end="B")
    print(f"cable {label} id={cable.id}")

print(f"NetBox {SITE}: 4× {LEAF_DT} leaf, 2× {SPINE_DT} spine, {len(links)} ISL cables — ready for ApplyTopology")
