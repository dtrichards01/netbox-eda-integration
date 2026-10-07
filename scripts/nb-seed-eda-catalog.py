"""Seed NetBox DCIM catalog before EDA topology sync (Mode A).

Run BEFORE enabling Instance.spec.sync.enabled. EDA pushes TopoNodes as
NetBox Devices and maps TopoNode.spec.platform to an existing DeviceType.model.
It does not create Manufacturers for you.

DeviceType.model must match TopoNode.spec.platform EXACTLY (case/spacing).

After first sync, EDA auto-creates the EDAManaged tag and EDA custom fields (objectType / objectName; Nokia docs also list eda_managed).
"""
from dcim.models import Manufacturer, DeviceType, Platform, DeviceRole, Region
from extras.models import CustomField, Tag
from tenancy.models import Tenant

# One (region, tenant) per fabric — must match Instance.spec.sync in that namespace
FABRIC_TENANCY = [
    ("region-1", "tenant-a"),   # baseline: clab-3-tier-leaf-spine-dcgw
    ("region-2", "tenant-b"),   # second fabric e.g. clab-srl-leaf-spine-dcgw
    ("region-3", "tenant-c"),   # Mode B: fabric-dc2
]

MANUFACTURER = "Nokia"

LAB_DEVICE_TYPES = [
    ("7220 IXR-D2L", 1),
    ("7220 IXR-D3L", 1),
    ("7220 IXR-D4", 1),
    ("7750 SR-1", 2),
    ("7250 IXR-X1B", 1),
    ("7250 IXR-X3B", 1),
]

EXTENDED_DEVICE_TYPES = [
    ("7215 IXS-A1", 1),
    ("7220 IXR-D1", 1), ("7220 IXR-D5", 1),
    ("7220 IXR-H2", 4), ("7220 IXR-H3", 1), ("7220 IXR-H4-32D", 1),
    ("7220 IXR-H4", 2), ("7220 IXR-H5-32D", 1), ("7220 IXR-H5-64D", 2),
    ("7220 IXR-H5-64O", 2), ("7220 IXR-H6-64", 3),
    ("7250 IXR-X4", 1),
    ("7250 IXR-6e", 10), ("7250 IXR-10e", 16), ("7250 IXR-18e", 35),
    ("7750 SR-7", 8), ("7750 SR-12", 14), ("7750 SR-12e", 22),
    ("7750 SR-1x-48D", 2), ("7750 SR-1-48D", 2), ("7750 SR-1-24D", 2),
    ("7750 SR-1x-92S", 2), ("7750 SR-1-92S", 2), ("7750 SR-1-46S", 2),
    ("7750 SR-1s", 3), ("7750 SR-1se", 3), ("7750 SR-2s", 5), ("7750 SR-2se", 5),
    ("7750 SR-7s", 17), ("7750 SR-14s", 28),
]

DEVICE_TYPES = LAB_DEVICE_TYPES + EXTENDED_DEVICE_TYPES

PLATFORMS = [
    ("srl", "SR Linux"),
    ("sros", "SR OS"),
]

ROLES = ["leaf", "spine", "pe", "dcgw", "border-leaf"]


def unique_device_type_slug(mfr, model):
    """NetBox slug is unique per manufacturer; avoid collisions when generating slugs."""
    base = model.lower().replace(" ", "-").replace("/", "-")[:45]
    slug = base[:50]
    n = 2
    while DeviceType.objects.filter(manufacturer=mfr, slug=slug).exclude(model=model).exists():
        suffix = f"-{n}"
        slug = f"{base[: 50 - len(suffix)]}{suffix}"
        n += 1
    return slug


for region_name, tenant_name in FABRIC_TENANCY:
    region, rc = Region.objects.get_or_create(name=region_name, defaults={"slug": region_name})
    tenant, tc = Tenant.objects.get_or_create(name=tenant_name, defaults={"slug": tenant_name})
    print(f"region {region_name} created={rc} | tenant {tenant_name} created={tc}")

mfr, mc = Manufacturer.objects.get_or_create(name=MANUFACTURER, defaults={"slug": "nokia"})
print(f"manufacturer {MANUFACTURER} created={mc}")

for model, u_height in DEVICE_TYPES:
    slug = unique_device_type_slug(mfr, model)
    dt, created = DeviceType.objects.get_or_create(
        manufacturer=mfr,
        model=model,
        defaults={"slug": slug, "u_height": u_height},
    )
    if not created and dt.u_height != u_height:
        dt.u_height = u_height
        dt.save(update_fields=["u_height"])
        print(f"device-type {model} updated u_height={u_height}")
    else:
        print(f"device-type {model} created={created} u_height={dt.u_height}")

for name, desc in PLATFORMS:
    p, created = Platform.objects.get_or_create(
        name=name, defaults={"slug": name, "description": desc}
    )
    print(f"platform {name} created={created}")

for role_name in ROLES:
    slug = role_name.replace(" ", "-")
    r, created = DeviceRole.objects.get_or_create(
        name=role_name, defaults={"slug": slug, "color": "9e9e9e"}
    )
    print(f"role {role_name} created={created}")

print("\n=== EDA automation objects (created by controller on first sync) ===")
EDA_CFS = ["objectType", "objectName", "operatingSystem", "allocationObject", "ownerObject", "eda_managed"]
for cf in CustomField.objects.filter(name__in=EDA_CFS):
    types = [ct.model for ct in cf.object_types.all()]
    print(f"  custom-field {cf.name} type={cf.type} on={types}")
for t in Tag.objects.filter(name__icontains="EDAManaged"):
    print(f"  tag {t.name} slug={t.slug}")
if not CustomField.objects.filter(name="objectType").exists():
    print("  (objectType custom field not present yet — normal before first sync)")

print(f"\nCatalog seed complete ({len(DEVICE_TYPES)} device types). Enable Instance sync.")
