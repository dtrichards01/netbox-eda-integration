# NetBox ↔ EDA Integration Guide

Technical documentation and lab scripts for integrating **Nokia Event-Driven Automation (EDA)** with **NetBox**.

## Start here

1. New to the integration? Read the summary: [`docs/NetBox-EDA-Technical-Documentation-public-v1.1.md`](docs/NetBox-EDA-Technical-Documentation-public-v1.1.md) — architecture, both operating modes, IPAM design and constraints. The [`.docx`](docs/NetBox-EDA-Technical-Documentation-public-v1.1.docx) is the master if you want to comment in Word.
2. Need the reference detail? Read the full guide: [`docs/NetBox-EDA-Technical-Documentation.md`](docs/NetBox-EDA-Technical-Documentation.md) — adds the CR reference (§9), implementation procedures and manual test guide (§10), and appendices (§13). The summary cites these section numbers, so the two read together.
3. Copy `manifests/secrets-*.yaml.example` → remove `.example`, fill in secrets
4. Run scripts from WSL against your EDA cluster + NetBox pod

**Mode B end-to-end:** `bash scripts/run-mode-b-fabric-dc2.sh`  
Set `NETBOX_API_TOKEN` if you do not have a Mode A namespace to copy the API token from.  
Set `FABRIC_DC2_WEBHOOK_SECRET` to match your NetBox webhook signing secret.

## Layout

| Path | Contents |
|------|----------|
| `docs/NetBox-EDA-Technical-Documentation-public-v1.1.docx` / `.md` | Public summary — start here |
| `docs/NetBox-EDA-Technical-Documentation.md` | Full technical documentation |
| `docs/CHANGELOG.md` | Document revision history |
| `scripts/` | NetBox Django ORM scripts + lab orchestration |
| `manifests/` | Kubernetes CR examples |

## Feedback

The public summary is circulated for review and comment. Please raise comments as issues here, or return an annotated copy of the `.docx`.

## Known limitations (lab-validated)

- **Mode B ASN allocation** requires `sync.enabled: true` site cache — expect 4/5 pools in Mode B
- NetBox 4.x: use valid cable types (e.g. `cat6`, not `mmr`)
- Do not tag devices with `eda.nokia.com/source=netbox` — use `site=<siteName>`

## License

Documentation and scripts provided as-is for lab and educational use.
