"""Mode B / fabric-dc2: create all five tagged IPAM pools for Allocation CRs.

Tags match §5.7 / allocations-fabric-dc2.yaml (namespace-scoped plain strings).
Run inside NetBox pod before kubectl apply -f allocations-fabric-dc2.yaml
"""
from ipam.models import Prefix, VLANGroup, ASNRange, RIR
from extras.models import Tag

TAG_VLAN = "eda-fabric-dc2-vlan"
TAG_ASN = "eda-fabric-dc2-asn"
TAG_SYSTEMIP = "eda-fabric-dc2-systemip"
TAG_MGMT = "eda-fabric-dc2-mgmt"
TAG_ISL = "eda-fabric-dc2-isl"

SYSTEM_PREFIX = "10.0.1.0/24"
MGMT_PREFIX = "192.168.100.0/24"
ISL_PREFIX = "10.255.0.0/16"
ASN_START = 4200000000
ASN_END = 4200000999


def plain_tag(name: str):
    slug = name.replace("_", "-")[:100]
    tag, created = Tag.objects.get_or_create(
        name=name, defaults={"slug": slug, "color": "2196f3"}
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


tag_prefix(SYSTEM_PREFIX, "active", TAG_SYSTEMIP, "fabric-dc2 system / loopback IPs")
tag_prefix(MGMT_PREFIX, "active", TAG_MGMT, "fabric-dc2 management IPs")
tag_prefix(ISL_PREFIX, "container", TAG_ISL, "fabric-dc2 ISL /31-/30 subnets")

tag_vlan = plain_tag(TAG_VLAN)
try:
    from django.contrib.postgres.fields.ranges import NumericRange
    vid_range = [NumericRange(100, 200, "[)")]  # VIDs 100–199
except ImportError:
    vid_range = "100-199"

vg, vg_created = VLANGroup.objects.get_or_create(
    name="fabric-dc2-vlans",
    defaults={"slug": "fabric-dc2-vlans", "vid_ranges": vid_range},
)
vg.tags.set([tag_vlan])
print(f"vlan-group fabric-dc2-vlans created={vg_created} tag={TAG_VLAN} VID 100-199")

rir, _ = RIR.objects.get_or_create(name="Private", defaults={"slug": "private", "is_private": True})
tag_asn = plain_tag(TAG_ASN)
asn_range, asn_created = ASNRange.objects.get_or_create(
    name="fabric-dc2-asns",
    defaults={
        "slug": "fabric-dc2-asns",
        "rir": rir,
        "start": ASN_START,
        "end": ASN_END,
        "description": "fabric-dc2 private ASNs",
    },
)
asn_range.tags.set([tag_asn])
print(f"asn-range {ASN_START}-{ASN_END} created={asn_created} tag={TAG_ASN}")

print("\nNetBox IPAM ready — apply allocations-fabric-dc2.yaml in fabric-dc2 namespace")
