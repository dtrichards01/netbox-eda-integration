# NetBox ↔ EDA Integration Guide

Technical documentation and lab scripts for integrating **Nokia Event-Driven Automation (EDA)** with **NetBox**.

## Start here

1. Read [`docs/NetBox-EDA-Technical-Documentation.md`](docs/NetBox-EDA-Technical-Documentation.md) (v1.47+)
2. Copy `manifests/secrets-*.yaml.example` → remove `.example`, fill in secrets
3. Run scripts from WSL against your EDA cluster + NetBox pod

## Layout

| Path | Contents |
|------|----------|
| `docs/` | Full technical documentation |
| `scripts/` | NetBox Django ORM scripts + lab orchestration |
| `manifests/` | Kubernetes CR examples |

## Known limitations (lab-validated)

- **Mode B ASN allocation** requires `sync.enabled: true` site cache — expect 4/5 pools in Mode B
- NetBox 4.x: use valid cable types (e.g. `cat6`, not `mmr`)
- Do not tag devices with `eda.nokia.com/source=netbox` — use `site=<siteName>`

## License

Documentation and scripts provided as-is for lab and educational use.
