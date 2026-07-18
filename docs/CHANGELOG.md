# Changelog — NetBox ↔ EDA Technical Documentation

Document ID: **NETBOX-EDA-TD-001**

## Version 2.0 (2026-07-18)

- Professional document structure: executive summary, conventions, part-based TOC
- Revision history moved to this file
- Repository-relative paths (`scripts/`, `manifests/`)
- Part I–VII organization without renumbering core sections

## Version 1.47 (2026-07-18)

- Mode A clab allocations (`eda-clab3tier-*`)
- §6.3 ASN/sync gate documented
- §8.1 tag table + verify/setup scripts

## Earlier versions (1.0–1.46)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-16 | Lab documentation | Consolidated report + import guide; standard technical structure |
| 1.1 | 2026-07-16 | Lab documentation | Mode A catalog prep procedure; `nb-seed-eda-catalog.py` |
| 1.2 | 2026-07-17 | Lab documentation | §9.8 manual test guide with example CRs and scripts |
| 1.3 | 2026-07-17 | Lab documentation | Canvas linear layout; multi-namespace secrets (§7); enable checklist (§8) |
| 1.4 | 2026-07-17 | Lab documentation | EDAManaged expanded (§4.4); namespace bootstrap corrected (label on namespace) |
| 1.5 | 2026-07-17 | Lab documentation | Operating modes clarified (ApplyTopology workflow, DCIM perms, orphans); catalog script shown before run; roles/EDAManaged explained |
| 1.6 | 2026-07-17 | Lab documentation | Nokia hardware catalog expanded from datasheets (u_height); D4/X1B corrections |
| 1.7 | 2026-07-17 | Lab documentation | Full `EXTENDED_DEVICE_TYPES` table added to §4.1.1; header/canvas version synced to revision history |
| 1.8 | 2026-07-17 | Lab documentation | Instance CR + NetBox tag prerequisites (§4.4); EDAManaged/allocation/device tags clarified |
| 1.9 | 2026-07-17 | Lab documentation | Region/Tenant convention: `region-1`/`tenant-a` (first fabric), `region-2`/`tenant-b` (second) |
| 1.10 | 2026-07-17 | Lab documentation | Full inline YAML manifests paired with every `kubectl apply` example |
| 1.11 | 2026-07-17 | Lab documentation | Fixed catalog seed kubectl commands (WSL + PowerShell; no broken line continuations) |
| 1.12 | 2026-07-17 | Lab documentation | Catalog seed: NetBox 4.x imports, full Nokia catalog (36 SKUs), stdin shell redirect (avoids OOM), X1B/X3B lab platforms |
| 1.13 | 2026-07-17 | Lab documentation | Paste-safe catalog seed commands (no jsonpath/bash -c nesting); `nb-run-seed-catalog.sh` wrapper |
| 1.14 | 2026-07-17 | Lab documentation | §8.2 — shared NetBox API token across namespaces; per-namespace webhook secrets |
| 1.15 | 2026-07-17 | Lab documentation | Section numbering aligned: §3.1, §9.0–8.11, §10.8.0–9.8.4; TOC and cross-refs updated |
| 1.16 | 2026-07-17 | Lab documentation | §4.4 NetBox Instance YAML cleaned; kubectl apply blocks; canvas prose de-bracketed |
| 1.17 | 2026-07-17 | Lab documentation | NetBox Instance apply via heredoc — no YAML file required |
| 1.18 | 2026-07-17 | Lab documentation | NetBox Instance one-liner + `nb-apply-instance-clab.sh` for collapsed paste |
| 1.19 | 2026-07-17 | Lab documentation | `clab-3-tier-leaf-spine-dcgw` Instance script; removed fragile one-liner; YAML indent troubleshooting |
| 1.20 | 2026-07-17 | Lab documentation | Baseline `clab-3-tier` = region-1/tenant-a; secrets-from-NetBox + embedded Instance YAML in §4.4 |
| 1.21 | 2026-07-17 | Lab documentation | §4.4 heredoc paste format — `>` prompt, line breaks, wrapper scripts; secrets + Instance step checklist |
| 1.22 | 2026-07-17 | Lab documentation | §4.4 one-block Mode A apply (`nb-mode-a-baseline.sh`); heredoc steps in collapsible section |
| 1.23 | 2026-07-17 | Lab documentation | §4.4 two paste-safe single blocks + explicit warning: heredoc/base64 cannot run as one line |
| 1.24 | 2026-07-17 | Lab documentation | §4.4 YAML file workflow — secrets + Instance manifests, `kubectl apply -f`; lab files in Temp |
| 1.25 | 2026-07-17 | Lab documentation | §4.4 YAML blocks match file format — `#` header comments inside fenced blocks |
| 1.26 | 2026-07-17 | Lab documentation | Full doc sync: §4.4 second-fabric YAML; §9.1/8.2/§9.8 baseline namespace; Appendix C split |
| 1.27 | 2026-07-17 | Lab documentation | §4.4 restructured — filename headings, YAML-only fences, one source of truth |
| 1.28 | 2026-07-17 | Lab documentation | Canvas YAML uses preformatted blocks; §4.4 note on multi-line display |
| 1.29 | 2026-07-17 | Lab documentation | §5 Mode B DCIM import (build path); allocations renumbered to §6; §4 Mode A only through §4.4 |
| 1.30 | 2026-07-17 | Lab documentation | Canonical path note; Temp copy synced; TOC labels §5 Mode B / §6 Allocations |
| 1.31 | 2026-07-17 | Lab documentation | §5.4 nb-test-fabric-dc2.py — 4× D3L leaf, 2× D4 spine, 8 ISL cables |
| 1.32 | 2026-07-17 | Lab documentation | §5.3 namespace + bootstrap (fabric-dc2); §5.4–5.6 renumbered |
| 1.33 | 2026-07-17 | Lab documentation | §5.3 EDA `core.eda.nokia.com/v1` Namespace CR (UI method) + `edactl` bootstrap |
| 1.34 | 2026-07-17 | Lab documentation | §5.3 simplified — EDA Namespace CR + edactl only; removed K8s label fallback |
| 1.35 | 2026-07-17 | Lab documentation | §5.5 full nb-test-fabric-dc2.py + how-it-works; §9.6 manual onboarding YAML removed |
| 1.36 | 2026-07-17 | Lab documentation | §5.4 NetBox prerequisites (region/tenant/site/webhook) before EDA secrets; §5.5–5.7 renumbered |
| 1.37 | 2026-07-17 | Lab documentation | §5.4 numbered subsections (NetBox UI); §5.6.2 script run commands before full source |
| 1.38 | 2026-07-17 | Lab documentation | §5.2/§5.3 build order + empty-bootstrap troubleshooting; §5.6 anchor fixes; TOC Mode B subsections; §9.10 Mode B path |
| 1.39 | 2026-07-17 | Lab documentation | §5.6.2 full script before §5.6.3 run commands; `nb-test-fabric-dc2.py` in Appendix D; canvas embeds script |
| 1.40 | 2026-07-17 | Lab documentation | Appendix E — full `nb-seed-eda-catalog.py` + `nb-test-fabric-dc2.py`; §5.6 / §10.0 reference appendix only |
| 1.41 | 2026-07-17 | Lab documentation | Scripts quick reference at top; full appendix TOC; canvas Appendix E section |
| 1.42 | 2026-07-17 | Lab documentation | §5 numbering/TOC fixed (5.1–5.7, 5.5.x); §6.4 all allocation examples + NetBox tags; fabric-dc2 tag names aligned |
| 1.43 | 2026-07-17 | Lab documentation | Quick navigation banner; §6 TOC expanded (6.1–6.4); open-this-file callout |
| 1.44 | 2026-07-17 | Lab documentation | §5 renumbered — step N = §5.N (5.2 bootstrap … 5.7 allocations); expanded §5.3 NetBox prerequisites; full §5.7 allocation examples |
| 1.45 | 2026-07-17 | Lab documentation | Appendix E expanded — **full** source for all lab scripts (E.1–E.7); §10.8 partial snippets replaced with E.x pointers |
| 1.46 | 2026-07-18 | Lab documentation | §5.5/Appendix E.2 — device tag `site=fabric-dc2` (not `eda.nokia.com/source=netbox`); cable type `cat6`; ApplyTopology troubleshooting for forbidden source label and invalid `mmr` CableType |
| 1.47 | 2026-07-18 | Lab documentation | Mode A clab allocations (`eda-clab3tier-*`, `allocations-clab-3-tier-leaf-spine-dcgw.yaml`); §6.3 ASN/sync gate documented; §8.1 tag table + verify/setup scripts |


