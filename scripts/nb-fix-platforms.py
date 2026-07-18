from dcim.models import Device, DeviceType, Platform, Manufacturer
from extras.models import Tag

# Fix SR-1 rack height
sr1 = DeviceType.objects.filter(model="7750 SR-1").first()
if sr1:
    old = sr1.u_height
    sr1.u_height = 2
    sr1.save()
    print(f"Updated 7750 SR-1 u_height: {old} -> {sr1.u_height}")

# Ensure platforms exist
platform_map = {
    "srl": "SR Linux",
    "sros": "SR OS",
}
platforms = {}
for slug, desc in platform_map.items():
    p, created = Platform.objects.get_or_create(
        name=slug,
        defaults={"slug": slug, "description": desc},
    )
    platforms[slug] = p
    print(f"platform {slug} created={created}")

# Map device name patterns / device types to platform
def platform_for_device(dev: Device) -> str | None:
    name = dev.name.lower()
    model = (dev.device_type.model if dev.device_type else "").lower()
    if name.startswith("sros-pe") or "7750 sr-1" in model or name.startswith("pe-"):
        return "sros"
    if name.startswith("srl-") or name.startswith("dcgw-") or "ixr" in model or "srl" in model:
        return "srl"
    if name.startswith("dc-gw"):
        return "sros"  # 3-tier site uses SR OS PEs
    if name.startswith("leaf-") or name.startswith("spine-"):
        return "srl"
    return None

updated = 0
for dev in Device.objects.all():
    slug = platform_for_device(dev)
    if not slug:
        print(f"skip (no mapping): {dev.name} dtype={dev.device_type}")
        continue
    if dev.platform_id != platforms[slug].id:
        dev.platform = platforms[slug]
        dev.save(update_fields=["platform"])
        updated += 1

print(f"Set platform on {updated} devices")
print("\n=== Verification ===")
for d in Device.objects.filter(name__in=["sros-pe-1", "srl-leaf-1", "dcgw-1"]):
    print(f"  {d.name} platform={d.platform} dtype_u={d.device_type.u_height}")

missing = Device.objects.filter(platform__isnull=True).count()
print(f"devices still missing platform: {missing}")
