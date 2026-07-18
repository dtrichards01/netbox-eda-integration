"""Mode A / clab-3-tier-leaf-spine-dcgw: create all five tagged IPAM pools.

Tags are namespace-scoped plain strings (eda-clab3tier-*).
Run inside NetBox pod before kubectl apply -f allocations-clab-3-tier-leaf-spine-dcgw.yaml
"""
from ipam.models import Prefix, VLANGroup, ASNRange, RIR
from extras.models import Tag

TAG_VLAN = "eda-clab3tier-vlan"
TAG_ASN = "eda-clab3tier-asn"
TAG_SYSTEMIP = "eda-clab3tier-systemip"
TAG_MGMT = "eda-clab3tier-mgmt"
TAG_ISL = "eda-clab3tier-isl"

SYSTEM_PREFIX = "10.0.10.0/24"
MGMT_PREFIX = "192.168.110.0/24"
ISL_PREFIX = "10.254.0.0/16"
ASN_START = 4200010000
ASN_END = 4200010999


def plain_tag(name: str):
    slug = name.replace("_", "-")[:100]
    tag, created = Tag.objects.get_or_create(
        name=name, defaults={"slug": slug, "color": "4caf50"}
    )
    print(f"tag {name} created={created}")
    return tag


def tag_prefix(cidr: str, status: str, tag_name: str, description: str):
    tag = plain_tag(tag_name)
    prefix, created = Prefix.objects.get_or_create(
        prefix=cidr,
        defaults={"status": status, "description": description},
    )
    if not created:
        prefix.status = status
        prefix.description = description
        prefix.save()
    prefix.tags.set([tag])
    print(f"prefix {cidr} status={status} tag={tag_name} created={created}")
    return prefix


tag_prefix(SYSTEM_PREFIX, "active", TAG_SYSTEMIP, "clab3tier system / loopback IPs")
tag_prefix(MGMT_PREFIX, "active", TAG_MGMT, "clab3tier management IPs")
tag_prefix(ISL_PREFIX, "container", TAG_ISL, "clab3tier ISL /31-/30 subnets")

tag_vlan = plain_tag(TAG_VLAN)
try:
    from django.contrib.postgres.fields.ranges import NumericRange
    vid_range = [NumericRange(300, 400, "[)")]  # VIDs 300-399
except ImportError:
    vid_range = "300-399"

vg, vg_created = VLANGroup.objects.get_or_create(
    name="clab3tier-vlans",
    defaults={"slug": "clab3tier-vlans", "vid_ranges": vid_range},
)
vg.tags.set([tag_vlan])
print(f"vlan-group clab3tier-vlans created={vg_created} tag={TAG_VLAN} VID 300-399")

rir, _ = RIR.objects.get_or_create(name="Private", defaults={"slug": "private", "is_private": True})
tag_asn = plain_tag(TAG_ASN)
asn_range, asn_created = ASNRange.objects.get_or_create(
    name="clab3tier-asns",
    defaults={
        "slug": "clab3tier-asns",
        "rir": rir,
        "start": ASN_START,
        "end": ASN_END,
        "description": "clab-3-tier-leaf-spine-dcgw private ASNs",
    },
)
asn_range.tags.set([tag_asn])
print(f"asn-range {ASN_START}-{ASN_END} created={asn_created} tag={TAG_ASN}")

print("\nNetBox IPAM ready — apply allocations-clab-3-tier-leaf-spine-dcgw.yaml")
