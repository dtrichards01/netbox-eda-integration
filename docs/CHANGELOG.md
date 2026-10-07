# Changelog — NetBox ↔ EDA Technical Documentation

Document ID: **NETBOX-EDA-TD-001**

## Public v1.1 (2026-10-05) — audited master; full guide 2.3 (2026-10-06)

- **`NetBox-EDA-Technical-Documentation-public-v1.1.docx` is now the master** (author audit). It is not generated or edited from the markdown; everything else follows it. Baseline: EDA 26.8.1, NetBox app v7.0.1.
- Full guide (`NetBox-EDA-Technical-Documentation.md`, Word v2) brought into line with the master's audited wording:
  - Intro: "DCIM — Topology integration model" heading; the controller creates the `EDAManaged` tag and matching `eda_managed` custom field; new note that webhook connectivity is optional (use `ApplyAllocation` / `ApplyTopology` workflows instead).
  - Executive summary: allocations support both webhook and workflow models.
  - §3.2: onboarding CRs are copied according to the `eda.nokia.com/bootstrap` label; NodeUser patch is only needed when its `nodeSelector` is non-empty and lacks the NetBox labels (applies to hardware as well as Containerlab). Stale `Section 8.0–8.8` pointer removed.
  - §4.1.1 / §4.3: `eda_managed` restored alongside the tag and ownership custom fields; Extras → Custom Field permission marked "needs checking". The lab observation stays in the full guide only: `eda_managed` was not created after topology sync or allocation write-back (2026-10-06) — status "needs checking with Nokia".
  - §6.3 ASN finding: app version 4.0.3; Mode B ASN "Blocked (Under investigation)"; shared Instance name and overlapping ASN ranges stated as supported.
  - §8.3: Extras permissions are for `EDAManaged` / `eda_managed` automation.
  - §14 References: repository URL and the public v1.1 master.
- Fixed in the full guide only (the master has the same wording — flag for the next master revision): §5.2 NodeUser patch said `eda.nokia.com/source=netbox` comes "from your NetBox device tags", contradicting §5.5 (EDA sets it; tagging devices with it breaks `ApplyTopology`).
- §8.3 "See also" link pointed at a non-existent §4.3 anchor; now §4.2.
- Publish script ships public v1.1 (docx + markdown rendition) to the integration repo.

## Public v1 (2026-08-14) — for review

- **New public summary** (`NetBox-EDA-Technical-Documentation-public-v1.docx`) — condensed from Word v2 for external circulation. Published alongside the full guide in [netbox-eda-integration](https://github.com/dtrichards01/netbox-eda-integration), with a markdown rendition for GitHub readability.
- Review fixes applied to the summary:
  - **Removed all citations of sections that exist only in the detailed doc** — section-number cross-references are kept for the detailed doc. The trim had left 8 dangling (§9.4, §9.7, §10.8.1.5, §10.8.2, §10.8.3, §5.3.3 ×2); the sentences were rewritten to refer to "the full technical documentation" by name instead. `§10.8.1.5` previously read as an IP address in body text.
  - Trimmed the §-numbering legend to the sections this document actually contains (§4 Mode A, §5 Mode B, §6 IPAM theory).
  - Removed the stale `Section 8.0–8.8` pointer. **This error is also present in v2 and the full markdown** — not yet corrected there.
  - Added `Document version: Public v1` and a `Note:` line (lab-validated integration guide, a summary of the full technical documentation, not official Nokia product documentation).
  - Added a **References** section carrying the repository URL, both document paths, and EDA / NetBox documentation links.
- Moved the allocation pool tag step (lead-in, **Customization → Tags → Add**, tag table) from §6 up to §5.7, its first reference. In the summary layout §6 comes after §5.7, so a reader was told to tag IPAM objects before being shown how to create the tags. The how-to also belongs with the hands-on pool creation rather than the architecture section. Its trailing caveat was dropped rather than moved: in the new location the surrounding paragraphs already state that the tags are plain strings and that the whole step is optional.
- **Renumbered so the summary is self-consistent** rather than aligned with v2, which left gaps wherever content was omitted:
  - §11 → **§9** (EDA transactions, with 11.1–11.4 → 9.1–9.4) and §12 → **§10** (Constraints and anti-patterns). The body ran 1–8 then jumped to 11. Nothing cited 11 or 12 by number, so no cross-references were affected.
  - §4.3 → **§4.2**, §4.4 → **§4.3** (the gap at 4.2), and §5.3.4–5.3.7 → **§5.3.3–5.3.6** (the gap at 5.3.3, left by moving the tag step to §5.7). Citations of the moved subsections were remapped in the same pass, since doing it sequentially would have collided.
  - Numbered the one unnumbered subsection inside a numbered section: **§5.8 Mode A vs Mode B (summary)**.
  - Removed an empty `Heading 4`, which would have rendered as a blank table-of-contents entry. **It was also separating the two comparison tables in §5.8**, and Word merged them into one 9-row table on the next save, since it treats tables with nothing between them as one. They are separated by an empty body paragraph now — keep a paragraph between adjacent tables.
- Removed the remaining pointers into the full guide, which the first sweep missed because it searched for section marks only:
  - `Appendix E.2` / `Appendix E.3` citations (×4) — the summary has no appendices, so these were dead links. Now name the shipped script instead.
  - Reader-role table cited section 13 and Appendices B and E, none of which exist here.
  - Two `§4.4–4.5` ranges. An audit keyed on `§` misses a range's upper bound, so these went unnoticed twice; both now point at §4.2, which holds all the EDAManaged material in this document.
- Marked the table-of-contents field dirty so Word rebuilds it on open — it carries no cached entries, so the new numbering would not otherwise appear. Word drops the flag when it saves without updating fields, so it needs reapplying after each round-trip until the field is populated once (in Word: select all, then F9).
- Numbering legend now reads `§6 = IPAM Allocations` (author edit).
- Verified after renumbering: numbering is continuous at every level, and all 22 cited numbers resolve inside the summary, counting both single references and range bounds.

## Version 2.2.1 (2026-08-10) — draft

- **Word v2** (`NetBox-EDA-Technical-Documentation-v2.docx`) adopted as canonical master (edit Word first; sync markdown from v2)
- §6.3 ASN table: Mode B blocked — **Unknown** controller behaviour (was: known)
- §14 References: removed edactl namespace bootstrap bullet; removed end-of-document footer (matches v2)

## Version 2.2 (2026-08-10) — draft

- New **Introduction — EDA NetBox App** section (product overview from [docs.eda.dev/apps/netbox](https://docs.eda.dev/latest/apps/netbox/)): CR types, IPAM/topology models, webhooks, EDAManaged, link to lab Modes A/B
- Word export and canvas refreshed for v2.2

## Version 2.1.1 (2026-08-01) — draft

- ASN allocation §6.3: App version **4.0.1** behaviour — reconciler requires synced-site cache (`sync.enabled: true`); Mode B ASN pool blocked (lab finding)
- Word source: `NetBox-EDA-Technical-Documentation-v1.docx` adopted as canonical `.docx` export

## Version 2.1 (2026-07-27) — draft

- §5.7.5a: Mode A IPv6 ISL example (`2005::/64` Container, `/127`, tag `eda-clab3tier-isl-ipv6`, Allocation `eda-isl-ipv6`)
- §6.4.7: `clab-3-tier-leaf-spine-dcgw` six Allocation CRs table
- §7.1.1: Bootstrap `SubnetAllocationPool` vs NetBox-backed pools
- §8.1: ISL IPv4/IPv6 tag and prefix columns for clab3tier
- Appendix E.8–E.9: `nb-test-allocation-pools-clab3tier.py` and `nb-add-clab3tier-isl-ipv6-only.py`
- §4.1.1 / §9.4: Webhook + event rule prerequisites before EDA sync (`reachable=true` ≠ full DCIM mirror)
- Mode A build order and checklist: webhook + event rule before expecting full DCIM mirror

## Version 2.0 (2026-07-18)

- Professional document structure: executive summary, conventions, part-based TOC
- Revision history moved to this file
- Repository-relative paths (`scripts/`, `manifests/`)
- Part I–VII organization without renumbering core sections

## Version 1.56 (2026-07-20)

- Document owner: Darren Richards, Cloud & Enterprise

## Version 1.55 (2026-07-20)

- Extended catalog notes: SR-7s / SR-14s RU height — "depending on power config"

## Version 1.54 (2026-07-20)

- Replaced misaligned ASCII box diagrams (§3.1, §4.1, §5.1, §6.1, §7.1) with bordered tables for cleaner Word export

## Version 1.53 (2026-07-20)

- §5.6: removed fabric-dc2 troubleshooting table (redundant)

## Version 1.52 (2026-07-20)

- Mode B cables: omit NetBox `Cable.type` (optional DCIM field; not used by `ApplyTopology` or reflected in EDA `TopoLink`)

## Version 1.51 (2026-07-20)

- Word export: `apply-word-table-borders.py` post-processes every table (Table Grid + full grid borders + autofit)
- Lab fabric platforms table: `7250 IXR-X1B` / `X3B` → SR Linux; removed `(`srl`)` / `(`sros`)` from OS column

## Version 1.50 (2026-07-20)

- §3.2: CLI subsection renamed to **Namespace creation (edactl CLI)**; approach table shows `EDA Namespace CR` without `spec.bootstrap.fromNamespace` path
- §4.1: Mode A sync flow diagram aligned ASCII box; §4.1.1 Region/Tenant table separated from catalog prerequisites table
- Word export: reference template sample table with grid borders (pandoc inherits for all pipe tables)
- ISL subnet allocation: `subnetLength` **/30 → /31** across docs, manifests, and seed scripts (point-to-point links)

## Version 1.49 (2026-07-18)

- §3.2 terminology: "namespace bootstrap" → **namespace instantiation** (onboarding kit copy; distinct from ZTP/day-0 bootstrap)
- Removed misleading `repopulate` callout; updated §3.2 anchor, TOC, and cross-refs (§5.2, §9.6, §10.1, §10.8.2.1)

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
| 1.48 | 2026-07-18 | Lab documentation | §3.1 site↔namespace mapping clarified; §3.2 bootstrap — removed invalid `repopulate`; delete/recreate guidance |


