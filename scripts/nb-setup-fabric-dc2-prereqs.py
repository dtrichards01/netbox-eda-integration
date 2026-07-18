"""Mode B fabric-dc2 — NetBox prerequisites (§5.3).

Creates/updates: region-3, tenant-c, site fabric-dc2, allocation tags,
webhook EDA fabric-dc2, event rule EDA fabric-dc2 events.

Set WEBHOOK_SECRET before running (env var) or uses default lab value.
Prints WEBHOOK_SECRET=... for secrets-fabric-dc2.yaml.
"""
import os
from dcim.models import Region, Site
from extras.models import Webhook, EventRule, Tag
from tenancy.models import Tenant
from django.contrib.contenttypes.models import ContentType

WEBHOOK_NAME = "EDA fabric-dc2"
EVENT_RULE_NAME = "EDA fabric-dc2 events"
WEBHOOK_URL = (
    "https://eda-api.eda-system.svc.cluster.local:443"
    "/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox"
)
WEBHOOK_SECRET = os.environ.get(
    "FABRIC_DC2_WEBHOOK_SECRET", "fabric-dc2-wh-secret-change-me"
)

ALLOC_TAGS = [
    "eda-fabric-dc2-vlan",
    "eda-fabric-dc2-asn",
    "eda-fabric-dc2-systemip",
    "eda-fabric-dc2-mgmt",
    "eda-fabric-dc2-isl",
]

CONTENT_TYPE_MODELS = [
    ("dcim", "device"),
    ("dcim", "devicetype"),
    ("dcim", "site"),
    ("dcim", "cable"),
    ("ipam", "ipaddress"),
    ("ipam", "prefix"),
    ("ipam", "asn"),
    ("ipam", "asnrange"),
    ("ipam", "vlan"),
    ("ipam", "vlangroup"),
]

region, rc = Region.objects.get_or_create(name="region-3", defaults={"slug": "region-3"})
tenant, tc = Tenant.objects.get_or_create(name="tenant-c", defaults={"slug": "tenant-c"})
print(f"region-3 created={rc} | tenant-c created={tc}")

site, sc = Site.objects.get_or_create(
    name="fabric-dc2",
    defaults={"slug": "fabric-dc2", "status": "planned", "region": region, "tenant": tenant},
)
if not sc:
    site.region = region
    site.tenant = tenant
    site.status = "planned"
    site.save()
print(f"site fabric-dc2 id={site.id} created={sc}")

for tag_name in ALLOC_TAGS:
    slug = tag_name.replace("_", "-")[:100]
    t, created = Tag.objects.get_or_create(
        name=tag_name, defaults={"slug": slug, "color": "2196f3"}
    )
    print(f"tag {tag_name} created={created}")

wh, wc = Webhook.objects.update_or_create(
    name=WEBHOOK_NAME,
    defaults={
        "payload_url": WEBHOOK_URL,
        "http_method": "POST",
        "http_content_type": "application/json",
        "secret": WEBHOOK_SECRET,
        "ssl_verification": False,
    },
)
print(f"webhook {WEBHOOK_NAME} id={wh.id} created={wc} url={WEBHOOK_URL}")

cts = []
for app_label, model in CONTENT_TYPE_MODELS:
    ct = ContentType.objects.get(app_label=app_label, model=model)
    cts.append(ct)

er, ec = EventRule.objects.update_or_create(
    name=EVENT_RULE_NAME,
    defaults={
        "enabled": True,
        "action_type": "webhook",
        "action_object": wh,
        "event_types": ["object_created", "object_updated", "object_deleted"],
    },
)
er.object_types.set(cts)
print(f"event-rule {EVENT_RULE_NAME} id={er.id} created={ec} types={len(cts)}")

print(f"\nWEBHOOK_SECRET={WEBHOOK_SECRET}")
print("Prerequisites done — apply secrets-fabric-dc2.yaml with this signatureKey")
