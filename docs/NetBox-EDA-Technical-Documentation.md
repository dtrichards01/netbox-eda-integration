# NetBox ↔ EDA Technical Documentation

| Field | Value |
|-------|-------|
| **Document ID** | NETBOX-EDA-TD-001 |
| **Version** | 1.47 |
| **Status** | Draft |
| **Date** | 2026-07-17 |
| **Environment** | `kind-eda-demo-wsl2`, NetBox `http://localhost:8081`, EDA `https://localhost:9443` |

> **Canonical file:** `docs/NetBox-EDA-Technical-Documentation.md` in this repository.

### Revision history

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

---

> **v1.47 — open this exact file:** `./scripts\NetBox-EDA-Technical-Documentation.md`  
> **Not** the Cursor canvas (summary only). **Reload the editor tab** (close/reopen) if you still see v1.46 or older.  
> **Verify:** header shows **1.47** · Mode A clab allocations · §6.3 ASN/sync gate · Appendix **E.1–E.8** = complete scripts.

---

> **OPEN THIS FILE:** `./scripts\NetBox-EDA-Technical-Documentation.md` — **not** the Cursor canvas. Header must show **Version 1.47**.

### Quick navigation (latest)

| Topic | Jump to |
|-------|---------|
| Mode B build order (§5.1–5.7) | [§5.1 Overview + build order](#51-overview) |
| NetBox prerequisites (Mode B) | [§5.3](#53-netbox-prerequisites-fabric-dc2) |
| All 5 allocation pools + NetBox tags | [§5.7](#57-netbox-allocation-pools-fabric-dc2) |
| Scripts (catalog, DCIM, allocations) | [Scripts table](#scripts--where-to-find-them) · [Appendix E](#appendix-e--netbox-django-shell-scripts-full-source) |
| Hands-on allocations test | [§10.8.3](#1083-test-allocations-optional) |

---

### Scripts — where to find them

**Full Python source is in [Appendix E](#appendix-e--netbox-django-shell-scripts-full-source)** (§13, near end of this file — search for `Appendix E` or `#### E.1`).

| Script | Appendix | Mode | Lab file |
|--------|----------|------|----------|
| `nb-seed-eda-catalog.py` | [E.1](#e1-nb-seed-eda-catalogpy-mode-a) | A — catalog seed | `./scripts\nb-seed-eda-catalog.py` |
| `nb-test-fabric-dc2.py` | [E.2](#e2-nb-test-fabric-dc2py-mode-b) | B — DCIM fabric | `./scripts\nb-test-fabric-dc2.py` |
| `nb-test-allocation-pools-fabric-dc2.py` | [E.3](#e3-nb-test-allocation-pools-fabric-dc2py) | Allocations — fabric-dc2 (5 pools) | `./scripts\nb-test-allocation-pools-fabric-dc2.py` |
| `nb-test-allocation-pools-clab3tier.py` | [E.8](#e8-nb-test-allocation-pools-clab3tierpy) | Allocations — clab Mode A (5 pools) | `./scripts\nb-test-allocation-pools-clab3tier.py` |
| `nb-fix-platforms.py` | [E.4](#e4-nb-fix-platformspy) | Mode A post-sync platform fix | `./scripts\nb-fix-platforms.py` |
| `nb-run-seed-catalog.sh` | [E.7](#e7-nb-run-seed-catalogsh) | Wrapper — catalog seed stdin | `./scripts\nb-run-seed-catalog.sh` |
| `setup-allocations-both-namespaces.sh` | — | Create pools + apply Allocation CRs (both fabrics) | `./scripts\setup-allocations-both-namespaces.sh` |
| `verify-allocations-both.sh` | — | Verify Allocation status + EDA pools | `./scripts\verify-allocations-both.sh` |

> **Canvas vs this file:** Open this **`.md` file`** — confirm **Version 1.47** in the header. Allocations: [§5.7](#57-netbox-allocation-pools-fabric-dc2), [§10.8.3.1b](#10831b-mode-a-clab-allocations). Scripts: [Appendix E](#appendix-e--netbox-django-shell-scripts-full-source) (E.1–E.8, full source).

---

## Abstract

This document describes Nokia Event-Driven Automation (EDA) integration with NetBox: two topology operating modes (EDA-managed and NetBox-managed), IPAM allocation pools decoupled from DCIM inventory, configuration custom resources (CRs), implementation procedures, and lab-derived constraints. It supersedes the informal *Integration Report* and *Import Guide* as the single reference.

**Critical design rule:** one EDA Kubernetes namespace = one fabric context = one `Instance` CR + one webhook URL. Topology import and allocation pools share the `Instance` but not reconcile scope.

---

## 1. Scope and audience

### 1.1 Scope

**In scope:**

- EDA NetBox app: `Instance`, `Allocation`, `ApplyTopology`, `ApplyAllocation`
- DCIM topology (Site, Device, Interface, Cable) and IPAM pools (Prefix, VLAN Group, ASN Range)
- SR Linux (`platform: srl`) devices as `TopoNode` objects
- Lab cluster: `clab-srl-leaf-spine-dcgw` (EDA-managed) and `fabric-dc2` (NetBox-managed pattern)

**Out of scope:**

- NetBox installation and Helm chart configuration (except `ENFORCE_GLOBAL_UNIQUE`)
- Non-SRL platforms as `TopoNode` (may appear as cable endpoints only)
- EDA application development beyond the NetBox app

### 1.2 Audience

| Role | Primary sections |
|------|------------------|
| Network architect | 2, 3, 5 |
| EDA operator | 7, 8, 9 |
| NetBox administrator | 7, 8, 12 (Appendix B) |
| Automation engineer | 7, 9, 12 (Appendix B) |

---

## 2. Definitions and acronyms

| Term | Definition |
|------|------------|
| **DCIM** | NetBox Data Center Infrastructure Management (sites, devices, cables) |
| **IPAM** | NetBox IP Address Management (prefixes, VLANs, ASNs) |
| **CR** | Kubernetes Custom Resource in EDA |
| **Instance** | `netbox.eda.nokia.com/v1alpha1` CR — connection to one NetBox server per EDA namespace |
| **Allocation** | CR mapping tagged NetBox IPAM objects to EDA allocation pools |
| **ApplyTopology** | Workflow CR importing a NetBox site into EDA as TopoNode/TopoLink |
| **EDAManaged** | Reserved NetBox tag (+ `eda_managed` field) marking objects EDA created or claimed — see §4.4–4.5 |
| **TopoNode** | EDA topology CR representing an SR Linux node |
| **Reconcile** | `ApplyTopology` default — desired state = NetBox site only; orphans deleted |
| **Namespace bootstrap** | Label namespace `eda.nokia.com/bootstrap=true` → EDA auto-copies onboarding CRs from install `eda` namespace — see §3.2 |

---

## Table of contents

1. [Scope and audience](#1-scope-and-audience)
2. [Definitions and acronyms](#2-definitions-and-acronyms)
3. [Architecture overview](#3-architecture-overview)
   - [3.1 Integration paths and namespace model](#31-integration-paths-and-namespace-model)
   - [3.2 Namespace bootstrap](#32-namespace-bootstrap-onboarding-prerequisites)
4. [Mode A — EDA-managed DCIM sync](#4-mode-a--eda-managed-dcim-sync)
   - [4.1.1 Mode A — NetBox catalog prerequisites](#411-mode-a--netbox-catalog-prerequisites-before-sync)
   - [4.3 The EDAManaged tag](#43-the-edamanaged-tag)
   - [4.4 NetBox Instance CR (Mode A)](#44-netbox-instance-cr-mode-a)
5. [Mode B — NetBox-managed DCIM import](#5-mode-b--netbox-managed-dcim-import)
   - [5.1 Overview + build order](#51-overview)
   - [5.2 EDA namespace + bootstrap](#52-eda-namespace--bootstrap-fabric-dc2)
   - [5.3 NetBox prerequisites](#53-netbox-prerequisites-fabric-dc2) — [5.3.1](#531-catalog-objects-verify--usually-already-seeded) · [5.3.2](#532-create-region-tenant-and-site-in-netbox) · [5.3.3](#533-create-allocation-pool-tags-optional--before-57) · [5.3.4](#534-create-webhook-in-netbox) · [5.3.5](#535-create-event-rule-in-netbox) · [5.3.6](#536-not-needed-until-later) · [5.3.7](#537-global-setting-one-time-netbox-ui-or-admin)
   - [5.4 Secrets + Instance](#54-secrets--instance-cr-fabric-dc2) — [5.4.1](#541-secrets-fabric-dc2yaml) · [5.4.2](#542-instance-fabric-dc2yaml)
   - [5.5 NetBox DCIM](#55-netbox-dcim-modelling--devices-interfaces-cables) — [5.5.1](#551-topology-summary) · [5.5.2](#552-prepare-the-script) · [5.5.3](#553-run-the-script) · [5.5.4](#554-manual-alternative-netbox-ui)
   - [5.6 ApplyTopology](#56-applytopology-cr)
   - [**5.7 Allocation pools**](#57-netbox-allocation-pools-fabric-dc2) — VLAN · ASN · system IP · mgmt IP · ISL subnet
6. [Allocations — IPAM pools](#6-allocations--ipam-pools)
   - [6.3 Allocation CR types](#63-allocation-cr--all-pool-types)
   - [**6.4 Pool index (`fabric-dc2`)**](#64-lab-examples--all-pool-types-fabric-dc2) — see §5.7 for full examples
7. [Decoupling topology from allocations](#7-decoupling-topology-from-allocations)
8. [Multi-namespace conventions and permissions](#8-multi-namespace-conventions-and-permissions)
   - [8.1 Webhook URLs and tag naming](#81-webhook-urls-and-tag-naming)
   - [8.2 API token and webhook secrets (lab convention)](#82-api-token-and-webhook-secrets-lab-convention)
   - [8.3 NetBox API permissions](#83-netbox-api-permissions)
9. [Configuration reference — CRs and enable steps](#9-configuration-reference--crs-and-enable-steps)
   - [9.0 Overview](#90-overview) · [9.1 Secrets](#91-kubernetes-secrets-per-eda-namespace) · [9.2 Instance](#92-instance-cr-required-one-per-namespace) · [9.3 Webhook](#93-netbox-webhook-one-per-instance) · [9.4 Event rule](#94-netbox-event-rule) · [9.5 API token](#95-netbox-api-token-and-permissions) · [9.6 Namespace bootstrap](#96-eda-namespace-prerequisites-onboarding) · [9.7 DCIM (Mode B)](#97-topology-path-netbox-dcim-mode-b) · [9.8 IPAM allocations](#98-allocation-path-netbox-ipam--eda-crs)
10. [Implementation procedures](#10-implementation-procedures)
   - [10.0 Catalog seed (Mode A)](#100-procedure--seed-netbox-catalog-for-eda-sync-mode-a)
   - [10.8 Manual test guide](#108-manual-test-guide-with-example-crs-and-scripts) — [10.8.1 Mode A](#1081-mode-a--eda--netbox-sync) · [10.8.2 Mode B](#1082-mode-b--netbox--eda-import) · [10.8.3 Allocations](#1083-test-allocations-optional)
11. [EDA transactions](#11-eda-transactions)
12. [Constraints and anti-patterns](#12-constraints-and-anti-patterns)
13. [Appendices](#13-appendices)
    - [Appendix A — Naming](#appendix-a--naming-conventions-production)
    - [Appendix B — Django ORM scripts](#appendix-b--django-orm-scripts-lab)
    - [Appendix C — Lab file locations](#appendix-c--lab-file-locations)
    - [Appendix D — Kubernetes manifests](#appendix-d--example-kubernetes-manifest-files)
    - [Appendix E — **Scripts (full source)**](#appendix-e--netbox-django-shell-scripts-full-source)
      - [E.1 nb-seed-eda-catalog.py](#e1-nb-seed-eda-catalogpy-mode-a)
      - [E.2 nb-test-fabric-dc2.py](#e2-nb-test-fabric-dc2py-mode-b)
      - [E.3 nb-test-allocation-pools-fabric-dc2.py](#e3-nb-test-allocation-pools-fabric-dc2py)
      - [E.4 nb-fix-platforms.py](#e4-nb-fix-platformspy)
      - [E.5 nb-planned-fabric-full.py](#e5-nb-planned-fabric-fullpy-legacy-lab-site)
      - [E.6 nb-delete-planned-fabric.py](#e6-nb-delete-planned-fabricpy)
      - [E.7 nb-run-seed-catalog.sh](#e7-nb-run-seed-catalogsh)
14. [References](#14-references)

**Numbering convention:** Major sections use `§N` (e.g. §9). Subsections use `§N.M` (e.g. §9.1). **§4** = Mode A DCIM sync through Instance CR; **§5** = Mode B import (**§5.2** bootstrap through **§5.7** allocations; step number = section number in [§5.1](#51-overview)); **§6** = IPAM allocations theory (orthogonal to §4/§5). The manual test guide uses `§10.8.x.y`. Appendix D maps Kubernetes manifests; **Appendix E** holds full Python script source.

---

## 3. Architecture overview

### 3.1 Integration paths and namespace model

Nokia EDA's NetBox app exposes **two independent integration paths**:

| Path | NetBox module | Primary direction | Trigger |
|------|---------------|-----------------|---------|
| **Topology / inventory** | DCIM | Mode-dependent | `ApplyTopology` + optional `sync.enabled` |
| **Allocations** | IPAM | NetBox pools → EDA → consumed values back to NetBox | `Allocation` + webhook / `ApplyAllocation` |

| Concept | Where it lives | Notes |
|---------|----------------|-------|
| **K8s namespace** | EDA | Created first; all CRs live here |
| **NetBox site** | NetBox | Becomes label on TopoNode (`site: fabric-dc2`), not a namespace |
| **Node profile** | EDA `NodeProfile` + NetBox device tag | `eda.nokia.com/node-profile=<name>` |

**Namespace is defined in EDA, not NetBox.** NetBox holds sites and devices; EDA decides target namespace via `Instance` and `ApplyTopology` placement.

```
┌─────────────────────────────────────────────────────────────┐
│  Namespace A (e.g. clab-srl-leaf-spine-dcgw)                │
│  EDA-managed: sync.enabled=true  →  NetBox mirror (EDAManaged)│
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│  Namespace B (e.g. fabric-dc2)                              │
│  NetBox-managed: sync.enabled=false  ←  ApplyTopology import │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Namespace bootstrap (onboarding prerequisites)

Every new fabric namespace needs **onboarding kit** CRs before TopoNodes can onboard: `NodeProfile`, `NodeUser`, `Init`, mgmt/system IP pools, and related supporting resources. You do not need to hand-author these if bootstrap works.

#### How bootstrap works

At **EDA installation**, the default user namespace (typically `eda`) is populated with CRs that carry the label **`eda.nokia.com/bootstrap: "true"`** on each resource — NodeProfiles, NodeUsers, Init, allocation pools, etc. These are the **template** onboarding objects.

**Recommended — EDA `Namespace` CR** (same as EDA UI → Create namespace):

```yaml
apiVersion: core.eda.nokia.com/v1
kind: Namespace
metadata:
  name: fabric-dc2
  namespace: eda-system          # CR object lives in eda-system
spec:
  bootstrap:
    fromNamespace: eda           # copy bootstrap kit from template namespace
```

EDA creates the Kubernetes namespace `fabric-dc2` and copies bootstrap CRs in one step. Use `fromNamespace: clab-3-tier-leaf-spine-dcgw` (or another fabric) to inherit that namespace's NodeProfile set instead of generic `eda` profiles.

| What gets copied (typical) | Purpose |
|--------------------------|---------|
| **NodeProfile** | OS/version, onboarding creds, mgmt pool — name goes in NetBox `eda.nokia.com/node-profile=` tag |
| **NodeUser** | Permanent management user; referenced by NodeProfile |
| **NodeGroup** / **NodeUserGroup** | Group bindings for NodeUser |
| **Init** | Day-0 bootstrap for selected TopoNodes |
| **IPAllocationPool** / **SubnetAllocationPool** | Mgmt and system IP pools for onboarding |

**This is independent of NetBox** — bootstrap is pure EDA onboarding. It does **not** set `sync.enabled` or NetBox integration; that comes later via the `Instance` CR.

#### `edactl namespace bootstrap` (CLI)

Same result as the EDA `Namespace` CR — run via **`eda-toolbox`** (**not** `make edactl`):

```bash
kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl namespace bootstrap create --from-namespace eda fabric-dc2

kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl -n fabric-dc2 namespace bootstrap list

kubectl get nodeprofiles,nodeusers,inits,ipallocationpools,subnetallocationpools -n fabric-dc2
```

Use `--from-namespace clab-3-tier-leaf-spine-dcgw` to match clab NodeProfile names. If bootstrap is partial:

```bash
kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl -n fabric-dc2 namespace bootstrap repopulate --from-namespace eda
```

| Approach | When to use |
|----------|-------------|
| **EDA `Namespace` CR** (`spec.bootstrap.fromNamespace`) | **Recommended** — EDA UI; creates namespace + copies bootstrap kit |
| **`edactl namespace bootstrap create`** | CLI equivalent; namespace already exists |
| **`edactl namespace bootstrap repopulate`** | Refresh missing bootstrap CRs |
| **Manual YAML** | Custom profiles only |

**After bootstrap — NetBox-specific adjustments:**

1. Note the **NodeProfile name** copied into the namespace (e.g. `srl-leaf-spine-dcgw-srlinux-26.3.1`) — set matching tag on NetBox devices.
2. **Patch `NodeUser` `nodeSelector`** if imported TopoNodes use labels different from the clab template (e.g. add `eda.nokia.com/source=netbox`).
3. **Patch `Init` `nodeSelectors`** similarly if nodes will onboard via ZTP.
4. Bootstrap does **not** create NetBox `Instance` / `Allocation` CRs — add those separately (Section 8.0–8.8).

> The `eda.nokia.com/bootstrap=true` label marks which CRs are part of the namespace onboarding kit. Playground / clab namespaces are bootstrapped from the `eda-kpt-playground` package at install time; new fabric namespaces inherit the same kit via `bootstrap create`.

---

## 4. Mode A — EDA-managed DCIM sync

Mode A: EDA owns topology (`TopoNode` / `TopoLink`); NetBox mirrors DCIM with `EDAManaged`. Complete through [§4.4](#44-netbox-instance-cr-mode-a) before allocations ([§6](#6-allocations--ipam-pools)) or Mode B ([§5](#5-mode-b--netbox-managed-dcim-import)).

### 4.1 Mode A — EDA-managed (topology sync on)

**Pattern:** EDA owns the live fabric; NetBox is a **mirror** for visibility and IPAM bookkeeping.

```
EDA namespace (e.g. clab-srl-leaf-spine-dcgw)
  TopoNode / TopoLink / Interface  ──sync.enabled=true──►  NetBox DCIM
                                                           Site, Devices, Cables
                                                           tagged EDAManaged
```

| Setting | Value |
|---------|-------|
| `Instance.spec.sync.enabled` | `true` |
| `Instance.spec.sync.region` | NetBox Region for synced Site |
| `Instance.spec.sync.tenant` | NetBox Tenant for synced Site |
| NetBox Site | **Created/updated by EDA** — not your design source |
| `ApplyTopology` | Usually **not** used (topology born in EDA / Containerlab) |

**What EDA pushes to NetBox (when sync runs):**

| EDA object | NetBox object | Notes |
|------------|---------------|-------|
| `TopoNode` | Device (+ DeviceType) | Under synced Site |
| `TopoLink` | Cable | Between device interfaces |
| (implicit) | Site | Named from namespace / sync config |
| Interfaces | Device interfaces | Created as part of device sync |

All pushed DCIM objects receive the **`EDAManaged`** tag and `eda_managed` custom field. **Only EDA should mutate EDAManaged DCIM objects.**

**Typical lab example:** Containerlab fabric in `clab-3-tier-leaf-spine-dcgw` with `sync.enabled: true`, region `region-1`, tenant `tenant-a`. NetBox site mirrors the clab topology; devices carry `EDAManaged`.

**Direction of truth:** EDA → NetBox for devices/cables. Changes made manually in NetBox to EDAManaged devices risk being overwritten on the next sync cycle.

**Important:** With `sync.enabled: true`, adding a Device manually in NetBox does **not** create a `TopoNode` in EDA (lab: `srl-leaf-9` stayed NetBox-only). Sync is **EDA → NetBox** for DCIM inventory.

#### 4.1.1 Mode A — NetBox catalog prerequisites (before sync)

Before enabling `Instance.spec.sync.enabled`, seed NetBox with the **DCIM catalog** objects EDA needs to materialize `TopoNode`/`TopoLink` records. You are **not** creating individual device inventory here — EDA creates Sites, Devices, Cables, and (often) DeviceTypes during sync. You **are** ensuring lookup tables exist so the first reconcile succeeds.

| NetBox object | Required before sync? | Who creates device records? | Notes |
|---------------|----------------------|----------------------------|-------|
| **Region** | Yes — must match `Instance.spec.sync.region` | EDA creates Site under this region | See tenancy table below |
| **Tenant** | Yes — must match `Instance.spec.sync.tenant` | EDA assigns to synced Site/Devices | See tenancy table below |

**Region / Tenant per fabric** — one pair per namespace with `sync.enabled: true`. **Baseline:** first Mode A fabric uses `region-1` / `tenant-a`; each additional fabric increments the number and tenant letter (`region-2` / `tenant-b`, `region-3` / `tenant-c`, …). Seed all pairs in the catalog script before enabling each NetBox Instance.

| Order | EDA namespace (lab) | `Instance.spec.sync` | Notes |
|-------|----------------------|----------------------|-------|
| **Baseline** | `clab-3-tier-leaf-spine-dcgw` | `region: region-1`, `tenant: tenant-a` | First Mode A fabric |
| **Second** | `clab-srl-leaf-spine-dcgw` | `region: region-2`, `tenant: tenant-b` | Second Mode A fabric |
| **Planned import** | `fabric-dc2` | `sync.enabled: false` | Mode B — assign Region/Tenant on NetBox Site manually |

| **Manufacturer** | Yes (recommended) | — | Lab: `Nokia` |
| **DeviceType** | Yes — model must match `TopoNode.spec.platform` | EDA may also create DeviceTypes on push; pre-seeding avoids mapping errors | Lab: `7220 IXR-D2L`, `7220 IXR-D3L`, `7220 IXR-D4`, `7750 SR-1`, `7250 IXR-X1B`, `7250 IXR-X3B` |
| **Platform** | Recommended | EDA sets platform on synced devices when mapped | Lab: `srl`, `sros` — see `nb-fix-platforms.py` post-sync |
| **DeviceRole** | Recommended | EDA maps from **`eda.nokia.com/role`** label on each `TopoNode` (e.g. `leaf`, `spine`, `dcgw`, `border-leaf`) — these are **fabric role labels** on nodes in that namespace, not separate NetBox sites. Pre-create matching `DeviceRole` records so sync can set `Device.role`. |
| **Site / Device / Cable** | **No** — created by sync | **EDA** | Tagged `EDAManaged` after push |
| **`EDAManaged` tag + `eda_managed` field** | Pre-create tag optional; CF usually EDA-created | **EDA controller** (or you pre-create tag) | See §4.4–4.5 — must exist in NetBox before EDA can tag objects |

**`eda_managed` vs `EDAManaged`:** Two linked NetBox objects created on **first EDA reconcile** (sync or allocation):

| Object | Type | Purpose |
|--------|------|---------|
| **`EDAManaged`** | NetBox **tag** | Visible in UI filters; marks “EDA owns this object” |
| **`eda_managed`** | NetBox **custom field** (boolean) | Machine-readable flag on supported models; used by the NetBox app and API |

Both are set together when EDA creates or claims an object. The catalog script only **checks** whether they exist — it does not create them. Ensure the **`EDAManaged` tag exists in NetBox** (pre-create or let EDA create on first reconcile with Extras Tag/CF permissions) before expecting tagged sync results.

**Roles (`leaf` / `spine` / `dcgw`):** In EDA, each `TopoNode` carries labels such as `eda.nokia.com/role=leaf` and `site: <fabric-name>`. The fabric is the EDA **namespace** (and synced NetBox **Site**). Role labels describe the node's function **in that fabric**. The catalog seed pre-creates NetBox `DeviceRole` entries with the same names so Mode A sync can populate `Device.role`. Mode B: you set equivalent tags on NetBox devices before `ApplyTopology`.

**Lab fabric platforms** (match `TopoNode.spec.platform` in clab namespaces):

| `TopoNode.spec.platform` | u_height | OS (typical) |
|--------------------------|----------|--------------|
| `7220 IXR-D2L` | 1 | SR Linux (`srl`) |
| `7220 IXR-D3L` | 1 | SR Linux |
| `7220 IXR-D4` | 1 | SR Linux |
| `7750 SR-1` | 2 | SR OS (`sros`) |
| `7250 IXR-X1B` | 1 | SR OS |
| `7250 IXR-X3B` | 1 | SR OS |

**Adding more hardware:** The seed script loads **lab + extended** Nokia SKUs by default (`DEVICE_TYPES = LAB_DEVICE_TYPES + EXTENDED_DEVICE_TYPES`). Trim to `LAB_DEVICE_TYPES` only if you want a minimal catalog. Every distinct `TopoNode.spec.platform` needs a matching `DeviceType.model` (exact string). Re-run the script — `get_or_create` is idempotent and updates `u_height` if changed.

**Extended Nokia catalog (`EXTENDED_DEVICE_TYPES`):** Merged into the default seed list below. u_height from Nokia hardware datasheets. Lab models (D2L/D3L/D4, SR-1, X1B/X3B) are in `LAB_DEVICE_TYPES`; extended adds the rest.

| Family | `DeviceType.model` | u_height | Notes |
|--------|-------------------|----------|-------|
| **7215 IXS** | `7215 IXS-A1` | 1 | |
| **7220 IXR-D** | `7220 IXR-D1` | 1 | D2L, D3L, D4 in lab table |
| | `7220 IXR-D5` | 1 | |
| **7220 IXR-H** | `7220 IXR-H2` | 4 | |
| | `7220 IXR-H3` | 1 | |
| | `7220 IXR-H4-32D` | 1 | |
| | `7220 IXR-H4` | 2 | |
| | `7220 IXR-H5-32D` | 1 | |
| | `7220 IXR-H5-64D` | 2 | |
| | `7220 IXR-H5-64O` | 2 | OSFP112 variant |
| | `7220 IXR-H6-64` | 3 | |
| **7250 IXR-X** | `7250 IXR-X4` | 1 | X1B/X3B in lab table |
| **7250 IXR-e** | `7250 IXR-6e` | 10 | |
| | `7250 IXR-10e` | 16 | |
| | `7250 IXR-18e` | 35 | |
| **7750 SR** | `7750 SR-7` | 8 | SR-1 in lab table |
| | `7750 SR-12` | 14 | |
| | `7750 SR-12e` | 22 | |
| **7750 SR-1x** | `7750 SR-1x-48D` | 2 | 48D family |
| | `7750 SR-1-48D` | 2 | |
| | `7750 SR-1-24D` | 2 | |
| | `7750 SR-1x-92S` | 2 | 92S family |
| | `7750 SR-1-92S` | 2 | |
| | `7750 SR-1-46S` | 2 | |
| **7750 SR-s** | `7750 SR-1s` | 3 | |
| | `7750 SR-1se` | 3 | |
| | `7750 SR-2s` | 5 | |
| | `7750 SR-2se` | 5 | |
| | `7750 SR-7s` | 17 | Datasheet: 16 or 17 RU depending on config |
| | `7750 SR-14s` | 28 | Datasheet: 27 or 28 RU depending on config |

> **Platform string matching:** `DeviceType.model` must match `TopoNode.spec.platform` exactly (case/spacing). Lab uses `7250 IXR-X1B` and `7250 IXR-X3B`. Check platforms with:  
> `kubectl get toponodes -n <ns> -o jsonpath='{range .items[*]}{.spec.platform}{"\n"}{end}' | sort -u`  
> Interface port templates (QSFP-DD counts, etc.) are **not** created by the catalog script.

**Build order (Mode A):**

1. NetBox: Region, Tenant, Manufacturer, DeviceTypes, Platforms, DeviceRoles (catalog seed — Section 10.0)
2. EDA: namespace exists; Containerlab / workflows have `TopoNode`/`TopoLink` CRs
3. EDA: `Instance` CR with `sync.enabled: true`, matching `region`/`tenant`
4. NetBox: API token (DCIM write), webhook, event rules
5. Wait for sync — Devices, Site, Cables appear in NetBox with `EDAManaged`
6. Optional post-sync fixes: platform assignment, device-type `u_height` (`nb-fix-platforms.py`)

---

### 4.2 Mode A vs Mode B (summary)

| | Mode A (§4) | Mode B ([§5](#5-mode-b--netbox-managed-dcim-import)) |
|---|-------------|------------------------------------------------------|
| **Source of truth** | EDA `TopoNode` / `TopoLink` | NetBox Site / Devices / Cables |
| **NetBox Site** | EDA creates on sync | **You create** — not `EDAManaged` |
| **`sync.enabled`** | `true` | `false` |
| **Import to EDA** | Containerlab / workflows | **`ApplyTopology`** |
| **DCIM token perms** | create / update / delete | read (import only) |

Full comparison and Mode B build steps: [§5](#5-mode-b--netbox-managed-dcim-import). IPAM allocations: [§6](#6-allocations--ipam-pools) (either mode).

---

### 4.3 The EDAManaged tag

`EDAManaged` is a **reserved NetBox tag** (and matching **`eda_managed` boolean custom field**) used by the Nokia EDA NetBox app to mark objects EDA created or claimed.

**Important:** The tag is **not** defined on the EDA `Instance` CR. It is a **NetBox object** that must exist (or be created by EDA) before EDA can tag synced or allocated objects. Mode B design devices must **not** carry this tag — see [§5](#5-mode-b--netbox-managed-dcim-import).

#### Who creates `EDAManaged` / `eda_managed`

| Object | Typical creator | When |
|--------|-------------------|------|
| **`EDAManaged` tag** | EDA NetBox controller on **first reconcile**, **or you** pre-create in NetBox | Before/at first sync or first allocation write-back |
| **`eda_managed` custom field** | EDA controller on first reconcile (recommended) | Same — requires **Extras → Custom Field** API permission |

EDA needs **Extras → Tag** and **Extras → Custom Field** write permission on the API token to auto-create these. If reconcile fails to tag objects, verify permissions and that the `EDAManaged` tag exists in NetBox (**Customization → Tags**).

**Pre-create (optional but valid):** Create tag **`EDAManaged`** (slug `edamanaged`) in NetBox before applying the `Instance` CR if you want the tag visible before first reconcile. Do **not** rename or delete after EDA uses it. The `eda_managed` custom field is best left for EDA to create on first reconcile.

#### What it marks

Objects NetBox should treat as **owned by EDA**:

| Object | When it gets EDAManaged |
|--------|-------------------------|
| **Site, Device, Cable, DeviceType** (sync path) | EDA pushes them via topology sync (`sync.enabled: true`) |
| **IP Address, VLAN, ASN** (allocation path) | EDA allocates a value from a pool and writes it back to NetBox |
| **Your design site/devices** (Mode B) | **Never** — you create these without EDAManaged; EDA imports them to TopoNodes |

#### What “only EDA should mutate” means

- **Do not manually edit** EDAManaged devices, cables, or sites in the NetBox UI for routine changes — EDA is the source of truth for those objects (Mode A) or for tracking allocation ownership (IPAM).
- On the next **sync cycle**, EDA may **overwrite** manual NetBox edits to EDAManaged DCIM objects.
- **Do not delete** the `EDAManaged` tag or `eda_managed` custom field — the NetBox app depends on them.
- **Do not run `ApplyTopology`** against a site or devices that already carry `EDAManaged` — the workflow expects a NetBox-owned design source (Mode B only).

#### How to use it in practice

| Task | Action |
|------|--------|
| See what EDA synced from clab | NetBox → Devices → filter tag **`EDAManaged`** |
| See what EDA allocated from pools | NetBox → IP Addresses / VLANs → filter **`EDAManaged`** |
| Your planned fabric (Mode B) | Site and devices **without** EDAManaged; only consumed IPs/VLANs get it after allocation |
| Troubleshoot “who owns this device?” | If EDAManaged → EDA; if not → your team (or not yet synced) |

#### Mode summary

| Mode | EDAManaged on DCIM source? | EDAManaged on allocated IPAM? |
|------|---------------------------|-------------------------------|
| **A — EDA-managed** (`sync.enabled: true`) | Yes — all synced Site/Device/Cable | Yes — when EDA hands out pool values |
| **B — NetBox-managed** (`sync.enabled: false`) | **No** on your design site/devices | Yes — when EDA hands out pool values |

**Rule:** Never run `ApplyTopology` against a site that EDA already owns (`EDAManaged`). Never enable `sync.enabled` on a namespace whose NetBox site is your design source.

---

### 4.4 NetBox Instance CR (Mode A)

The **NetBox Instance CR** connects EDA to NetBox for this namespace. For Mode A, set `sync.enabled: true` with matching `region` / `tenant`.

**After §4.4:** configure NetBox webhook ([§9.3](#93-netbox-webhook-one-per-instance)) and verify sync ([§10.8.1.4–10.8.1.5](#10814-netbox-webhook--event-rule-ui)). Site and devices are **created by EDA on first sync** — not pre-modelled in NetBox.

Allocation pool tags and `Allocation` CRs are in [§6](#6-allocations--ipam-pools) (orthogonal to DCIM).

**Region / Tenant convention:** baseline namespace `clab-3-tier-leaf-spine-dcgw` → `region-1` / `tenant-a`. Each additional Mode A namespace increments: `region-2` / `tenant-b`, `region-3` / `tenant-c`, …

**Baseline fabric:** `clab-3-tier-leaf-spine-dcgw`. Apply **secrets YAML first**, then **Instance YAML** — same EDA namespace.

> **Multi-line YAML:** Each `yaml` code block below is a complete file with line breaks and indentation. Save manifests under `manifests/` in this repository (see `manifests/*.yaml.example` for secrets).

**Credentials** — edit `stringData` in the secrets file before apply:

| Value | NetBox UI location | YAML key |
|-------|-------------------|----------|
| API token | Admin → Authentication → API Tokens | `stringData.apiToken` on Secret `netbox-api-token` |
| Webhook secret | Operations → Integrations → Webhooks → **Secret** (this namespace) | `stringData.signatureKey` on Secret `netbox-webhook-signature` |

Lab: one API token across namespaces ([§8.2](#82-api-token-and-webhook-secrets-lab-convention)); webhook secret **unique per namespace**.

#### Mode A baseline — `clab-3-tier-leaf-spine-dcgw` (`region-1` / `tenant-a`)

Save each block below as the named file, edit `stringData`, then apply in order.

##### secrets-clab-3-tier-leaf-spine-dcgw.yaml

```yaml
# Edit stringData from NetBox UI before apply.
# apiToken     — Admin → Authentication → API Tokens
# signatureKey — Operations → Integrations → Webhooks → Secret (this namespace)
apiVersion: v1
kind: Secret
metadata:
  name: netbox-webhook-signature
  namespace: clab-3-tier-leaf-spine-dcgw
type: Opaque
stringData:
  signatureKey: paste-webhook-secret-from-netbox
---
apiVersion: v1
kind: Secret
metadata:
  name: netbox-api-token
  namespace: clab-3-tier-leaf-spine-dcgw
type: Opaque
stringData:
  apiToken: paste-netbox-api-token
```

##### instance-clab-3-tier-leaf-spine-dcgw.yaml

```yaml
# Baseline Mode A — region-1 / tenant-a. Apply secrets YAML first.
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Instance
metadata:
  name: netbox
  namespace: clab-3-tier-leaf-spine-dcgw
spec:
  url: http://netbox.netbox.svc.cluster.local:80
  apiToken: netbox-api-token
  signatureKey: netbox-webhook-signature
  sync:
    enabled: true
    region: region-1
    tenant: tenant-a
```

```bash
kubectl apply -f secrets-clab-3-tier-leaf-spine-dcgw.yaml
kubectl apply -f instance-clab-3-tier-leaf-spine-dcgw.yaml
kubectl get instance.netbox.eda.nokia.com netbox -n clab-3-tier-leaf-spine-dcgw -o jsonpath='reachable={.status.reachable}{"\n"}'
```

**Pass:** `reachable=true`

#### Mode A second fabric — `clab-srl-leaf-spine-dcgw` (`region-2` / `tenant-b`)

##### secrets-clab-srl-leaf-spine-dcgw.yaml

```yaml
# Second fabric — unique webhook secret for this namespace.
apiVersion: v1
kind: Secret
metadata:
  name: netbox-webhook-signature
  namespace: clab-srl-leaf-spine-dcgw
type: Opaque
stringData:
  signatureKey: paste-webhook-secret-from-netbox
---
apiVersion: v1
kind: Secret
metadata:
  name: netbox-api-token
  namespace: clab-srl-leaf-spine-dcgw
type: Opaque
stringData:
  apiToken: paste-netbox-api-token
```

##### instance-clab-srl-leaf-spine-dcgw.yaml

```yaml
# Second Mode A fabric — region-2 / tenant-b. Apply secrets YAML first.
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Instance
metadata:
  name: netbox
  namespace: clab-srl-leaf-spine-dcgw
spec:
  url: http://netbox.netbox.svc.cluster.local:80
  apiToken: netbox-api-token
  signatureKey: netbox-webhook-signature
  sync:
    enabled: true
    region: region-2
    tenant: tenant-b
```

```bash
kubectl apply -f secrets-clab-srl-leaf-spine-dcgw.yaml
kubectl apply -f instance-clab-srl-leaf-spine-dcgw.yaml
kubectl get instance.netbox.eda.nokia.com netbox -n clab-srl-leaf-spine-dcgw -o jsonpath='reachable={.status.reachable}{"\n"}'
```

| NetBox Instance field | Purpose |
|-----------------------|---------|
| `spec.url` | NetBox API base URL |
| `spec.apiToken` | Kubernetes Secret with NetBox REST token |
| `spec.signatureKey` | Kubernetes Secret with webhook HMAC secret |
| `spec.sync.enabled` | `true` for Mode A (EDA → NetBox push) |
| `spec.sync.region` / `.tenant` | NetBox Region and Tenant for synced Site |
| `spec.disableWebhook` | `true` disables auto-reconcile on NetBox events |

**Status:** `status.reachable`, `status.errorReason`, `status.lastChecked` — `reachable: true` before sync.

#### Mode A checklist (before first sync)

| # | NetBox | EDA |
|---|--------|-----|
| 1 | Region + Tenant exist ([§4.1.1](#411-mode-a--netbox-catalog-prerequisites-before-sync)) | TopoNodes in namespace ([§10.8.1.1](#10811-confirm-eda-fabric-exists)) |
| 2 | Catalog seeded — DeviceTypes, Roles | Namespace bootstrapped ([§3.2](#32-namespace-bootstrap-onboarding-prerequisites)) |
| 3 | `EDAManaged` pre-created **or** token has Extras Tag/CF write | Secrets + Instance CR applied ([§4.4](#44-netbox-instance-cr-mode-a)) |
| 4 | Webhook + event rule ([§9.3–9.4](#93-netbox-webhook-one-per-instance)) | `reachable=true` |
| 5 | — | Wait for sync → Site + devices appear with `EDAManaged` ([§10.8.1.5](#10815-verify-sync-in-netbox)) |

---

## 5. Mode B — NetBox-managed DCIM import

NetBox is the **design source** for DCIM. EDA imports topology via **`ApplyTopology`**. IPAM allocation pools are optional — [§5.7](#57-netbox-allocation-pools-fabric-dc2).

**Lab example:** EDA namespace `fabric-dc2`, NetBox site `fabric-dc2`, `sync.enabled: false`.

### 5.1 Overview

```
NetBox DCIM (site, no EDAManaged)  ──ApplyTopology──►  EDA namespace
  Site: fabric-dc2                                      TopoNode / Interface / TopoLink
  Devices (platform=srl, tagged)                        site label on TopoNode
  Interfaces, Cables
```

| Setting | Value |
|---------|-------|
| `Instance.spec.sync.enabled` | `false` |
| NetBox Site | **You create** — must **not** be `EDAManaged` |
| `ApplyTopology` | **Required** — workflow CR reads NetBox site → `TopoNode` / `TopoLink` |
| Device tags | `eda.nokia.com/node-profile=...` (required), role, custom labels |

**NetBox → EDA mapping:**

| NetBox (DCIM) | EDA CR | Requirements |
|---------------|--------|--------------|
| Device | `TopoNode` | Platform = `srl`; `eda.nokia.com/node-profile=<NodeProfile>` tag |
| Interface | `Interface` | On SRL devices |
| Cable | `TopoLink` | Both ends resolved |
| Site name | `TopoNode` label `site: <siteName>` | Not an EDA namespace |

**`ApplyTopology` default:** `operation: Reconcile` — orphans in the EDA namespace are **deleted**. Use a **dedicated** namespace; never import into a clab/Mode A namespace.

**Build order** — section number = step number:

| Step | § | Action |
|------|---|--------|
| 1 | **5.2** | EDA namespace + bootstrap; NodeUser patch |
| 2 | **5.3** | NetBox prerequisites (region, tenant, site, webhook, event rule) — **before** EDA secrets |
| 3 | **5.4** | `secrets-fabric-dc2.yaml` + `instance-fabric-dc2.yaml` → `reachable=true` |
| 4 | **5.5** | NetBox DCIM — `nb-test-fabric-dc2.py` (devices, interfaces, cables) |
| 5 | **5.6** | `applytopology-fabric-dc2.yaml` → TopoNodes / TopoLinks |
| 6 | **5.7** | (Optional) NetBox IPAM allocation pools + `allocations-fabric-dc2.yaml` |

### 5.2 EDA namespace + bootstrap (`fabric-dc2`)

Create a **dedicated** fabric namespace before any NetBox `Instance` or `ApplyTopology`. See [§3.2](#32-namespace-bootstrap-onboarding-prerequisites) for background.

**File: `eda-namespace-fabric-dc2.yaml`** (same as EDA UI → Create namespace)

```yaml
# Mode B — recommended. Matches EDA UI "Create namespace".
apiVersion: core.eda.nokia.com/v1
kind: Namespace
metadata:
  name: fabric-dc2
  namespace: eda-system          # CR object is stored in eda-system
spec:
  bootstrap:
    fromNamespace: eda           # or clab-3-tier-leaf-spine-dcgw | clab-srl-leaf-spine-dcgw
```

```bash
kubectl apply -f eda-namespace-fabric-dc2.yaml

kubectl get namespaces.core.eda.nokia.com -n eda-system fabric-dc2
kubectl get nodeprofiles,nodeusers,inits,ipallocationpools,subnetallocationpools -n fabric-dc2

NODE_PROFILE=$(kubectl get nodeprofiles -n fabric-dc2 -o jsonpath='{.items[0].metadata.name}')
echo "eda.nokia.com/node-profile=${NODE_PROFILE}"
```

> **Empty bootstrap after apply?** If the K8s namespace `fabric-dc2` exists but `kubectl get nodeprofiles -n fabric-dc2` returns nothing, the EDA `Namespace` CR did not copy bootstrap objects — run **`edactl namespace bootstrap create`** (below) or **`repopulate`** per [§3.2](#32-namespace-bootstrap-onboarding-prerequisites). Do not rely on a plain K8s namespace label alone.

| `spec.bootstrap.fromNamespace` | Result |
|--------------------------------|--------|
| `eda` | Generic profiles (`srlinux-ghcr-26.3.1`, …) — good default |
| `clab-3-tier-leaf-spine-dcgw` | Same NodeProfile names as baseline clab fabric |
| `clab-srl-leaf-spine-dcgw` | Same as second Mode A fabric |

**Or use `edactl`** (CLI equivalent — via `eda-toolbox`, **not** `make edactl`):

```bash
kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl namespace bootstrap create --from-namespace eda fabric-dc2

kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl -n fabric-dc2 namespace bootstrap list

kubectl get nodeprofiles,nodeusers,inits,ipallocationpools,subnetallocationpools -n fabric-dc2
NODE_PROFILE=$(kubectl get nodeprofiles -n fabric-dc2 -o jsonpath='{.items[0].metadata.name}')
echo "eda.nokia.com/node-profile=${NODE_PROFILE}"
```

| Bootstrap object | Purpose for Mode B |
|------------------|-------------------|
| **NodeProfile** | Name goes in NetBox device tag `eda.nokia.com/node-profile=<name>` |
| **NodeUser** / **Init** | Onboarding when TopoNodes are deployed (patch below for NetBox-sourced nodes) |
| **IPAllocationPool** / **SubnetAllocationPool** | Mgmt and system IP pools for future node onboarding |

> **EDA UI:** `fabric-dc2` may not appear meaningfully until bootstrap CRs exist. Refresh after apply or `edactl`.

**You do not hand-create** NodeProfile, NodeUser, Init, or IP pools — bootstrap (EDA Namespace CR or `edactl`) copies them from the template namespace. The only post-bootstrap edit in this lab is the **NodeUser patch** below so imported TopoNodes match SSH bindings.

**Patch NodeUser** so imported TopoNodes (label `eda.nokia.com/source=netbox` from your NetBox device tags) match SSH/credential bindings:

```bash
kubectl patch nodeuser admin -n fabric-dc2 --type=json -p='[
  {"op":"add","path":"/spec/groupBindings/-","value":{
    "groups":["sudo"],
    "nodeSelector":["eda.nokia.com/source=netbox"]
  }}
]'
```

**Pass:** `kubectl get nodeprofiles -n fabric-dc2` returns at least one profile; `NODE_PROFILE` printed for use in [§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables).

### 5.3 NetBox prerequisites (`fabric-dc2`)

Complete **after** [§5.2](#52-eda-namespace--bootstrap-fabric-dc2) and **before** [§5.4](#54-secrets--instance-cr-fabric-dc2). Everything in §5.3.2–§5.3.5 is created **directly in the NetBox UI** at `http://localhost:8081` — not via `kubectl`, YAML, or EDA. EDA secrets ([§5.4](#54-secrets--instance-cr-fabric-dc2)) need the webhook signing secret from §5.3.4.

#### 5.3.1 Catalog objects (verify — usually already seeded)

If you ran [§10.0](#100-procedure--seed-netbox-catalog-for-eda-sync-mode-a) / `nb-seed-eda-catalog.py`, these already exist in NetBox. Confirm in the UI; re-run the seed script if anything is missing.

| Object | NetBox UI path | Lab value | Needed for Mode B |
|--------|----------------|-----------|-------------------|
| Manufacturer | DCIM → Manufacturers | `Nokia` | Yes |
| Device type | DCIM → Device Types | `7220 IXR-D3L`, `7220 IXR-D4` | Yes — device script looks up types |
| Platform | DCIM → Platforms | `srl` | Yes |
| Device role | DCIM → Device Roles | `leaf`, `spine` | Yes |
| Region | Tenancy → Regions | `region-3` | Yes — assign to site in §5.3.2 |
| Tenant | Tenancy → Tenants | `tenant-c` | Yes |
| API token | Admin → API Tokens → Add | One token (reuse Mode A) | Yes — [§8.2](#82-api-token-and-webhook-secrets-lab-convention) |

**API token (if you do not already have one from Mode A):**

| Field | Value |
|-------|-------|
| **Description** | e.g. `EDA lab` |
| **Write enabled** | Yes |
| **Permissions** | Grant **write** on DCIM (Device, Interface, Cable, Site), IPAM (Prefix, VLAN Group, ASN Range, IP Address, VLAN, ASN), and **Extras** (Tag, Custom Field) — see [§8.3](#83-netbox-api-permissions) |

Copy the token once — it goes in `secrets-fabric-dc2.yaml` → `apiToken` ([§5.4.1](#541-secrets-fabric-dc2yaml)).

#### 5.3.2 Create region, tenant, and site in NetBox

**NetBox UI only** — Tenancy and DCIM menus.

**Example — Region**

1. **Tenancy → Regions → Add**
2. Name: `region-3`
3. **Create**

**Example — Tenant**

1. **Tenancy → Tenants → Add**
2. Name: `tenant-c`
3. **Create**

**Example — Site** (must match `ApplyTopology.spec.siteName`)

1. **DCIM → Sites → Add**
2. **Name:** `fabric-dc2`
3. **Status:** Planned
4. **Region:** `region-3`
5. **Tenant:** `tenant-c`
6. **Tags:** leave empty — **do not** add `EDAManaged`
7. **Create**

| # | NetBox UI path | Lab value | Notes |
|---|----------------|-----------|-------|
| 1 | **Tenancy → Regions → Add** | Name `region-3` | Skip if catalog seed already created it |
| 2 | **Tenancy → Tenants → Add** | Name `tenant-c` | Skip if catalog seed already created it |
| 3 | **DCIM → Sites → Add** | Name **`fabric-dc2`** | Region `region-3`, Tenant `tenant-c`, Status **planned**; **no** `EDAManaged` tag |

Site name must match `ApplyTopology.spec.siteName` (`fabric-dc2`). The device script ([§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables)) can `get_or_create` the site if you skip step 3 — creating it here assigns region/tenant in the UI first.

#### 5.3.3 Create allocation pool tags (optional — before §5.7)

If you plan to test IPAM allocations, create **plain string** tags now (same tags used in [§5.7](#57-netbox-allocation-pools-fabric-dc2)):

1. **Customization → Tags → Add** (repeat for each)

| Tag name | Used on |
|----------|---------|
| `eda-fabric-dc2-vlan` | VLAN Group |
| `eda-fabric-dc2-asn` | ASN Range |
| `eda-fabric-dc2-systemip` | Prefix (Active) |
| `eda-fabric-dc2-mgmt` | Prefix (Active) |
| `eda-fabric-dc2-isl` | Prefix (Container) |

> Allocation tags are **not** `key=value` device tags. Skip this subsection if you are only doing DCIM import (steps 1–5 in [§5.1](#51-overview)).

#### 5.3.4 Create webhook in NetBox

**NetBox UI only** — **Customization → Webhooks → Add** (NetBox 4.x: **Operations → Integrations → Webhooks → Add**)

**Full example:**

| Field | Value |
|-------|-------|
| **Name** | `EDA fabric-dc2` |
| **Enabled** | ✓ |
| **URL** | `https://eda-api.eda-system.svc.cluster.local:443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox` |
| **HTTP method** | POST |
| **HTTP content type** | application/json |
| **Secret** | e.g. `fabric-dc2-wh-secret-change-me` — **generate a new random string**; copy for `secrets-fabric-dc2.yaml` → `signatureKey` ([§5.4](#54-secrets--instance-cr-fabric-dc2)) |
| **SSL verification** | Disabled (lab self-signed) |
| **CA file path** | (empty) |

URL must be reachable **from the NetBox pod** (not browser `localhost`):

```bash
kubectl get svc eda-api -n eda-system
# Typical in-cluster URL:
# https://eda-api.eda-system.svc.cluster.local:443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox
```

Do **not** reuse the clab webhook URL or signing secret — each EDA namespace needs its own webhook + secret ([§8.1](#81-webhook-urls-and-tag-naming)).

#### 5.3.5 Create event rule in NetBox

**NetBox UI only** — **Customization → Event Rules → Add** (NetBox 4.x: **Operations → Integrations → Event Rules → Add**)

**Full example:**

| Field | Value |
|-------|-------|
| **Name** | `EDA fabric-dc2 events` |
| **Enabled** | ✓ |
| **Event types** | Object created · Object updated · Object deleted |
| **Action type** | Webhook |
| **Webhook** | `EDA fabric-dc2` (from §5.3.4) |
| **Object types** | Enable all rows below |

| Object type (NetBox UI) | Topology (§5.5–5.6) | Allocations (§5.7) |
|------------------------|---------------------|---------------------|
| DCIM → Cable | Optional | — |
| DCIM → Device | Optional | — |
| DCIM → Device Type | Optional | — |
| DCIM → Site | Optional | — |
| IPAM → ASN | — | **Yes** |
| IPAM → ASN Range | — | **Yes** |
| IPAM → IP Address | — | **Yes** |
| IPAM → Prefix | — | **Yes** |
| IPAM → VLAN | — | **Yes** |
| IPAM → VLAN Group | — | **Yes** |

For the full lab (topology + optional allocations), enable **all** types — same object set as Mode A ([§9.4](#94-netbox-event-rule)); only the webhook URL targets `fabric-dc2`.

#### 5.3.6 Not needed until later

| Item | When |
|------|------|
| Devices, interfaces, cables | [§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables) — `nb-test-fabric-dc2.py` |
| VLAN groups, prefixes, ASN ranges | [§5.7](#57-netbox-allocation-pools-fabric-dc2) — optional |
| `EDAManaged` on site or devices | **Never** on Mode B design objects |

#### 5.3.7 Global setting (one-time, NetBox UI or admin)

Confirm `ENFORCE_GLOBAL_UNIQUE=false` ([§8.3](#83-netbox-api-permissions)).

**Pass:** Site `fabric-dc2` visible in NetBox UI (no `EDAManaged`); webhook + event rule saved; webhook **Secret** and API token copied ready for [§5.4](#54-secrets--instance-cr-fabric-dc2).

### 5.4 Secrets + Instance CR (`fabric-dc2`)

#### 5.4.1 `secrets-fabric-dc2.yaml`

```yaml
# Mode B — edit stringData from NetBox UI before apply.
apiVersion: v1
kind: Secret
metadata:
  name: netbox-webhook-signature
  namespace: fabric-dc2
type: Opaque
stringData:
  signatureKey: paste-webhook-secret-from-netbox
---
apiVersion: v1
kind: Secret
metadata:
  name: netbox-api-token
  namespace: fabric-dc2
type: Opaque
stringData:
  apiToken: paste-netbox-api-token
```

#### 5.4.2 `instance-fabric-dc2.yaml`

```yaml
# Mode B — NetBox design source. sync.enabled: false
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Instance
metadata:
  name: netbox
  namespace: fabric-dc2
spec:
  url: http://netbox.netbox.svc.cluster.local:80
  apiToken: netbox-api-token
  signatureKey: netbox-webhook-signature
  sync:
    enabled: false
```

```bash
kubectl apply -f secrets-fabric-dc2.yaml
kubectl apply -f instance-fabric-dc2.yaml
kubectl get instance.netbox.eda.nokia.com netbox -n fabric-dc2 -o jsonpath='reachable={.status.reachable}{"\n"}'
```

### 5.5 NetBox DCIM modelling — devices, interfaces, cables

After [§5.4](#54-secrets--instance-cr-fabric-dc2) (`Instance` reachable). Creates leaf/spine devices **in NetBox** — via the script below (run inside NetBox pod) or manually in the NetBox UI.

#### 5.5.1 Topology summary

Django ORM script executed **inside the NetBox pod** (`manage.py shell`). Creates devices, interfaces, and cables at site `fabric-dc2`. Site may already exist from [§5.3.2](#532-create-region-tenant-and-site-in-netbox); script uses `get_or_create`.

| Role | Names | Device type | Uplinks |
|------|-------|-------------|---------|
| Leaf | `leaf-dc2-01` … `leaf-dc2-04` | `7220 IXR-D3L` | `ethernet-1/49` → spine-01, `ethernet-1/50` → spine-02 |
| Spine | `spine-dc2-01`, `spine-dc2-02` | `7220 IXR-D4` | `ethernet-1/1`–`ethernet-1/4` (one per leaf link) |

#### 5.5.2 Prepare the script

Full source: [Appendix E.2](#e2-nb-test-fabric-dc2py-mode-b). Copy `scripts/nb-test-fabric-dc2.py` and **edit `NODE_PROFILE`** to match [§5.2](#52-eda-namespace--bootstrap-fabric-dc2) bootstrap:

```bash
kubectl get nodeprofiles -n fabric-dc2 -o jsonpath='{.items[0].metadata.name}{"\n"}'
```

| Setting | Requirement |
|---------|-------------|
| `SITE` | `fabric-dc2` — must match `ApplyTopology.spec.siteName` |
| `NODE_PROFILE` | Must match a NodeProfile in `fabric-dc2` |
| Device tags | `eda.nokia.com/node-profile=…`, `eda.nokia.com/role=leaf` or `spine`, `site=fabric-dc2` — **do not** tag devices with `eda.nokia.com/source=netbox` (EDA sets that label on TopoNodes; putting it on NetBox device tags causes ApplyTopology to fail) |
| Cable tag | `eda.nokia.com/role=interSwitch` on each ISL |
| Cable type | `cat6` (must be a valid NetBox `CableType`; `mmr` is not valid in NetBox 4.x) |

Script is idempotent — safe to re-run.

#### 5.5.3 Run the script

After saving [Appendix E.2](#e2-nb-test-fabric-dc2py-mode-b) to disk, copy into the NetBox pod and execute:

```bash
# From WSL — lab file path
SCRIPT=./manifests/nb-test-fabric-dc2.py

POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-fabric-dc2.py').read())"
```

**Pass:** NetBox UI → DCIM → Devices at site `fabric-dc2` shows **6 devices**, **8 cables**; no `EDAManaged` tag on site or devices.

#### 5.5.4 Manual alternative (NetBox UI)

Create each device in **DCIM → Devices** with platform `srl`, device types above, and tags:

```
eda.nokia.com/node-profile=<NodeProfile-from-§5.2>
eda.nokia.com/role=leaf
site=fabric-dc2
```

Add interfaces and cables in DCIM. Optional cable tag: `eda.nokia.com/role=interSwitch`. Use a valid cable type (e.g. `cat6`). Plain string tags without `=` are ignored by `ApplyTopology` except `site=<siteName>`.

> **Do not** add `eda.nokia.com/source=netbox` to device tags. EDA applies that label internally on imported TopoNodes; NetBox device tags with that key are copied to TopoNode labels and rejected by the CE.

### 5.6 ApplyTopology CR

**File: `applytopology-fabric-dc2.yaml`**

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyTopology
metadata:
  name: import-fabric-dc2
  namespace: fabric-dc2
spec:
  instanceName: netbox
  siteName: fabric-dc2
  deviceTags: []
```

```bash
kubectl apply -f applytopology-fabric-dc2.yaml
kubectl get applytopology import-fabric-dc2 -n fabric-dc2 -o yaml
kubectl get toponodes -n fabric-dc2
```

**Pass:** `TopoNode` / `TopoLink` count matches NetBox site (6 TopoNodes, 8 TopoLinks for this lab).

**Troubleshooting (fabric-dc2 lab):**

| Symptom | Cause | Fix |
|---------|-------|-----|
| `mmr is not a valid CableType` in `eda-netbox` logs | Invalid cable `type` in NetBox | Use `cat6` (or another valid NetBox 4.x `CableType`); patch existing cables |
| `transaction execution failed` / 0 TopoNodes after ApplyTopology | `eda.nokia.com/source=netbox` on NetBox **device** tags | Remove from devices; use `site=fabric-dc2` instead. Keep `eda.nokia.com/source=netbox` only on **NodeUser** `nodeSelector` |
| ASN allocation `site not yet synced` with 6 TopoNodes present | Mode B (`sync.enabled: false`) — ASN pool may require site entry in `eda-netbox` site cache | Known gap; topology import still succeeds. See [§5.7](#57-netbox-allocation-pools-fabric-dc2) |

Hands-on walkthrough: [§10.8.2](#1082-mode-b--netbox--eda-import). Reference detail: [§9.7](#97-topology-path-netbox-dcim-mode-b).

### 5.7 NetBox allocation pools (`fabric-dc2`)

**Optional step 6** in [§5.1](#51-overview). Requires [§5.4](#54-secrets--instance-cr-fabric-dc2) (`Instance` reachable) and IPAM object types enabled in the event rule ([§5.3.5](#535-create-event-rule-in-netbox)). Allocation pool tags can be pre-created in [§5.3.3](#533-create-allocation-pool-tags-optional--before-57).

Create tagged IPAM objects in NetBox **before** `kubectl apply -f allocations-fabric-dc2.yaml`. Tags are **plain strings** (not `key=value` device tags). Theory and CR matrix: [§6.3](#63-allocation-cr--all-pool-types).

#### 5.7.0 Create all pools at once (script)

**File:** `nb-test-allocation-pools-fabric-dc2.py` — full source [Appendix E.3](#e3-nb-test-allocation-pools-fabric-dc2py). Creates all five NetBox objects + tags in one run:

```bash
SCRIPT=./scripts/nb-test-allocation-pools-fabric-dc2.py
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-fabric-dc2.py').read())"
```

Then apply EDA side ([§5.7.6](#576-apply-all-allocation-crs)).

#### 5.7.1 VLAN pool (`type: vlan`)

**NetBox UI — create VLAN Group**

1. **IPAM → VLAN Groups → Add**
2. **Name:** `fabric-dc2-vlans`
3. **Slug:** `fabric-dc2-vlans`
4. **Minimum VID / Maximum VID:** `100` / `199` (or add VID ranges after create)
5. **Tags:** `eda-fabric-dc2-vlan` (create tag in §5.3.3 if missing)
6. **Create**

**EDA Allocation CR** (`nb-fabric-dc2-vlan-pool` → `IndexAllocationPool`):

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-vlan-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-vlan]
  type: vlan
```

#### 5.7.2 ASN pool (`type: asn`)

**NetBox UI — create ASN Range**

1. **IPAM → ASN Ranges → Add**
2. **Name:** `fabric-dc2-asns`
3. **RIR:** Private
4. **Start ASN / End ASN:** `4200000000` / `4200000999`
5. **Tags:** `eda-fabric-dc2-asn`
6. **Create**

**EDA Allocation CR** (`nb-fabric-dc2-asn-pool` → `IndexAllocationPool`):

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-asn-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-asn]
  type: asn
```

#### 5.7.3 System IP pool (`type: ip-address`)

**NetBox UI — create Prefix (Active)**

1. **IPAM → Prefixes → Add**
2. **Prefix:** `10.0.1.0/24`
3. **Status:** **Active** (required — not Container)
4. **Tags:** `eda-fabric-dc2-systemip`
5. **Create**

**EDA Allocation CR** (`nb-fabric-dc2-systemip` → `IPAllocationPool`):

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-systemip
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-systemip]
  type: ip-address
```

#### 5.7.4 Management IP pool (`type: ip-in-subnet`)

**NetBox UI — create Prefix (Active)**

1. **IPAM → Prefixes → Add**
2. **Prefix:** `192.168.100.0/24`
3. **Status:** **Active**
4. **Tags:** `eda-fabric-dc2-mgmt`
5. **Create**

**EDA Allocation CR** (`nb-fabric-dc2-mgmt` → `IPInSubnetAllocationPool`):

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-mgmt
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-mgmt]
  type: ip-in-subnet
```

#### 5.7.5 ISL subnet pool (`type: subnet`)

**NetBox UI — create Prefix (Container)**

1. **IPAM → Prefixes → Add**
2. **Prefix:** `10.255.0.0/16`
3. **Status:** **Container** (required for subnet allocation)
4. **Tags:** `eda-fabric-dc2-isl`
5. **Create**

**EDA Allocation CR** (`nb-fabric-dc2-isl` → `SubnetAllocationPool`):

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-isl
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-isl]
  type: subnet
  subnetLength: 30
```

#### 5.7.6 Apply all Allocation CRs

**File: `allocations-fabric-dc2.yaml`** (multi-document — combines §5.7.1–§5.7.5):

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-systemip
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-systemip]
  type: ip-address
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-mgmt
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-mgmt]
  type: ip-in-subnet
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-isl
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-isl]
  type: subnet
  subnetLength: 30
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-asn-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-asn]
  type: asn
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-vlan-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-vlan]
  type: vlan
```

```bash
kubectl apply -f allocations-fabric-dc2.yaml
kubectl get allocation -n fabric-dc2
```

#### 5.7.7 Verify all pools

```bash
kubectl get allocation -n fabric-dc2
kubectl get allocation nb-fabric-dc2-vlan-pool -n fabric-dc2 -o jsonpath='matched={.status.matchedPrefixes}{"\n"}'
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n fabric-dc2
```

| Allocation CR | EDA pool kind | Pass |
|---------------|---------------|------|
| `nb-fabric-dc2-vlan-pool` | `IndexAllocationPool` | `status` shows matched VLAN group |
| `nb-fabric-dc2-asn-pool` | `IndexAllocationPool` | matched ASN range |
| `nb-fabric-dc2-systemip` | `IPAllocationPool` | matched Active prefix |
| `nb-fabric-dc2-mgmt` | `IPInSubnetAllocationPool` | matched Active prefix |
| `nb-fabric-dc2-isl` | `SubnetAllocationPool` | matched Container prefix |

Hands-on walkthrough: [§10.8.3](#1083-test-allocations-optional).

---

## 6. Allocations — IPAM pools

> **Mode B lab examples (all five pools):** [§5.7](#57-netbox-allocation-pools-fabric-dc2). This section covers architecture and CR reference; `fabric-dc2` walkthrough is in §5.7.

IPAM allocation pools are **orthogonal** to DCIM Mode A ([§4](#4-mode-a--eda-managed-dcim-sync)) and Mode B ([§5](#5-mode-b--netbox-managed-dcim-import)). Same `Instance` CR; pool tags on NetBox IPAM objects.

### 6.1 Architecture — one Instance per EDA namespace

A single NetBox **server** can serve many EDA namespaces. Each namespace gets its **own** integration binding:

```
                    ┌─────────────────────────────────────┐
                    │         NetBox (one server)          │
                    │  DCIM sites  │  IPAM pools (tagged)  │
                    └──────┬───────────────┬──────────────┘
                           │               │
         webhook/eda/ns1/netbox           │ same webhook path pattern
                           │               │
    ┌──────────────────────┼───────────────┼──────────────────────┐
    │                      ▼               ▼                      │
    │  Namespace: clab-srl-leaf-spine-dcgw                        │
    │    Instance (sync.enabled: true)   Allocation CRs (pools)   │
    │    TopoNodes (EDA-owned)           IndexAllocationPool ...   │
    └─────────────────────────────────────────────────────────────┘
    ┌─────────────────────────────────────────────────────────────┐
    │  Namespace: fabric-dc2                                        │
    │    Instance (sync.enabled: false)  Allocation CRs (pools)     │
    │    TopoNodes (NetBox-imported)     IPAllocationPool ...       │
    └─────────────────────────────────────────────────────────────┘
```

**Per namespace you deploy:**

1. Secrets: `netbox-api-token`, `netbox-webhook-signature` (see [§8.2](#82-api-token-and-webhook-secrets-lab-convention) — lab reuses one API token; webhook secret is always per namespace)
2. `Instance` CR
3. NetBox webhook URL: `https://<EDA>:9443/core/httpproxy/v1/netbox/webhook/<NAMESPACE>/<INSTANCE_NAME>`
4. NetBox Event Rule (can be one rule covering all object types — webhook URL differs per namespace)
5. Zero or more `Allocation` CRs
6. Optional: `ApplyTopology` / `ApplyAllocation` workflows

`Instance` and `Allocation` **must** live in the **same namespace**. The Allocation controller resolves `spec.instance` by name within that namespace only.

---

### 6.2 Instance CR — full options

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Instance
metadata:
  name: netbox                    # referenced by Allocation + ApplyTopology
  namespace: fabric-dc2           # one per fabric namespace
spec:
  url: http://netbox.netbox.svc.cluster.local:80
  apiToken: netbox-api-token      # secret name; key: apiToken (base64)
  signatureKey: netbox-webhook-signature  # secret name; key: signatureKey

  # Optional
  checkInterval: 1m               # NetBox reachability probe (default 1m)
  timeout: 10s                    # per-request API timeout (default 10s)
  disableWebhook: false           # true = no auto-reconcile on NetBox events
  tls:
    skipVerify: false
    trustBundle: my-ca-bundle     # ConfigMap with trust-bundle.pem

  sync:
    enabled: false                # true = EDA→NetBox topology push (Mode A)
    region: region-1              # NetBox Region for synced Site (sync only)
    tenant: tenant-a              # NetBox Tenant for synced Site (sync only)
```

| Field | Affects topology? | Affects allocations? |
|-------|-------------------|----------------------|
| `sync.enabled` | **Yes** — EDA→NetBox device/cable push | **No** |
| `sync.region` / `sync.tenant` | Yes (synced Site metadata) | No |
| `disableWebhook` | No (sync is controller-driven) | **Yes** — use `ApplyAllocation` manually if true |
| `url`, `apiToken`, TLS | Both | Both |

**Status fields:** `reachable`, `errorReason`, `lastChecked`

---

### 6.3 Allocation CR — all pool types

`Allocation` maps **tagged NetBox IPAM objects** → **EDA allocation pools**. Matching is by **plain string tags** on IPAM objects (not `key=value` device tags).

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-vlan-pool   # becomes EDA pool name
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox                # Instance CR in same namespace
  tags:
    - eda-fabric-dc2-vlan          # plain string tag on NetBox VLAN Group
  type: vlan
  subnetLength: 30                # required for type: subnet only
  description: ""                 # optional
```

#### Complete type matrix

| `spec.type` | NetBox source | Prefix status | EDA pool CRD | Typical use |
|-------------|---------------|---------------|--------------|-------------|
| `ip-address` | Prefix | **Active** | `IPAllocationPool` | System / loopback IPs |
| `ip-in-subnet` | Prefix | **Active** | `IPInSubnetAllocationPool` | Management IP (address + mask) |
| `subnet` | Prefix | **Container** | `SubnetAllocationPool` | ISL / point-to-point link subnets |
| `asn` | ASN Range | n/a | `IndexAllocationPool` | BGP private ASNs |
| `vlan` | VLAN Group | n/a | `IndexAllocationPool` | VLAN IDs |

#### ASN allocation and `sync.enabled` (lab finding)

VLAN and prefix-based pools (`vlan`, `ip-address`, `ip-in-subnet`, `subnet`) reconcile from **tagged NetBox IPAM objects only** — they work in both Mode A and Mode B.

**ASN is different.** The `eda-netbox` allocation reconciler also requires the namespace site to be in its internal **synced-site cache**. That cache is populated when `Instance.spec.sync.enabled: true` (Mode A DCIM sync). With `sync.enabled: false` (Mode B), even a correctly tagged ASN range in NetBox and a healthy `ApplyTopology` import will log:

```
site not yet synced ... sync.enabled=false
```

| Mode | `sync.enabled` | VLAN / IP pools | ASN pool |
|------|----------------|-----------------|----------|
| A — EDA-managed (`clab-3-tier-leaf-spine-dcgw`) | `true` | Matched | **Matched** |
| B — NetBox-managed (`fabric-dc2`) | `false` | Matched | **Blocked** (known controller behaviour) |

This is **not** caused by sharing the same `Instance` name (`netbox`) across namespaces — each namespace resolves `spec.instance` locally. It is **not** caused by overlapping ASN numeric ranges — matching is by **tag**. Mode B lab: expect **4/5** Allocation CRs matched; use Mode A namespace for full ASN pool testing until Nokia documents a Mode B workaround.

**Tag rule:** one distinct tag per pool mapping. Multiple NetBox objects with the same tag can feed one `Allocation` (status shows `matchedPrefixes` / matched ranges).

**Example — five pools in one namespace (`fabric-dc2` tags per [§8.1](#81-webhook-urls-and-tag-naming)):**

```yaml
# --- VLAN (IndexAllocationPool) ---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-vlan-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-vlan]
  type: vlan
---
# --- ASN (IndexAllocationPool) ---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-asn-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-asn]
  type: asn
---
# --- System IPs (IPAllocationPool) ---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-systemip
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-systemip]
  type: ip-address
---
# --- Management IPs (IPInSubnetAllocationPool) ---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-mgmt
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-mgmt]
  type: ip-in-subnet
---
# --- ISL subnets (SubnetAllocationPool) ---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-isl
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-isl]
  type: subnet
  subnetLength: 30
```

#### NetBox IPAM setup (summary)

| `spec.type` | NetBox object | Tag (`fabric-dc2`) | Status / range |
|-------------|---------------|-------------------|----------------|
| `vlan` | VLAN Group | `eda-fabric-dc2-vlan` | VID range e.g. 100–199 |
| `asn` | ASN Range | `eda-fabric-dc2-asn` | e.g. 4200000000–4200000999 |
| `ip-address` | Prefix | `eda-fabric-dc2-systemip` | **Active** e.g. `10.0.1.0/24` |
| `ip-in-subnet` | Prefix | `eda-fabric-dc2-mgmt` | **Active** e.g. `192.168.100.0/24` |
| `subnet` | Prefix | `eda-fabric-dc2-isl` | **Container** e.g. `10.255.0.0/16` |

Full NetBox UI steps and per-pool examples: [§5.7](#57-netbox-allocation-pools-fabric-dc2).

IPAM objects are **not scoped to a DCIM site**. Separation across namespaces is by **tag naming** ([§8.1](#81-webhook-urls-and-tag-naming)), not site membership.

#### Trigger and verify

**File: `applyallocation-refresh-fabric-dc2.yaml`** (on-demand reconcile — repeat per pool name)

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyAllocation
metadata:
  name: refresh-fabric-dc2-vlan
  namespace: fabric-dc2
spec:
  allocation: nb-fabric-dc2-vlan-pool
```

```bash
kubectl apply -f applyallocation-refresh-fabric-dc2.yaml
kubectl get instance,allocation -n fabric-dc2
kubectl get allocation nb-fabric-dc2-vlan-pool -n fabric-dc2 -o yaml
kubectl get ipallocationpools,subnetallocationpools,indexallocationpools -n fabric-dc2
```

**When EDA consumes a value** (Fabric app, onboarding, etc.):

- Individual IP / VLAN / ASN is **created in NetBox IPAM**
- Object gets **`EDAManaged`** tag + EDA custom fields (allocation owner, requesting CR)
- Parent pool prefix / VLAN group / ASN range stays **your** object — not fully taken over

---

### 6.4 Lab examples — all pool types (`fabric-dc2`)

> **Canonical walkthrough:** [§5.7](#57-netbox-allocation-pools-fabric-dc2) (Mode B build step 6). This subsection is a short index; full NetBox UI steps, per-pool Allocation YAML, and `allocations-fabric-dc2.yaml` are in §5.7.

Create tagged IPAM objects in NetBox **before** `kubectl apply -f allocations-fabric-dc2.yaml`. Tags are **plain strings** (not `key=value` device tags).

#### 6.4.0 Run all pools (script)

**File:** `nb-test-allocation-pools-fabric-dc2.py` — full source [Appendix E.3](#e3-nb-test-allocation-pools-fabric-dc2py). Creates all five objects + tags in one run:

```bash
SCRIPT=./scripts/nb-test-allocation-pools-fabric-dc2.py
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-fabric-dc2.py').read())"
```

Then apply EDA side:

```bash
kubectl apply -f allocations-fabric-dc2.yaml
kubectl get allocation -n fabric-dc2
```

#### 6.4.1 VLAN (`type: vlan`)

| Item | Lab value |
|------|-----------|
| **NetBox UI** | IPAM → VLAN Groups → Add |
| **Name** | `fabric-dc2-vlans` |
| **VID ranges** | `100`–`199` |
| **Tag** | `eda-fabric-dc2-vlan` (Extras → Tags → Add if missing; assign on VLAN Group) |
| **Allocation CR** | `nb-fabric-dc2-vlan-pool`, `spec.type: vlan`, `spec.tags: [eda-fabric-dc2-vlan]` |
| **EDA pool CRD** | `IndexAllocationPool` |

#### 6.4.2 ASN (`type: asn`)

| Item | Lab value |
|------|-----------|
| **NetBox UI** | IPAM → ASN Ranges → Add |
| **Name** | `fabric-dc2-asns` |
| **RIR** | Private |
| **Range** | `4200000000` – `4200000999` |
| **Tag** | `eda-fabric-dc2-asn` |
| **Allocation CR** | `nb-fabric-dc2-asn-pool`, `spec.type: asn` |
| **EDA pool CRD** | `IndexAllocationPool` |

#### 6.4.3 System IP (`type: ip-address`)

| Item | Lab value |
|------|-----------|
| **NetBox UI** | IPAM → Prefixes → Add |
| **Prefix** | `10.0.1.0/24` |
| **Status** | **Active** (required — not Container) |
| **Tag** | `eda-fabric-dc2-systemip` |
| **Allocation CR** | `nb-fabric-dc2-systemip`, `spec.type: ip-address` |
| **EDA pool CRD** | `IPAllocationPool` |

#### 6.4.4 Management IP (`type: ip-in-subnet`)

| Item | Lab value |
|------|-----------|
| **NetBox UI** | IPAM → Prefixes → Add |
| **Prefix** | `192.168.100.0/24` |
| **Status** | **Active** |
| **Tag** | `eda-fabric-dc2-mgmt` |
| **Allocation CR** | `nb-fabric-dc2-mgmt`, `spec.type: ip-in-subnet` |
| **EDA pool CRD** | `IPInSubnetAllocationPool` |

#### 6.4.5 ISL subnet (`type: subnet`)

| Item | Lab value |
|------|-----------|
| **NetBox UI** | IPAM → Prefixes → Add |
| **Prefix** | `10.255.0.0/16` |
| **Status** | **Container** (required for subnet allocation) |
| **Tag** | `eda-fabric-dc2-isl` |
| **Allocation CR** | `nb-fabric-dc2-isl`, `spec.type: subnet`, `spec.subnetLength: 30` |
| **EDA pool CRD** | `SubnetAllocationPool` |

#### 6.4.6 Verify all pools

```bash
kubectl get allocation -n fabric-dc2
kubectl get allocation nb-fabric-dc2-vlan-pool -n fabric-dc2 -o jsonpath='matched={.status.matchedPrefixes}{"\n"}'
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n fabric-dc2
```

| Allocation CR | EDA pool kind | Pass |
|---------------|---------------|------|
| `nb-fabric-dc2-vlan-pool` | `IndexAllocationPool` | `status` shows matched VLAN group |
| `nb-fabric-dc2-asn-pool` | `IndexAllocationPool` | matched ASN range |
| `nb-fabric-dc2-systemip` | `IPAllocationPool` | matched Active prefix |
| `nb-fabric-dc2-mgmt` | `IPInSubnetAllocationPool` | matched Active prefix |
| `nb-fabric-dc2-isl` | `SubnetAllocationPool` | matched Container prefix |

Hands-on walkthrough: [§10.8.3](#1083-test-allocations-optional).

---

## 7. Decoupling topology from allocations

### 7.1 Two paths, one namespace

```
┌─────────────────────────────────────────────────────────────────────────┐
│ EDA namespace: fabric-dc2                                                │
│                                                                          │
│  TOPOLOGY PATH (DCIM)              ALLOCATION PATH (IPAM)                │
│  ─────────────────────             ────────────────────────                │
│  ApplyTopology                     Allocation CRs                        │
│       │                                 │                                │
│       ▼                                 ▼                                │
│  TopoNode, Interface, TopoLink     IPAllocationPool /                    │
│                                    SubnetAllocationPool /                │
│                                    IndexAllocationPool                   │
│                                                                          │
│  sync.enabled: false               Always active via Allocation CRs      │
│  (no EDA→NetBox device push)      (independent of sync.enabled)         │
└─────────────────────────────────────────────────────────────────────────┘
         │                                      │
         ▼                                      ▼
┌─────────────────┐                   ┌─────────────────┐
│ NetBox DCIM     │                   │ NetBox IPAM     │
│ Site, Devices,  │                   │ Prefixes, VLAN  │
│ Cables          │                   │ Groups, ASN     │
│ (your design)   │                   │ Ranges (pools)  │
└─────────────────┘                   └─────────────────┘
```

| Dimension | Topology (DCIM) | Allocations (IPAM) |
|-----------|-------------------|---------------------|
| **Scoped by** | NetBox **site** (`ApplyTopology.spec.siteName`) | **Tags** on IPAM objects |
| **Site association** | Required for devices/cables | **Not required** |
| **EDA workflow** | `ApplyTopology` | `Allocation` + `ApplyAllocation` |
| **Controlled by `sync.enabled`** | **Yes** (EDA→NetBox push) | **No** |
| **Import direction** | NetBox → EDA (when managed) | NetBox pool defs → EDA pools |
| **Export direction** | EDA → NetBox (when sync on) | EDA allocations → NetBox IPAM objects |
| **EDAManaged on source** | Mode A: all synced DCIM | Never on pool definitions |
| **EDAManaged on consumption** | N/A | Individual allocated IPs/VLANs/ASNs |

### 7.2 Combined deployment patterns

#### Pattern 1 — Clab / EDA-managed fabric (lab default)

| Component | Setting |
|-----------|---------|
| Namespace | `clab-srl-leaf-spine-dcgw` |
| `Instance.sync.enabled` | `true` |
| Topology | Born in EDA; mirrored to NetBox |
| Allocations | Optional `Allocation` CRs for VLAN/ASN/IP pools |
| NetBox DCIM | Read-only mirror (`EDAManaged`) |
| NetBox IPAM | Tagged pools + `EDAManaged` on consumed values |

#### Pattern 2 — Greenfield planned fabric (NetBox design source)

| Component | Setting |
|-----------|---------|
| Namespace | `fabric-dc2` (dedicated) |
| `Instance.sync.enabled` | `false` |
| Topology | Modelled in NetBox → `ApplyTopology` |
| Allocations | `Allocation` CRs + IPAM pools (can pre-exist before devices) |
| NetBox DCIM | Your source of truth (no `EDAManaged`) |
| NetBox IPAM | Pools untagged/`EDAManaged` only on allocations |

#### Pattern 3 — Hybrid (common in production)

- **NetBox-managed** planned site imported to EDA (`sync.enabled: false`)
- **Shared IPAM pools** tagged per namespace (e.g. `eda-fabric-dc2-vlan` vs `eda-clab-vlan`)
- Same NetBox server, **separate** `Instance` + webhook per namespace
- Fabric / Init / NodeProfile reference allocation pools **in their namespace**

### 7.3 What is shared vs isolated

| Shared across namespaces (lab) | Per namespace (always) |
|--------------------------------|------------------------|
| NetBox API token **value** (one token in NetBox UI, same literal in each `netbox-api-token` secret) | K8s `Secret` objects (`netbox-api-token`, `netbox-webhook-signature`) |
| NetBox server URL (`Instance.spec.url`) | Webhook URL path (`.../webhook/<namespace>/netbox`) |
| | Webhook `signatureKey` (unique signing secret) |
| | `Instance` CR, `sync.region` / `sync.tenant` |

### 7.4 Recommended build order

1. Create EDA namespace + **`edactl namespace bootstrap create`** (NodeProfile, NodeUser, Init, pools — Section 3.2)
2. Secrets + **`Instance`** + NetBox webhook for **this namespace**
3. **`Allocation` CRs** + NetBox IPAM pools (optional but do before Fabric/onboarding)
4. NetBox DCIM: site, devices, interfaces, cables
5. **`ApplyTopology`**
6. **`ApplyAllocation`** if webhooks did not reconcile pools

---

## 8. Multi-namespace conventions and permissions

### 8.1 Webhook URLs and tag naming

**One webhook URL per namespace** — the path includes namespace and Instance name:

Examples (webhook — use address **reachable from NetBox pod**, not browser localhost):

```
https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-3-tier-leaf-spine-dcgw/netbox
https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-srl-leaf-spine-dcgw/netbox
https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox
```

| Access from | EDA URL |
|-------------|---------|
| **Your browser** (UI, EDA Explorer) | `https://localhost:9443` |
| **NetBox webhook** (HTTP call from NetBox pod) | `https://eda-api.eda-system.svc.cluster.local:443/...` or LB IP from `kubectl get svc eda-api -n eda-system` — **not** `localhost` |

**Suggested tag naming** to avoid cross-namespace pool collisions (`fabric-dc2` lab):

| Namespace | VLAN | ASN | System IP | Mgmt IP | ISL subnet |
|-----------|------|-----|-----------|---------|------------|
| `clab-3-tier-leaf-spine-dcgw` | `eda-clab3tier-vlan` | `eda-clab3tier-asn` | `eda-clab3tier-systemip` | `eda-clab3tier-mgmt` | `eda-clab3tier-isl` |
| `clab-srl-leaf-spine-dcgw` | `eda-clab-vlan` | `eda-clab-asn` | `eda-clab-systemip` | `eda-clab-mgmt` | `eda-clab-isl` |
| `fabric-dc2` | `eda-fabric-dc2-vlan` | `eda-fabric-dc2-asn` | `eda-fabric-dc2-systemip` | `eda-fabric-dc2-mgmt` | `eda-fabric-dc2-isl` |

Device tags remain `key=value` (e.g. `eda.nokia.com/node-profile=fabric-dc2-srlinux-26.3.1`).

---

### 8.2 API token and webhook secrets (lab convention)

**This lab uses one NetBox API token across all EDA namespaces.** Create a single token in NetBox (Admin → API tokens) with the permissions in [§8.3](#83-netbox-api-permissions). Store the **same literal value** in each fabric namespace's `Secret/netbox-api-token`. Each namespace still has its **own** Secret object — EDA only reads secrets in the `Instance`'s namespace.

**Webhook signing secrets are always per namespace.** Each fabric gets a unique `signatureKey` in `Secret/netbox-webhook-signature` and a matching NetBox webhook whose URL path includes that namespace (§8.1). Do not reuse webhook secrets across namespaces.

| Credential | This lab | Alternative (stricter isolation) |
|------------|----------|--------------------------------|
| **NetBox API token** | One token; duplicate value into each namespace's `netbox-api-token` secret | Issue a separate NetBox token per fabric with scoped object permissions |
| **Webhook `signatureKey`** | Unique per namespace + dedicated NetBox webhook | Same — always per namespace |

> You can mix approaches: e.g. shared API token for all Mode A clab fabrics, but a dedicated token for a production `fabric-dc2` namespace with tighter DCIM scope.

---

### 8.3 NetBox API permissions

These are the **object permissions** on the NetBox API token referenced by `Instance.spec.apiToken`. EDA calls the NetBox REST API as that token user.

| Mode | NetBox token needs | Why |
|------|-------------------|-----|
| NetBox-managed import only (`sync.enabled: false`) | IPAM: read+write (for allocations); DCIM: **read** | `ApplyTopology` workflow **reads** site/devices/cables; it does not write DCIM back |
| EDA-managed sync (`sync.enabled: true`) | IPAM: read+write; DCIM: **create/update/delete** | Sync **creates and updates** Site, Device, Cable, interfaces in NetBox |
| Allocations only | IPAM: read+write; DCIM: read | Pools and consumed values only |

Also required: `Extras > Tag`, `Extras > Custom Field` (for `EDAManaged` / `eda_managed` automation).

See also [§4.3](#43-side-by-side-comparison--devices-interfaces-cables) — **DCIM API perms** row.

---

## 9. Configuration reference — CRs and enable steps

Consolidated checklist of every CR and NetBox setting required to enable integration. **Reference only** — apply in your environment with your namespace names, URLs, and tags.

### 9.0 Overview

| Path | EDA CRs | NetBox config |
|------|---------|---------------|
| **Topology (DCIM)** | `Instance` + optional `ApplyTopology` | Site, devices, interfaces, cables |
| **Allocations (IPAM)** | `Instance` + `Allocation` (+ `ApplyAllocation`) | Tagged prefixes, VLAN groups, ASN ranges |
| **EDA → NetBox mirror** | `Instance` with `sync.enabled: true` | Webhook + DCIM write permissions |

**Rule:** one EDA namespace = one `Instance` CR + one webhook URL.

**YAML file convention:** Throughout this section and §9, each apply step shows the **full manifest** (save as the named file) followed by the **`kubectl apply`** command. Review the YAML first; apply when values match your environment.

---

### 9.1 Kubernetes secrets (per EDA namespace)

Full YAML per namespace: [§4.4](#44-netbox-instance-cr-mode-a) (Mode A) or [§5.4](#54-secrets--instance-cr-fabric-dc2) (Mode B). **Lab convention ([§8.2](#82-api-token-and-webhook-secrets-lab-convention)):** same `apiToken` in every namespace; unique `signatureKey` per namespace.

```bash
kubectl apply -f secrets-<namespace>.yaml
```

### 9.2 Instance CR (required; one per namespace)

> **Tags are not part of the Instance CR.** Ensure NetBox tags exist per [§4.4](#44-netbox-instance-cr-mode-a) before sync, allocations, or ApplyTopology.

#### Mode A — EDA-managed (clab pattern)

EDA owns topology; NetBox is a mirror. **Pre-seed NetBox catalog** before enabling sync — see [Section 10.0](#100-procedure--seed-netbox-catalog-for-eda-sync-mode-a). Full YAML manifests: [§4.4](#44-netbox-instance-cr-mode-a).

**Baseline** — apply secrets, then Instance:

```bash
kubectl apply -f secrets-clab-3-tier-leaf-spine-dcgw.yaml
kubectl apply -f instance-clab-3-tier-leaf-spine-dcgw.yaml
kubectl get instance.netbox.eda.nokia.com netbox -n clab-3-tier-leaf-spine-dcgw -o jsonpath='reachable={.status.reachable}{"\n"}'
```

**Second fabric** — `secrets-clab-srl-leaf-spine-dcgw.yaml` then `instance-clab-srl-leaf-spine-dcgw.yaml` (region-2 / tenant-b).

#### Mode B — NetBox-managed (design source)

NetBox owns DCIM; EDA imports via `ApplyTopology`. Instance YAML: [§5.4](#54-secrets--instance-cr-fabric-dc2).

```bash
kubectl apply -f secrets-fabric-dc2.yaml
kubectl apply -f instance-fabric-dc2.yaml
kubectl get instance.netbox.eda.nokia.com netbox -n fabric-dc2 -o jsonpath='reachable={.status.reachable}{"\n"}'
```

#### Optional Instance fields

| Field | Default | When to set |
|-------|---------|-------------|
| `checkInterval` | `1m` | Reachability probe interval |
| `timeout` | `10s` | NetBox API timeout |
| `disableWebhook` | `false` | `true` if you only use `ApplyAllocation` manually |
| `tls.skipVerify` | `false` | `true` for self-signed NetBox HTTPS |
| `tls.trustBundle` | — | ConfigMap name with `trust-bundle.pem` |

**Verify:** `kubectl get instance netbox -n <ns> -o yaml` → `status.reachable: true`

---

### 9.3 NetBox webhook (one per Instance)

**Operations → Integrations → Webhooks**

| Field | Value |
|-------|-------|
| **URL** | `https://<EDA_ADDR>:9443/core/httpproxy/v1/netbox/webhook/<NAMESPACE>/<INSTANCE_NAME>` |
| **Method** | POST |
| **Secret** | Same plaintext string as `signatureKey` secret (before base64) |
| **SSL verification** | Off for lab self-signed; on in production |

Examples:

Examples (webhook — use address **reachable from NetBox pod**, not browser localhost):

```
https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-3-tier-leaf-spine-dcgw/netbox
https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-srl-leaf-spine-dcgw/netbox
https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox
```

| Access from | EDA URL |
|-------------|---------|
| **Your browser** (UI, EDA Explorer) | `https://localhost:9443` |
| **NetBox webhook** (HTTP call from NetBox pod) | `https://eda-api.eda-system.svc.cluster.local:443/...` or LB IP from `kubectl get svc eda-api -n eda-system` — **not** `localhost` |

---

### 9.4 NetBox event rule

**Operations → Integrations → Event Rules**

| Field | Value |
|-------|-------|
| **Enabled** | Yes |
| **Event types** | Object created, updated, deleted |
| **Action** | Webhook → select webhook from §9.3 |
| **Object types** | See table below |

| Object type | Topology sync | Allocations |
|-------------|---------------|-------------|
| IPAM → IP Address | | ✓ |
| IPAM → Prefix | | ✓ |
| IPAM → ASN / ASN Range | | ✓ |
| IPAM → VLAN / VLAN Group | | ✓ |
| DCIM → Device | ✓ (`sync.enabled: true`) | |
| DCIM → Device Type | ✓ (`sync.enabled: true`) | |
| DCIM → Site | ✓ (`sync.enabled: true`) | |
| DCIM → Cable | ✓ (`sync.enabled: true`) | |

---

### 9.5 NetBox API token and permissions

**Admin → Authentication → API Tokens** — enable **write** on the token.

| Object | NetBox-managed import | EDA-managed sync | Allocations |
|--------|----------------------|------------------|-------------|
| IPAM: IPAddress, Prefix, ASN, ASNRange, VLAN, VLANGroup | write | write | write |
| DCIM: Site, Device, DeviceType, Cable | **read** | **write** | read |
| Extras: Tag, Custom Field | write | write | write |

**NetBox global setting** (multi-topology / overlapping IPs):

```
ENFORCE_GLOBAL_UNIQUE=false
```

---

### 9.6 EDA namespace prerequisites (onboarding)

Bootstrap is documented in [§5.2](#52-eda-namespace--bootstrap-fabric-dc2). EDA Namespace CR or `edactl` copies **NodeProfile, NodeUser, Init, IP pools** automatically — no hand-authored onboarding YAML in this lab.

| After bootstrap | Action |
|-----------------|--------|
| NodeProfile name | Use in NetBox tag `eda.nokia.com/node-profile=<name>` |
| NodeUser | Patch `nodeSelector` for NetBox-imported nodes ([§5.2](#52-eda-namespace--bootstrap-fabric-dc2)) |
| Verify | `kubectl get nodeprofiles,nodeusers,inits,ipallocationpools -n fabric-dc2` |

---

### 9.7 Topology path: NetBox DCIM (Mode B)

#### NetBox site

| Field | Value |
|-------|-------|
| Name | e.g. `fabric-dc2` |
| Status | `planned` or `active` |
| Tags | **No** `EDAManaged` |

#### Per SRL device

| Field | Required |
|-------|----------|
| Site | Your fabric site |
| Platform | **`srl`** |
| Device type | e.g. `7220 IXR-D2L` |
| Status | `planned` |

**Required device tags (`key=value`):**

```
eda.nokia.com/node-profile=fabric-dc2-srlinux-26.3.1
eda.nokia.com/role=leaf
eda.nokia.com/source=netbox
```

#### Interfaces and cables

- Interfaces on each device (e.g. `ethernet-1/49`, `ethernet-1/50`)
- Cables: DCIM → Cables → connect interface A ↔ B
- Optional cable tag: `eda.nokia.com/role=interSwitch`

#### ApplyTopology CR

**File: `applytopology-fabric-dc2.yaml`**

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyTopology
metadata:
  name: import-fabric-dc2
  namespace: fabric-dc2
spec:
  instanceName: netbox
  siteName: fabric-dc2
  deviceTags: []    # optional; empty = all devices in site
```

```bash
kubectl apply -f applytopology-fabric-dc2.yaml
kubectl get applytopology import-fabric-dc2 -n fabric-dc2 -o yaml
```

**Produces:** `TopoNode`, `Interface`, `TopoLink` in the workflow namespace.

> Default operation is **Reconcile** — orphans in the namespace are deleted. Use a **dedicated** namespace.

---

### 9.8 Allocation path: NetBox IPAM + EDA CRs

IPAM is **tag-scoped**, not site-scoped. Works with either topology mode.

#### NetBox IPAM objects

| Pool use | NetBox object | Status | Tag (`fabric-dc2`) |
|----------|---------------|--------|-------------------|
| System IPs | Prefix `10.0.1.0/24` | **Active** | `eda-fabric-dc2-systemip` |
| Mgmt IPs | Prefix `192.168.100.0/24` | **Active** | `eda-fabric-dc2-mgmt` |
| ISL subnets | Prefix `10.255.0.0/16` | **Container** | `eda-fabric-dc2-isl` |
| BGP ASNs | ASN Range | — | `eda-fabric-dc2-asn` |
| VLAN IDs | VLAN Group | — | `eda-fabric-dc2-vlan` |

Full per-pool NetBox UI steps: [§5.7](#57-netbox-allocation-pools-fabric-dc2).

Tags on IPAM objects are **plain strings** (not `key=value`).

#### Allocation CRs (one per pool)

**File: `allocations-fabric-dc2.yaml`** (multi-document — one `Allocation` per pool)

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-systemip
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-systemip]
  type: ip-address
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-mgmt
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-mgmt]
  type: ip-in-subnet
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-isl
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-isl]
  type: subnet
  subnetLength: 30
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-asn-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-asn]
  type: asn
---
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Allocation
metadata:
  name: nb-fabric-dc2-vlan-pool
  namespace: fabric-dc2
spec:
  enabled: true
  instance: netbox
  tags: [eda-fabric-dc2-vlan]
  type: vlan
```

```bash
kubectl apply -f allocations-fabric-dc2.yaml
kubectl get allocation -n fabric-dc2
```

#### ApplyAllocation CR (on-demand refresh)

**File: `applyallocation-refresh-fabric-dc2.yaml`**

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyAllocation
metadata:
  name: refresh-fabric-dc2-vlan
  namespace: fabric-dc2
spec:
  allocation: nb-fabric-dc2-vlan-pool
```

```bash
kubectl apply -f applyallocation-refresh-fabric-dc2.yaml
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools -n fabric-dc2
```

**Produces:** `IPAllocationPool`, `IPInSubnetAllocationPool`, `SubnetAllocationPool`, `IndexAllocationPool`.

**Verify:** `Allocation.status.matchedPrefixes` shows matched NetBox object IDs.

---

### 9.9 Mode comparison — what to enable

| Step | EDA-managed (clab) | NetBox-managed (fabric-dc2) |
|------|-------------------|----------------------------|
| EDA namespace | `clab-srl-leaf-spine-dcgw` | `fabric-dc2` (dedicated) |
| `Instance.sync.enabled` | **`true`** | **`false`** |
| `Instance.sync.region/tenant` | Set | N/A |
| NetBox webhook | Per namespace | Per namespace |
| NetBox DCIM modelling | EDA sync creates it | **You** create site/devices/cables |
| NetBox site `EDAManaged` | Yes (synced) | **No** |
| `ApplyTopology` | Not used | **Required** — `ApplyTopology` workflow CR |
| `Allocation` CRs | Optional | Optional |
| NetBox IPAM pools | Optional tagged pools | Optional tagged pools |
| NodeProfile / NodeUser / Init | In namespace | In namespace |

---

### 9.10 Recommended enable order

**Mode B (`fabric-dc2`):** follow [§5.1](#51-overview) build order — NetBox region/tenant/site/webhook/event rule ([§5.3](#53-netbox-prerequisites-fabric-dc2)) **before** EDA secrets ([§5.4](#54-secrets--instance-cr-fabric-dc2)); run `nb-test-fabric-dc2.py` ([§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables)) only after `Instance` is `reachable=true`; then [§5.6](#56-applytopology-cr); optional allocations [§5.7](#57-netbox-allocation-pools-fabric-dc2).

**Combined checklist (both modes):**

1. Install NetBox EDA app (if not present)
2. NetBox: Region, Tenant, catalog seed (Mode A — §4.1.1, §10.0; Mode B — verify catalog in [§5.3.1](#531-catalog-objects-verify--usually-already-seeded))
3. NetBox: **tags** — `EDAManaged` (optional, Mode A); allocation pool tags ([§5.3.3](#533-create-allocation-pool-tags-optional--before-57) / [§5.7](#57-netbox-allocation-pools-fabric-dc2)); device `key=value` tags (Mode B — [§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables))
4. NetBox: API token (with Extras Tag + Custom Field write); webhook + event rule per namespace ([§5.3](#53-netbox-prerequisites-fabric-dc2) for Mode B); `ENFORCE_GLOBAL_UNIQUE=false`
5. EDA: namespace + **namespace bootstrap** ([§5.2](#52-eda-namespace--bootstrap-fabric-dc2) / §3.2)
6. EDA: secrets + **`Instance` CR** → verify `status.reachable: true` ([§4.4](#44-netbox-instance-cr-mode-a) Mode A, [§5.4](#54-secrets--instance-cr-fabric-dc2) Mode B)
7. EDA: **`Allocation`** CRs (pool tags must already exist on NetBox IPAM)
8. NetBox: DCIM site/devices/interfaces/cables (**Mode B only** — [§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables))
9. EDA: **`ApplyTopology`** ([§5.6](#56-applytopology-cr), Mode B) or let sync run (Mode A — [§10.8.1.5](#10815-verify-sync-in-netbox))
10. EDA: **`ApplyAllocation`** if pools did not reconcile via webhook

---

### 9.11 Verify (read-only)

```bash
kubectl get instance,allocation,applytopology -n fabric-dc2
kubectl get nodeprofiles,nodeusers,inits -n fabric-dc2
kubectl get toponodes,topolinks,interfaces -n fabric-dc2
kubectl get ipallocationpools,subnetallocationpools,indexallocationpools -n fabric-dc2
```

NetBox UI: filter by `EDAManaged` — expect on synced DCIM (Mode A) and consumed IPAM allocations; **not** on your design site/devices (Mode B).

---

## 10. Implementation procedures

| Mode | Use sections |
|------|--------------|
| **A — EDA-managed (sync on)** | [9.0](#100-procedure--seed-netbox-catalog-for-eda-sync-mode-a) → [9.2](#92-procedure--enable-netbox-integration) → verify sync; skip 9.4–9.6 |
| **B — NetBox-managed (import)** | [9.1](#91-procedure--create-and-bootstrap-eda-namespace) → 9.2–9.6 |

### 10.0 Procedure — seed NetBox catalog for EDA sync (Mode A)

Run on the Containerlab host **before** applying `Instance` with `sync.enabled: true`. This prepares NetBox so EDA can push `TopoNode` objects as Devices.

#### What the Django shell command does

Pipe the Python seed script into `manage.py shell` on the NetBox deployment. **No `kubectl cp`, no `jsonpath`, no nested `bash -c` quotes** — those break when copied from Word/PDF/browser (smart quotes, merged lines).

**Recommended (WSL)** — two lines, paste into bash:

```bash
SCRIPT=./manifests/nb-seed-eda-catalog.py
kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell < "$SCRIPT"
```

**Or one line** — wrapper script (same logic; easiest for teams):

```bash
bash ./manifests/nb-run-seed-catalog.sh
```

`manage.py shell` starts an embedded **Django ORM** session inside the NetBox pod — the same database layer the UI and REST API use. `-i` streams your local script file into the pod; `-c netbox` targets the main container (not `init-dirs`). Smaller scripts may use `kubectl cp` + `exec(open(...))`; the catalog seed should use stdin as above.

| Import | Django model | Purpose in this script |
|--------|--------------|------------------------|
| `Manufacturer` | `dcim.Manufacturer` | Vendor record DeviceTypes hang off (e.g. Nokia) |
| `DeviceType` | `dcim.DeviceType` | Hardware SKU; **`model` must match `TopoNode.spec.platform`** |
| `CustomField` | `extras.CustomField` | **Read-only check** — `eda_managed` is created by EDA on first sync, not by you |
| `Platform` | `dcim.Platform` | OS family (`srl`, `sros`) — used for display and Mode B import rules |
| `DeviceRole` | `dcim.DeviceRole` | leaf / spine / pe — mapped from EDA node labels |
| `Region` | `dcim.Region` | Must match `Instance.spec.sync.region` |
| `Tenant` | `tenancy.Tenant` | Must match `Instance.spec.sync.tenant` |

The script uses `get_or_create()` so it is **idempotent** — safe to re-run after adding new hardware to the clab topology.

#### Script source

Full source: [Appendix E.1](#e1-nb-seed-eda-catalogpy-mode-a). Use `scripts/nb-seed-eda-catalog.py`. Adjust `FABRIC_TENANCY`, `DEVICE_TYPES`, and `ROLES` for your fabrics before running.

**Catalog scope:** Seeds **36** device types by default (6 lab + 30 extended Nokia SKUs). Set `DEVICE_TYPES = LAB_DEVICE_TYPES` in the script for lab-only. Full model/u_height list in [§4.1.1](#411-mode-a--netbox-catalog-prerequisites-before-sync).

**What this adds:** Region/Tenant pairs per fabric, Manufacturer, `DeviceType` per platform, `Platform`, and `DeviceRole` entries. It does **not** create Sites, Devices, or Cables — EDA does that on sync.

#### Step-by-step

| Step | Where | Action |
|------|--------|--------|
| 1 | NetBox | Ensure Region/Tenant pairs exist for each fabric (`region-1`/`tenant-a`, `region-2`/`tenant-b`, …) — catalog script seeds these |
| 2 | NetBox | Run catalog seed script (Manufacturer, DeviceTypes, Platforms, Roles) |
| 3 | EDA | Namespace + Containerlab fabric — `TopoNode`/`TopoLink` CRs must already exist |
| 4 | EDA | Apply `Instance` with `sync.enabled: true`, `region`, `tenant` |
| 5 | NetBox | API token with DCIM **write**, webhook + event rules (Section 9.2) |
| 6 | Both | Verify `Instance.status.reachable: true`; Devices appear under synced Site with `EDAManaged` |
| 7 | NetBox (optional) | Run `nb-fix-platforms.py` if platforms or `u_height` need correction after first sync |

**Copy and run (WSL)** — paste into a **bash** shell (WSL/Containerlab host). Use straight ASCII quotes only (not Word “smart quotes”):

```bash
SCRIPT=./manifests/nb-seed-eda-catalog.py
kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell < "$SCRIPT"
```

**Copy and run (PowerShell)** — pipe file contents (no `<` redirect in PowerShell):

```powershell
$SCRIPT = "$env:LOCALAPPDATA\Temp\nb-seed-eda-catalog.py"
Get-Content -Raw $SCRIPT | kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell
```

> **Copy-paste pitfalls:** (1) Pasting into **PowerShell** instead of WSL bash — use the PowerShell block above. (2) **Smart/curly quotes** from Word or PDF break shell parsing; copy from plain Markdown or Cursor, or use the wrapper script. (3) **All lines merged into one** — run: `bash ./manifests/nb-run-seed-catalog.sh`. (4) `ImportError: Region from tenancy.models` — use the script with `Region` imported from `dcim.models` (NetBox 4.x).

**Verify in NetBox UI:** DCIM → Manufacturers, Device Types, Platforms; Tenancy → Regions/Tenants.

**Do not:** manually create Devices in the EDAManaged site expecting them to appear in EDA — sync does not flow NetBox → EDA when `sync.enabled: true`.

---

### 10.1 Procedure — create and bootstrap EDA namespace

Full detail: [§5.2](#52-eda-namespace--bootstrap-fabric-dc2).

```bash
kubectl apply -f eda-namespace-fabric-dc2.yaml
kubectl get nodeprofiles,nodeusers,inits,ipallocationpools -n fabric-dc2
```

**Or `edactl`:**

```bash
kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl namespace bootstrap create --from-namespace eda fabric-dc2

kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl -n fabric-dc2 namespace bootstrap list
```

Use `--from-namespace clab-3-tier-leaf-spine-dcgw` to match clab NodeProfile names. **Do not** use `make edactl` from the playground Makefile.

**Post-bootstrap for NetBox import:**

| Check | Action |
|-------|--------|
| NodeProfile name | Record name; use in NetBox `eda.nokia.com/node-profile=<name>` on every SRL device |
| NodeUser `nodeSelector` | Patch if template selects clab labels — add `eda.nokia.com/source=netbox` (or your label) |
| Init `nodeSelectors` | Same as NodeUser if nodes will onboard |
| Design-only | No change needed until TopoNodes exist; use `npp.mode: emulate` if interfaces fail |

### 10.2 Procedure — enable NetBox integration

1. Create secrets — **File: `secrets-<namespace>.yaml`** (see [§9.1](#91-kubernetes-secrets-per-eda-namespace)); `kubectl apply -f secrets-<namespace>.yaml`
2. Apply **Instance** CR — **File: `instance-<namespace>.yaml`** (see [§9.2](#92-instance-cr-required-one-per-namespace)); `kubectl apply -f instance-<namespace>.yaml`
3. Configure NetBox webhook and event rule (URL includes namespace name) — [§9.3](#93-netbox-webhook-one-per-instance), [§9.4](#94-netbox-event-rule)
4. Verify `Instance.status.reachable: true`

### 10.3 Procedure — configure allocation pools (optional)

1. Create tagged IPAM objects in NetBox (prefixes, VLAN groups, ASN ranges).
2. Apply **`allocations-<namespace>.yaml`** in same namespace as `Instance` — see [§9.8](#98-allocation-path-netbox-ipam--eda-crs).
3. Run **`applyallocation-*.yaml`** or wait for webhook reconcile.
4. Verify EDA pool CRs and `Allocation.status.matchedPrefixes`.

### 10.4 Procedure — model fabric in NetBox (DCIM)

| Step | Action |
|------|--------|
| 1 | Create site (no `EDAManaged`) |
| 2 | Create devices: `platform=srl`, tags `eda.nokia.com/node-profile=...`, role, source |
| 3 | Create interfaces on each device |
| 4 | Create cables between interfaces |

### 10.5 Procedure — import topology to EDA

**File: `applytopology-fabric-dc2.yaml`**

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyTopology
metadata:
  name: import-fabric-dc2
  namespace: fabric-dc2
spec:
  instanceName: netbox
  siteName: fabric-dc2
  deviceTags: []
```

```bash
kubectl apply -f applytopology-fabric-dc2.yaml
```

**Verify:**

```bash
kubectl get toponodes,topolinks,interfaces -n fabric-dc2
kubectl get applytopology import-fabric-dc2 -n fabric-dc2 -o yaml
```

### 10.6 Procedure — design-only / planned nodes

| State | TopoNode settings |
|-------|-------------------|
| Design only | `onBoarded: false`, `npp.mode: emulate` |
| Live / onboarded | `productionAddress` set, `onBoarded: true`, `npp.mode: normal` |

NetBox site `status: planned` → `active` is updated manually in NetBox.

### 10.7 Implementation checklist

**Mode A (EDA SOT / sync):** NetBox catalog seed (9.0) → EDA namespace + TopoNodes → secrets + Instance (`sync.enabled: true`) → webhook → verify EDAManaged devices in NetBox.

**Mode B (NetBox import):**

**EDA (before NetBox):** namespace, bootstrap, NodeProfile/NodeUser/Init, secrets, Instance, webhook, optional Allocation CRs.

**NetBox DCIM:** site, devices, interfaces, cables.

**NetBox IPAM (optional):** prefixes, VLAN groups, ASN ranges with matching tags.

**EDA (import):** ApplyAllocation (if needed), ApplyTopology, verify TopoNodes and pools.

**Ongoing:** use Create workflow or transaction `create` for incremental adds — never reconcile into a shared namespace.

---

### 10.8 Manual test guide (with example CRs and scripts)

Hands-on validation for the lab. **Run commands yourself** — copy/paste each block in order. Replace `NODE_PROFILE`, tokens, and webhook host for your environment.

| Manual test (§10.8) | Configuration reference (§9) |
|--------------------|-----------------------------------|
| §10.8.1.2 Seed catalog | [§10.0](#100-procedure--seed-netbox-catalog-for-eda-sync-mode-a) |
| §10.8.1.3 Secrets + Instance | [§4.4](#44-netbox-instance-cr-mode-a) |
| §10.8.1.4 Webhook + event rule | [§9.3](#93-netbox-webhook-one-per-instance), [§9.4](#94-netbox-event-rule) |
| §10.8.2.1 Namespace + bootstrap | [§9.6](#96-eda-namespace-prerequisites-onboarding), [§10.1](#101-procedure--create-and-bootstrap-eda-namespace) |
| §10.8.2.2 NetBox prerequisites | [§5.3](#53-netbox-prerequisites-fabric-dc2) |
| §10.8.2.3 Secrets + Instance | [§5.4](#54-secrets--instance-cr-fabric-dc2) |
| §10.8.2.5 ApplyTopology | [§5.6](#56-applytopology-cr), [§9.7](#97-topology-path-netbox-dcim-mode-b) |
| §10.8.3.2–3.3 Allocations | [§6](#6-allocations--ipam-pools), [§9.8](#98-allocation-path-netbox-ipam--eda-crs), [§10.3](#103-procedure--configure-allocation-pools-optional) |

#### Lab URLs (important — three different addresses)

| Who is calling | URL | Why |
|----------------|-----|-----|
| **Your browser** (EDA UI, Cursor EDA Explorer, REST from laptop) | **https://localhost:9443** | KIND maps the `eda-api` LoadBalancer to your host. **Do not** use the KIND node IP (e.g. `192.168.221.33`) in the browser — that is the cluster node, not your port-forward. |
| **NetBox UI** | **http://localhost:8081** | Same pattern — host port-map to the NetBox Service. |
| **EDA controller → NetBox** (`Instance.spec.url`) | `http://netbox.netbox.svc.cluster.local:80` | Pod-to-pod DNS inside the cluster. EDA reads/writes NetBox here. |
| **NetBox → EDA** (webhook URL in NetBox UI) | `https://<EDA-WEBHOOK-HOST>:443/...` | NetBox pod must reach EDA. **Do not** use `localhost` — from inside NetBox, `localhost` is the NetBox pod itself. |

**Find your webhook host** (run once; use the result in NetBox webhook URL):

```bash
# In-cluster hostname (preferred if NetBox can resolve cluster DNS):
echo "https://eda-api.eda-system.svc.cluster.local:443/core/httpproxy/v1/netbox/webhook/<NAMESPACE>/netbox"

# Or LoadBalancer IP (lab example):
kubectl get svc eda-api -n eda-system -o jsonpath='LB IP={.status.loadBalancer.ingress[0].ip}{"\n"}'
# Example output: 172.18.255.2 → webhook base https://172.18.255.2:443/...
```

| Command | What it does |
|---------|--------------|
| `kubectl get svc eda-api -n eda-system` | Shows how EDA API is exposed — `LoadBalancer` with external IP and ports 80/443 |
| `jsonpath='{.status.loadBalancer.ingress[0].ip}'` | Prints the IP other pods can use to reach EDA API (webhook host candidate) |

**Namespaces:** Mode A `clab-srl-leaf-spine-dcgw` · Mode B `fabric-dc2`

**Script paths (Windows → WSL):** `./manifests/<script>`

#### Helper — run any NetBox Python script

**WSL (one line at a time):**

```bash
NS=netbox
POD=$(kubectl get pods -n "$NS" -l "app.kubernetes.io/name=netbox" -o jsonpath='{.items[0].metadata.name}')
echo "Using pod: $POD"
kubectl cp ./manifests/<script>.py "${NS}/${POD}:/tmp/<script>.py"
kubectl exec -n "$NS" "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/<script>.py').read())"
```

| Command | What it does |
|---------|--------------|
| `POD=$(kubectl get pod ...)` | Finds the running NetBox pod name and stores it in `$POD` |
| `kubectl cp ...` | Copies your script from the WSL filesystem into the pod at `/tmp/` |
| `kubectl exec ... manage.py shell -c "exec(open(...))"` | Runs Django ORM Python **inside** NetBox — same DB as the UI; creates/reads objects directly |

---

#### 10.8.0 Prerequisites

| Step | Command | What it does |
|------|---------|--------------|
| 0.1 | `kubectl get nodes` | Confirms the Kubernetes cluster (KIND) is up and nodes are Ready |
| 0.2 | `kubectl get pods -n netbox` | Confirms the NetBox Helm deployment is running |
| 0.3 | Open http://localhost:8081 and https://localhost:9443 | Browser check — both UIs load |
| 0.4 | `kubectl get nodeprofiles -n clab-srl-leaf-spine-dcgw` | Lists EDA NodeProfile CRs; note the name for device tags later |

---

#### 10.8.1 Mode A — EDA → NetBox sync

*EDA owns the live fabric; NetBox mirrors it.*

##### 10.8.1.1 Confirm EDA fabric exists

```bash
kubectl get toponodes -n clab-srl-leaf-spine-dcgw
kubectl get topolinks -n clab-srl-leaf-spine-dcgw --no-headers | wc -l
```

| Command | What it does |
|---------|--------------|
| `kubectl get toponodes` | Lists EDA topology nodes (switches) in the clab namespace — your Containerlab fabric |
| `kubectl get topolinks ... \| wc -l` | Counts inter-switch links; confirms topology is not empty |

**Pass:** Non-zero TopoNodes.

##### 10.8.1.2 Seed NetBox catalog

**Full script:** [Appendix E.1](#e1-nb-seed-eda-catalogpy-mode-a) — use `scripts/nb-seed-eda-catalog.py`. Review `FABRIC_TENANCY`, `DEVICE_TYPES`, and `ROLES` before running.

**Then run (WSL):**

```bash
SCRIPT=./manifests/nb-seed-eda-catalog.py
kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell < "$SCRIPT"
```

**Pass:** NetBox UI → DCIM → Manufacturers / Device Types / Platforms; Tenancy → Regions / Tenants. Expect `Catalog seed complete (36 device types)`. `eda_managed` / `EDAManaged` still absent until first sync (expected).

##### 10.8.1.3 Secrets + NetBox Instance CR

Use the YAML files in [§4.4](#44-netbox-instance-cr-mode-a) (baseline: `clab-3-tier-leaf-spine-dcgw`). Lab copies:

```bash
kubectl apply -f ./manifests/secrets-clab-3-tier-leaf-spine-dcgw.yaml
kubectl apply -f ./manifests/instance-clab-3-tier-leaf-spine-dcgw.yaml
kubectl get instance.netbox.eda.nokia.com netbox -n clab-3-tier-leaf-spine-dcgw -o jsonpath='reachable={.status.reachable}{"\n"}'
```

**Pass:** `reachable=true`

##### 10.8.1.4 NetBox webhook + event rule (UI)

Configure in NetBox → **Operations → Integrations**:

| Field | Value | What it does |
|-------|-------|--------------|
| Webhook URL | `https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-3-tier-leaf-spine-dcgw/netbox` | When NetBox objects change, NetBox POSTs to EDA's NetBox proxy |
| Secret | Same plaintext as `signatureKey` secret | HMAC validation so EDA trusts the caller |
| Event rule objects | DCIM: Device, Device Type, Site, Cable (+ IPAM if using allocations) | Limits which changes trigger webhooks |

##### 10.8.1.5 Verify sync in NetBox

```bash
kubectl get toponodes -n clab-3-tier-leaf-spine-dcgw --no-headers | wc -l
```

Compare that count to NetBox UI → **DCIM → Devices** filtered by tag **`EDAManaged`**.

**Pass:** Device names match EDA; synced site exists; `eda_managed` custom field populated.

##### 10.8.1.6 Optional post-sync fix

**Script `nb-fix-platforms.py`:** Full source [Appendix E.4](#e4-nb-fix-platformspy). Sets Platform `srl` or `sros` on devices; fixes `7750 SR-1` rack height.

```bash
kubectl cp ./manifests/nb-fix-platforms.py "netbox/${POD}:/tmp/nb-fix-platforms.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-fix-platforms.py').read())"
```

##### 10.8.1.7 Negative test

1. **NetBox UI:** Add device `test-manual-leaf` to the EDAManaged clab site.
2. Wait ~60s, then:

```bash
kubectl get toponodes -n clab-3-tier-leaf-spine-dcgw | grep test-manual-leaf || echo "PASS: no TopoNode created"
```

**What this proves:** With `sync.enabled: true`, direction is EDA → NetBox only. NetBox manual devices do not become TopoNodes.

---

#### 10.8.2 Mode B — NetBox → EDA import

*NetBox is design source. Use dedicated namespace `fabric-dc2` — never reconcile into clab.*

##### 10.8.2.1 Create namespace + bootstrap

Full procedure: [§5.2](#52-eda-namespace--bootstrap-fabric-dc2).

**Recommended — `eda-namespace-fabric-dc2.yaml`:**

```yaml
apiVersion: core.eda.nokia.com/v1
kind: Namespace
metadata:
  name: fabric-dc2
  namespace: eda-system
spec:
  bootstrap:
    fromNamespace: eda
```

**If namespace exists but bootstrap CRs are empty — `edactl`:**

```bash
kubectl exec -n eda-system deploy/eda-toolbox -- \
  edactl namespace bootstrap create --from-namespace eda fabric-dc2
```

##### 10.8.2.2 NetBox prerequisites

Full procedure: [§5.3](#53-netbox-prerequisites-fabric-dc2). **Create directly in NetBox UI** (`http://localhost:8081`) before EDA secrets:

| Step | NetBox UI | Lab value |
|------|-----------|-----------|
| Region / Tenant | Tenancy → Regions / Tenants | `region-3` / `tenant-c` |
| Site | DCIM → Sites → Add | `fabric-dc2`, planned, **no** `EDAManaged` |
| Webhook | Operations → Integrations → Webhooks | URL `.../webhook/fabric-dc2/netbox`, **new** secret |
| Event rule | Operations → Integrations → Event Rules | Points to `fabric-dc2` webhook |

Reuse Mode A API token. Copy webhook **Secret** for `secrets-fabric-dc2.yaml`.

##### 10.8.2.3 Secrets + Instance CR (sync off)

**File: `secrets-fabric-dc2.yaml`** — same structure as §10.8.1.3; namespace `fabric-dc2` (see [§9.1](#91-kubernetes-secrets-per-eda-namespace)).

```bash
kubectl apply -f secrets-fabric-dc2.yaml
```

**Instance CR** — `sync.enabled: false` means EDA does **not** push topology to NetBox; you import with `ApplyTopology`.

**File: `instance-fabric-dc2.yaml`**

```yaml
# Mode B — NetBox design source. sync.enabled: false
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: Instance
metadata:
  name: netbox
  namespace: fabric-dc2
spec:
  url: http://netbox.netbox.svc.cluster.local:80
  apiToken: netbox-api-token
  signatureKey: netbox-webhook-signature
  sync:
    enabled: false
```

```bash
kubectl apply -f instance-fabric-dc2.yaml
kubectl get instance netbox -n fabric-dc2 -o jsonpath='reachable={.status.reachable}{"\n"}'
```

**Pass:** `reachable=true` (requires webhook + token from [§5.3](#53-netbox-prerequisites-fabric-dc2) / §10.8.2.2).

##### 10.8.2.4 Model fabric in NetBox

Full procedure: [§5.5](#55-netbox-dcim-modelling--devices-interfaces-cables). Save [Appendix E.2](#e2-nb-test-fabric-dc2py-mode-b) (edit `NODE_PROFILE`), then run:

```bash
SCRIPT=./manifests/nb-test-fabric-dc2.py
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-fabric-dc2.py').read())"
```

**Pass:** 6 devices + 8 cables at site `fabric-dc2`; no `EDAManaged`.

##### 10.8.2.5 ApplyTopology CR

**What ApplyTopology does:** Reads the named NetBox site, fetches devices (platform `srl`) + cables, and creates/updates `TopoNode`, `Interface`, `TopoLink` CRs in the workflow namespace. Default workflow operation is **Reconcile** — orphans in that namespace not in the site spec are **deleted**.

**File: `applytopology-fabric-dc2.yaml`**

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyTopology
metadata:
  name: import-fabric-dc2
  namespace: fabric-dc2
spec:
  instanceName: netbox      # Instance CR in same namespace
  siteName: fabric-dc2      # NetBox site to read
  deviceTags: []            # empty = all devices in site
```

```bash
kubectl apply -f applytopology-fabric-dc2.yaml
kubectl get applytopology import-fabric-dc2 -n fabric-dc2 -w
```

| Command | What it does |
|---------|--------------|
| `kubectl apply -f applytopology-...` | Submits the import workflow to EDA |
| `kubectl get applytopology ... -w` | Watches workflow status until complete |

##### 10.8.2.6 Verify in EDA

```bash
kubectl get toponodes -n fabric-dc2
kubectl get toponodes leaf-dc2-01 -n fabric-dc2 -o yaml | grep -E 'nodeProfile|onBoarded|netbox.device'
kubectl get topolinks,interfaces -n fabric-dc2
```

| Command | What it does |
|---------|--------------|
| `get toponodes` | Lists imported nodes — should show `leaf-dc2-01` … `leaf-dc2-04`, `spine-dc2-01`, `spine-dc2-02` (6 total) |
| `grep nodeProfile\|onBoarded\|netbox.device` | Confirms NodeProfile binding, planned state, and back-reference to NetBox device ID |
| `get topolinks,interfaces` | Shows imported cable as TopoLink + Interface CRs |

**Pass:** `onBoarded: false` for planned design; `eda.nokia.com/netbox.device.id` label present.

##### 10.8.2.7 Confirm clab untouched

```bash
kubectl get toponodes -n clab-srl-leaf-spine-dcgw --no-headers | wc -l
```

**Pass:** Same count as before §10.8.2.

---

#### 10.8.3 Test allocations (optional)

*IPAM pools — independent of DCIM site. Full examples for all five pool types: [§5.7](#57-netbox-allocation-pools-fabric-dc2).*

##### 10.8.3.1 Create all NetBox IPAM pools (Mode B — `fabric-dc2`)

**Script `nb-test-allocation-pools-fabric-dc2.py`** creates VLAN group, ASN range, and three prefixes with namespace-scoped tags (`eda-fabric-dc2-*`). Source: [Appendix E.3](#e3-nb-test-allocation-pools-fabric-dc2py).

```bash
SCRIPT=./scripts/nb-test-allocation-pools-fabric-dc2.py
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-fabric-dc2.py').read())"
```

**Or create manually in NetBox UI** — see [§5.7.1](#571-vlan-pool-type-vlan) through [§5.7.5](#575-isl-subnet-pool-type-subnet).

##### 10.8.3.1b Mode A clab allocations (`clab-3-tier-leaf-spine-dcgw`)

Mode A namespaces need their **own** tagged IPAM pools and `Allocation` CRs (bootstrap pools from `edactl` are EDA-native, not NetBox-backed).

**Script:** `nb-test-allocation-pools-clab3tier.py` — tags `eda-clab3tier-*`, pools non-overlapping with `fabric-dc2` (e.g. VLAN 300–399, ASN `4200010000–4200010999`). Source: [Appendix E.8](#e8-nb-test-allocation-pools-clab3tierpy).

```bash
SCRIPT=./scripts/nb-test-allocation-pools-clab3tier.py
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-allocation-pools-clab3tier.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-clab3tier.py').read())"
kubectl apply -f allocations-clab-3-tier-leaf-spine-dcgw.yaml
```

**Pass:** `kubectl get allocation -n clab-3-tier-leaf-spine-dcgw` — all five show matched status (including ASN, because `sync.enabled: true`).

**Both namespaces at once:** `bash setup-allocations-both-namespaces.sh` · verify: `bash verify-allocations-both.sh`

##### 10.8.3.2 Apply Allocation CRs (all five pools)

**File: `allocations-fabric-dc2.yaml`** — see [§9.8](#98-allocation-path-netbox-ipam--eda-crs) or [§6.3](#63-allocation-cr--all-pool-types).

```bash
kubectl apply -f allocations-fabric-dc2.yaml
kubectl get allocation -n fabric-dc2
```

| Allocation CR | `spec.type` | Tag on NetBox object |
|---------------|-------------|----------------------|
| `nb-fabric-dc2-vlan-pool` | `vlan` | `eda-fabric-dc2-vlan` |
| `nb-fabric-dc2-asn-pool` | `asn` | `eda-fabric-dc2-asn` |
| `nb-fabric-dc2-systemip` | `ip-address` | `eda-fabric-dc2-systemip` |
| `nb-fabric-dc2-mgmt` | `ip-in-subnet` | `eda-fabric-dc2-mgmt` |
| `nb-fabric-dc2-isl` | `subnet` | `eda-fabric-dc2-isl` |

##### 10.8.3.3 ApplyAllocation (if webhook missed reconcile)

```yaml
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyAllocation
metadata:
  name: refresh-fabric-dc2-vlan
  namespace: fabric-dc2
spec:
  allocation: nb-fabric-dc2-vlan-pool
```

Repeat with each Allocation name (`nb-fabric-dc2-asn-pool`, `nb-fabric-dc2-systemip`, …) or rely on webhook after NetBox edits.

```bash
kubectl apply -f applyallocation-refresh-fabric-dc2.yaml
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n fabric-dc2
```

**Pass:** Each `Allocation` `status` shows matched NetBox objects; corresponding EDA pool CRDs exist in `fabric-dc2`.

---

#### 10.8.4 Pass/fail checklist

| # | Test | Pass |
|---|------|------|
| 1 | Mode A sync | NetBox `EDAManaged` devices match clab TopoNodes |
| 2 | Mode A negative | No TopoNode for manually added NetBox device |
| 3 | Mode B import | 6 TopoNodes + 8 TopoLinks in `kubectl get toponodes,topolinks -n fabric-dc2` |
| 4 | Isolation | clab TopoNode count unchanged |
| 5 | Allocations | `Allocation.status` matched + `IndexAllocationPool` exists |
| 6 | Health | Both Instances `reachable: true` |

**Summary script `test-verify-integration.sh` does:** Runs kubectl checks for Parts 0–3 (node/pod health, Instance reachability, TopoNode counts, Allocation status) and prints a quick pass/fail overview.

```bash
bash ./manifests/test-verify-integration.sh
```

#### Test script inventory

| Script | What it does |
|--------|--------------|
| `nb-seed-eda-catalog.py` | Mode A: Region, Tenant, Manufacturer, DeviceTypes, Platforms, Roles |
| `nb-fix-platforms.py` | Mode A post-sync: assign `srl`/`sros` platform; fix SR-1 rack height |
| `nb-test-fabric-dc2.py` | Mode B: site + leaf + spine + ISL cable with import tags |
| `nb-test-allocation-pools-fabric-dc2.py` | All 5 IPAM pools + tags for Allocation CRs |
| `test-verify-integration.sh` | Read-only kubectl summary after all parts |

---

## 11. EDA transactions

Individual CR changes use EDA **transactions** (atomic, Git-backed). Distinct from `ApplyTopology` workflow ops (`create` / `reconcile` / `replace`).

### 11.1 Per-resource operation types

| Op | Resource exists | Resource missing | Behaviour |
|----|-----------------|------------------|-----------|
| **create** | Fails | Creates | Strict create only |
| **modify** | Updates | Fails | In-place update |
| **replace** | Full overwrite | Creates (upsert) | Whole resource replaced |
| **patch** | Field update | Fails | JSON Patch (RFC 6902) |
| **delete** | Deletes | Fails | Remove by GVK + name + namespace |

### 11.2 Rule of thumb (NetBox-imported fabric)

| Goal | Use |
|------|-----|
| Patch TopoNode label or `npp.mode` | `modify` or `patch` |
| Redefine whole TopoNode | `replace` |
| Add TopoLink without reconcile | transaction `create` or `kubectl apply` |
| Add device from NetBox | `ApplyTopology` with **Create** workflow |
| Remove one resource | `delete` |

### 11.3 Transaction vs topology import

| Mechanism | Orphans in namespace |
|-----------|----------------------|
| Transaction ops on named CRs | Untouched |
| `ApplyTopology` reconcile | **Deleted** if not in site spec |
| `NetworkTopology` `operation: create` | Untouched |

### 11.4 Execution and inspection

- **dryRun:** validate without pushing to nodes
- **detailLevel:** `basic` | `standard` | `detailed`
- **CLI:** `edactl apply|replace|patch|delete -f ... -d -m "message"`
- **Inspect:** `edactl transaction <id> cr-change|node-change`

See [EDA transactions documentation](https://docs.eda.dev/latest/user-guide/transactions/) for full API and rollback (Revert / Restore).

---

## 12. Constraints and anti-patterns

| Mistake | Consequence |
|---------|-------------|
| One namespace, clab + NetBox planned | `ApplyTopology` **Reconcile** removes TopoNodes not in the NetBox site — live fabric nodes in that namespace are deleted |
| `sync.enabled: true` on NetBox-design namespace | EDA overwrites your DCIM |
| `ApplyTopology` on EDAManaged site | Conflict / workflow failure |
| Same IPAM tag on pools for two namespaces | Wrong pool matched / shared consumption |
| Stale API token secret | Empty `Allocation.status`; pools never appear |
| `ENFORCE_GLOBAL_UNIQUE=true` with overlapping topologies | Duplicate IP allocation failures |

---

## 13. Appendices

### Appendix A — Naming conventions (production)

| Demo (avoid) | Production |
|--------------|------------|
| Site `nb-planned-fabric` | `fabric-dc2`, `pop-london-01` |
| Device `srl-leaf-planned-01` | `leaf-dc2-01` |
| Tag `netbox-planned=true` | `eda.nokia.com/source=netbox` |

### Appendix B — Django ORM scripts (lab)

Bulk NetBox DCIM modelling used **Django ORM inside the NetBox pod** (`manage.py shell`).

### How to run

```bash
# From WSL (Containerlab host) — copy script into pod, exec via manage.py shell
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp /path/to/script.py "netbox/${POD}:/tmp/script.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/script.py').read())"
```

**Windows temp path (lab):** `./manifests/<script>.py`

### Script inventory

| Script | Purpose | Scope |
|--------|---------|-------|
| `nb-planned-fabric-full.py` | Create 4 leaves + 2 spines, interfaces, 8 ISL cables | Site `nb-planned-fabric` |
| `nb-seed-eda-catalog.py` | Seed Manufacturer, DeviceTypes, Platforms, Roles, Region/Tenant before Mode A sync | NetBox global catalog |
| `nb-test-fabric-dc2.py` | Mode B: 4× D3L leaf + 2× D4 spine, interfaces, 8 ISL cables | Site `fabric-dc2` |
| `nb-test-allocation-pools-fabric-dc2.py` | All 5 IPAM pools + tags for `fabric-dc2` Allocation CRs | IPAM |
| `nb-test-vlan-pool.py` | Legacy — VLAN only; use `nb-test-allocation-pools-fabric-dc2.py` | IPAM |
| `test-verify-integration.sh` | kubectl pass/fail summary after manual test (§9.8) | Read-only |
| `nb-fix-platforms.py` | Post-sync: set `srl`/`sros` platforms; fix SR-1 `u_height` | All devices |
| `nb-delete-planned-fabric.py` | Delete cables then devices (interfaces cascade) | Site `nb-planned-fabric`, name prefix `srl-*-planned-*` |
| `nb-create-planned-site.py` | Create site + single leaf (minimal example) | Site `nb-planned-fabric` |
| `nb-list-devices.py` | List `srl-*` devices; flag duplicate names across sites | Read-only audit |
| `nb-audit-devices.py` | Platform / device-type audit | Read-only |
| `run-nb-delete-planned.sh` | Wrapper: copy + exec delete script | NetBox only |
| `run-planned-fabric-full.sh` | NetBox create + EDA YAML apply (demo) | NetBox + EDA |
| `run-delete-planned-all.sh` | Delete EDA planned CRs + NetBox ORM delete | EDA + NetBox |

> **Production:** replace `nb-planned-fabric` / `*-planned-*` naming with real site/device names (`fabric-dc2`, `leaf-dc2-01`). Use `eda.nokia.com/source=netbox` instead of `netbox-planned=true`. See [Naming conventions](#naming-for-production).

### ORM patterns used

| Operation | Django ORM |
|-----------|------------|
| Idempotent device | `Device.objects.filter(name=..., site=site).first()` then create or update |
| `key=value` tags | `Tag.objects.get_or_create(name=kv, ...)` — NetBox stores full `eda.nokia.com/node-profile=...` as tag **name** |
| Interfaces | `Interface.objects.get_or_create(device=dev, name=...)` |
| Cables | `Cable.objects.create(...)` + two `CableTermination` rows (GenericForeignKey to Interface) |
| Safe delete | Resolve interface IDs → `CableTermination` → cable IDs → delete cables **before** devices |
| Site scope | Always filter `Device.objects.filter(site=site)` — duplicate device names across sites are possible |

**Delete order:** cables → devices (interfaces delete with device).

---

### `nb-seed-eda-catalog.py` — catalog before EDA sync (Mode A)

Idempotent seed for Region, Tenant, Manufacturer, DeviceTypes (matching `TopoNode.spec.platform`), Platforms, and DeviceRoles. **Review and edit before running** — full source in [Appendix E.1](#e1-nb-seed-eda-catalogpy-mode-a).

**Catalog scope:** Seeds **36** device types by default (6 lab + 30 extended Nokia SKUs). Set `DEVICE_TYPES = LAB_DEVICE_TYPES` in the script for lab-only. Full model/u_height list in [§4.1.1](#411-mode-a--netbox-catalog-prerequisites-before-sync).

```python
DEVICE_TYPES = LAB_DEVICE_TYPES + EXTENDED_DEVICE_TYPES
ROLES = ["leaf", "spine", "pe", "dcgw", "border-leaf"]
```

**Run (WSL)** — see [Section 10.0](#100-procedure--seed-netbox-catalog-for-eda-sync-mode-a):

```bash
SCRIPT=./manifests/nb-seed-eda-catalog.py
kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell < "$SCRIPT"
```

Wrapper: `bash ./manifests/nb-run-seed-catalog.sh`

---

### `nb-planned-fabric-full.py` — create fabric in NetBox

Creates 4 leaf + 2 spine devices at legacy site `nb-planned-fabric`. **Full source:** [Appendix E.5](#e5-nb-planned-fabric-fullpy-legacy-lab-site). For Mode B production lab use [E.2](#e2-nb-test-fabric-dc2py-mode-b) (`fabric-dc2`).

**Run:**

```bash
bash ./manifests/run-nb-delete-planned.sh   # optional clean first
# or copy + exec nb-planned-fabric-full.py directly (see How to run above)
```

---

### `nb-delete-planned-fabric.py` — scoped delete

Deletes only devices matching name prefixes in site `nb-planned-fabric`. Does **not** touch EDAManaged clab site objects. **Full source:** [Appendix E.6](#e6-nb-delete-planned-fabricpy).

> **Lesson learned:** do not query `Cable.objects.filter(terminations__interface__device=...)` — `CableTermination` uses a GenericForeignKey. Resolve interface IDs first, then filter `CableTermination` by `termination_type` + `termination_id`.

---

### `nb-create-planned-site.py` — minimal single-device example

Useful template for one device before scaling to full fabric:

```python
from dcim.models import Device, Site, Platform, DeviceRole, DeviceType
from extras.models import Tag

SITE_NAME = "nb-planned-fabric"
DEVICE_NAME = "srl-leaf-nb-1"
NODE_PROFILE = "srl-leaf-spine-dcgw-srlinux-26.3.1"

platform, _ = Platform.objects.get_or_create(name="srl", defaults={"slug": "srl"})
site, created = Site.objects.get_or_create(
    name=SITE_NAME,
    defaults={"slug": "nb-planned-fabric", "status": "planned"},
)
print(f"site {SITE_NAME} created={created}")

role = DeviceRole.objects.filter(name__iexact="leaf").first()
dtype = DeviceType.objects.get(model="7220 IXR-D2L")

def kv_tag(kv: str):
    slug = kv.replace("=", "-").replace("/", "-").replace(".", "-").lower()[:100]
    tag, _ = Tag.objects.get_or_create(name=kv, defaults={"slug": slug, "color": "9e9e9e"})
    return tag

dev, created = Device.objects.get_or_create(
    name=DEVICE_NAME,
    defaults={"site": site, "role": role, "device_type": dtype, "platform": platform, "status": "planned"},
)
dev.tags.set([
    kv_tag(f"eda.nokia.com/node-profile={NODE_PROFILE}"),
    kv_tag("eda.nokia.com/role=leaf"),
])
print(f"device {DEVICE_NAME} created={created} id={dev.id}")
```

---

### Utility scripts (read-only / audit)

**`nb-list-devices.py`** — find duplicate device names across sites:

```python
from dcim.models import Device
from collections import Counter
names = [d.name for d in Device.objects.filter(name__startswith='srl-')]
for name, cnt in sorted(Counter(names).items()):
    if cnt > 1:
        print(f"DUPLICATE {name}: {cnt}")
        for d in Device.objects.filter(name=name):
            print(f"  id={d.id} site={d.site.name} role={d.role.name}")
for d in Device.objects.filter(name__startswith='srl-').order_by('name','id'):
    print(f"{d.id}\t{d.name}\t{d.site.name}")
```

**`nb-audit-devices.py`** — platform and device-type sanity check:

```python
from dcim.models import Device, DeviceType, Platform

print("=== Platforms ===")
for p in Platform.objects.all():
    print(f"  {p.name} slug={p.slug}")

print("\n=== Devices missing platform ===")
for d in Device.objects.filter(platform__isnull=True)[:20]:
    print(f"  {d.name} site={d.site.name} dtype={d.device_type}")
```

---

### Shell wrappers

**`run-nb-delete-planned.sh`** — NetBox-only delete:

```bash
#!/bin/bash
set -euo pipefail
SCRIPT="./manifests/nb-delete-planned-fabric.py"
NS="${NS:-netbox}"
POD=$(kubectl get pod -n "$NS" -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp "$SCRIPT" "${NS}/${POD}:/tmp/nb-delete-planned-fabric.py"
kubectl exec -n "$NS" "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-delete-planned-fabric.py').read())"
```

**`run-delete-planned-all.sh`** — EDA CRs + NetBox (full cleanup):

```bash
#!/bin/bash
set -euo pipefail
EDA_NS="${EDA_NS:-clab-srl-leaf-spine-dcgw}"
DELETE_EDA="${DELETE_EDA:-true}"

if [[ "$DELETE_EDA" == "true" ]]; then
  kubectl delete toponodes,topolinks,interfaces -n "$EDA_NS" -l netbox-planned=true --ignore-not-found
  sleep 3
fi
bash ./manifests/run-nb-delete-planned.sh
```

**`run-planned-fabric-full.sh`** — NetBox create then EDA apply (demo; used additive `kubectl apply`, not `ApplyTopology` reconcile):

```bash
#!/bin/bash
set -e
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
kubectl cp ./manifests/nb-planned-fabric-full.py "netbox/${POD}:/tmp/nb-planned-fabric-full.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-planned-fabric-full.py').read())"
python3 ./manifests/gen-planned-eda.py
kubectl apply -f /tmp/planned-fabric-eda.yaml
```

### Appendix C — Lab file locations

**Kubernetes manifests** (primary — edit `stringData`, then `kubectl apply -f`):

```
./manifests/
  eda-namespace-fabric-dc2.yaml              # Mode B — step 1 (EDA Namespace CR)
  secrets-clab-3-tier-leaf-spine-dcgw.yaml      # baseline Mode A
  instance-clab-3-tier-leaf-spine-dcgw.yaml
  secrets-clab-srl-leaf-spine-dcgw.yaml         # second Mode A fabric
  secrets-fabric-dc2.yaml
  instance-fabric-dc2.yaml
  applytopology-fabric-dc2.yaml
```

**Helper scripts** (catalog seed, Mode B tests, cleanup) — **full source for primary scripts in [Appendix E](#appendix-e--netbox-django-shell-scripts-full-source)**:

```
./manifests/
  nb-seed-eda-catalog.py
  nb-run-seed-catalog.sh
  nb-fix-platforms.py
  nb-test-fabric-dc2.py
  nb-test-allocation-pools-fabric-dc2.py
  nb-test-vlan-pool.py          # legacy — VLAN only
  nb-planned-fabric-full.py
  nb-delete-planned-fabric.py
  test-verify-integration.sh
  ...
```

### Appendix D — Example Kubernetes manifest files

Save manifests from §4.4 / §5 / §9 YAML blocks (or use copies in `manifests/`). Pattern: **edit YAML → `kubectl apply -f <file>`**.

| File | Kind(s) | Namespace (lab) | Section |
|------|---------|-----------------|---------|
| `eda-namespace-fabric-dc2.yaml` | Namespace (`core.eda.nokia.com/v1`) | `eda-system` (CR) → `fabric-dc2` | §5.2, §10.8.2.1 |
| `secrets-clab-3-tier-leaf-spine-dcgw.yaml` | Secret ×2 | `clab-3-tier-leaf-spine-dcgw` | §4.4, §10.8.1.3 |
| `instance-clab-3-tier-leaf-spine-dcgw.yaml` | Instance | `clab-3-tier-leaf-spine-dcgw` | §4.4, §9.2, §10.8.1.3 |
| `instance-clab-srl-leaf-spine-dcgw.yaml` | Instance | `clab-srl-leaf-spine-dcgw` | §4.4 (second fabric) |
| `secrets-clab-srl-leaf-spine-dcgw.yaml` | Secret ×2 | `clab-srl-leaf-spine-dcgw` | §4.4 (second fabric) |
| `secrets-fabric-dc2.yaml` | Secret ×2 | `fabric-dc2` | §5.4, §9.1, §10.8.2.3 |
| `instance-fabric-dc2.yaml` | Instance | `fabric-dc2` | §5.4, §9.2, §10.8.2.3 |
| `applytopology-fabric-dc2.yaml` | ApplyTopology | `fabric-dc2` | §5.6, §9.7, §10.8.2.5 |
| `allocations-fabric-dc2.yaml` | Allocation ×5 | `fabric-dc2` | §5.7, §6.3, §9.8, §10.8.3 |
| `allocations-clab-3-tier-leaf-spine-dcgw.yaml` | Allocation ×5 | `clab-3-tier-leaf-spine-dcgw` | §10.8.3.1b, §8.1 |
| `applyallocation-refresh-fabric-dc2.yaml` | ApplyAllocation | `fabric-dc2` | §6.3, §9.8, §10.8.3.3 |

### Appendix E — NetBox Django shell scripts (full source)

**Every script below is complete** — copy the entire fenced block; there are no `...` omissions. Lab copies: `./scripts\`.

| Script | Appendix | Mode | Used in |
|--------|----------|------|---------|
| `nb-seed-eda-catalog.py` | [E.1](#e1-nb-seed-eda-catalogpy-mode-a) | A — catalog seed | §4.1.1, §10.0, §10.8.1.2 |
| `nb-test-fabric-dc2.py` | [E.2](#e2-nb-test-fabric-dc2py-mode-b) | B — DCIM fabric | §5.5, §10.8.2.4 |
| `nb-test-allocation-pools-fabric-dc2.py` | [E.3](#e3-nb-test-allocation-pools-fabric-dc2py) | Allocations — all 5 pools | §5.7, §10.8.3 |
| `nb-fix-platforms.py` | [E.4](#e4-nb-fix-platformspy) | A — post-sync fix | §10.8.1.6 |
| `nb-planned-fabric-full.py` | [E.5](#e5-nb-planned-fabric-fullpy-legacy-lab-site) | Legacy lab site | Appendix B |
| `nb-delete-planned-fabric.py` | [E.6](#e6-nb-delete-planned-fabricpy) | Legacy cleanup | Appendix B |
| `nb-run-seed-catalog.sh` | [E.7](#e7-nb-run-seed-catalogsh) | Wrapper (stdin seed) | §10.0 |
| `nb-test-allocation-pools-clab3tier.py` | [E.8](#e8-nb-test-allocation-pools-clab3tierpy) | Allocations — clab Mode A | §10.8.3.1b |

**How to run:** see [Appendix B — How to run](#appendix-b--django-orm-scripts-lab). Catalog seed uses stdin redirect ([E.7](#e7-nb-run-seed-catalogsh)); Mode B fabric script uses `kubectl cp` + `exec(open(...))` ([§5.5.3](#553-run-the-script)).

#### E.1 `nb-seed-eda-catalog.py` (Mode A)

Idempotent seed for Region, Tenant, Manufacturer, DeviceTypes, Platforms, and DeviceRoles. `DeviceType.model` must match `TopoNode.spec.platform` exactly. Includes `region-3`/`tenant-c` for Mode B catalog verification.

```python
"""Seed NetBox DCIM catalog before EDA topology sync (Mode A).

Run BEFORE enabling Instance.spec.sync.enabled. EDA pushes TopoNodes as
NetBox Devices and maps TopoNode.spec.platform to an existing DeviceType.model.
It does not create Manufacturers for you.

DeviceType.model must match TopoNode.spec.platform EXACTLY (case/spacing).

After first sync, EDA auto-creates the EDAManaged tag and eda_managed custom field.
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
for cf in CustomField.objects.filter(name__icontains="eda"):
    types = [ct.model for ct in cf.content_types.all()]
    print(f"  custom-field {cf.name} type={cf.type} on={types}")
for t in Tag.objects.filter(name__icontains="EDAManaged"):
    print(f"  tag {t.name} slug={t.slug}")
if not CustomField.objects.filter(name="eda_managed").exists():
    print("  (eda_managed custom field not present yet — normal before first sync)")

print(f"\nCatalog seed complete ({len(DEVICE_TYPES)} device types). Enable Instance sync.")
```

#### E.2 `nb-test-fabric-dc2.py` (Mode B)

Creates site `fabric-dc2`, 4× `7220 IXR-D3L` leaf, 2× `7220 IXR-D4` spine, interfaces, and 8 ISL cables with EDA import tags. **Edit `NODE_PROFILE`** before run.

```python
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
    cable = Cable.objects.create(type="cat6", status="planned", label=label)
    cable.tags.set([isl_tag])
    CableTermination.objects.create(cable=cable, termination_type=ct, termination_id=a.id, cable_end="A")
    CableTermination.objects.create(cable=cable, termination_type=ct, termination_id=b.id, cable_end="B")
    print(f"cable {label} id={cable.id}")

print(f"NetBox {SITE}: 4× {LEAF_DT} leaf, 2× {SPINE_DT} spine, {len(links)} ISL cables — ready for ApplyTopology")
```

#### E.3 `nb-test-allocation-pools-fabric-dc2.py` (allocations)

Creates all five tagged IPAM pool objects for `fabric-dc2` ([§5.7](#57-netbox-allocation-pools-fabric-dc2)). Run before `kubectl apply -f allocations-fabric-dc2.yaml`.

```python
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
vg, vg_created = VLANGroup.objects.get_or_create(
    name="fabric-dc2-vlans",
    defaults={"slug": "fabric-dc2-vlans", "vid_ranges": [[100, 199]]},
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
```

#### E.4 `nb-fix-platforms.py` (Mode A post-sync)

Assigns `srl` / `sros` platform on synced devices; fixes `7750 SR-1` rack height (`u_height` 1→2). Run after first Mode A sync if NetBox UI shows missing platforms.

```python
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
```

#### E.5 `nb-planned-fabric-full.py` (legacy lab site)

Creates 4 leaf + 2 spine at site `nb-planned-fabric` (older lab naming — production Mode B uses `fabric-dc2` / [E.2](#e2-nb-test-fabric-dc2py-mode-b)).

```python
from dcim.models import Device, Site, Platform, DeviceRole, DeviceType, Interface, Cable, CableTermination
from extras.models import Tag
from django.contrib.contenttypes.models import ContentType

SITE = "nb-planned-fabric"
NODE_PROFILE = "srl-leaf-spine-dcgw-srlinux-26.3.1"

platform = Platform.objects.get(name="srl")
site = Site.objects.get(name=SITE)
leaf_role = DeviceRole.objects.get(name__iexact="leaf")
spine_role = DeviceRole.objects.filter(name__iexact="spine").first() or leaf_role
dtype_leaf = DeviceType.objects.get(model="7220 IXR-D2L")
dtype_spine = DeviceType.objects.get(model="7220 IXR-D4")
ct = ContentType.objects.get_for_model(Interface)

def kv_tag(kv: str):
    slug = kv.replace("=", "-").replace("/", "-").replace(".", "-").lower()[:100]
    tag, _ = Tag.objects.get_or_create(name=kv, defaults={"slug": slug, "color": "9e9e9e"})
    return tag

base_tags = [
    kv_tag(f"eda.nokia.com/node-profile={NODE_PROFILE}"),
    kv_tag("netbox-planned=true"),
    kv_tag("site=nb-planned-fabric"),
]
isl_tag = kv_tag("eda.nokia.com/role=interSwitch")

links = [
    ("srl-leaf-planned-01", "ethernet-1/49", "srl-spine-planned-01", "ethernet-1/1"),
    ("srl-leaf-planned-01", "ethernet-1/50", "srl-spine-planned-02", "ethernet-1/1"),
    ("srl-leaf-planned-02", "ethernet-1/49", "srl-spine-planned-01", "ethernet-1/2"),
    ("srl-leaf-planned-02", "ethernet-1/50", "srl-spine-planned-02", "ethernet-1/2"),
    ("srl-leaf-planned-03", "ethernet-1/49", "srl-spine-planned-01", "ethernet-1/3"),
    ("srl-leaf-planned-03", "ethernet-1/50", "srl-spine-planned-02", "ethernet-1/3"),
    ("srl-leaf-planned-04", "ethernet-1/49", "srl-spine-planned-01", "ethernet-1/4"),
    ("srl-leaf-planned-04", "ethernet-1/50", "srl-spine-planned-02", "ethernet-1/4"),
]

def ensure_device(name, role, dtype):
    tags = base_tags + [kv_tag(f"eda.nokia.com/role={role.name}")]
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
            name=name, site=site, role=role, device_type=dtype, platform=platform, status="planned"
        )
        created = True
    dev.tags.set(tags)
    print(f"device {name} created={created}")
    return dev

def ensure_iface(dev, name):
    iface, created = Interface.objects.get_or_create(
        device=dev, name=name, defaults={"type": "100gbase-x-qsfp28", "enabled": True}
    )
    return iface, created

for i in range(1, 5):
    ensure_device(f"srl-leaf-planned-{i:02d}", leaf_role, dtype_leaf)
ensure_device("srl-spine-planned-01", spine_role, dtype_spine)
ensure_device("srl-spine-planned-02", spine_role, dtype_spine)

ifaces = {}
for leaf, leaf_if, spine, spine_if in links:
    for dev_name, if_name in [(leaf, leaf_if), (spine, spine_if)]:
        key = (dev_name, if_name)
        if key not in ifaces:
            dev = Device.objects.get(name=dev_name, site=site)
            ifaces[key], _ = ensure_iface(dev, if_name)

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
    cable = Cable.objects.create(type="cat6", status="planned", label=label)
    cable.tags.set([isl_tag, kv_tag("netbox-planned=true")])
    CableTermination.objects.create(cable=cable, termination_type=ct, termination_id=a.id, cable_end="A")
    CableTermination.objects.create(cable=cable, termination_type=ct, termination_id=b.id, cable_end="B")
    print(f"cable {label} id={cable.id}")

print("NetBox done")
```

#### E.6 `nb-delete-planned-fabric.py`

Scoped delete for site `nb-planned-fabric` only — does **not** touch EDAManaged clab devices.

```python
"""Delete planned-fabric objects from NetBox via Django ORM.

Safe scope: site nb-planned-fabric only (not EDAManaged clab site).
Delete order: cables -> devices (interfaces cascade with devices).
"""
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from dcim.models import Device, Site, Cable, Interface, CableTermination

SITE_NAME = "nb-planned-fabric"
DEVICE_PREFIXES = ("srl-leaf-planned-", "srl-spine-planned-")

site = Site.objects.filter(name=SITE_NAME).first()
if not site:
    print(f"site {SITE_NAME} not found — nothing to do")
    raise SystemExit(0)

prefix_q = Q()
for prefix in DEVICE_PREFIXES:
    prefix_q |= Q(name__startswith=prefix)

devices = Device.objects.filter(site=site).filter(prefix_q).order_by("name")
device_ids = list(devices.values_list("id", flat=True))

print(f"site={SITE_NAME} devices matched: {len(device_ids)}")
for d in devices:
    print(f"  device: {d.name}")

if not device_ids:
    print("no matching devices — done")
    raise SystemExit(0)

ct = ContentType.objects.get_for_model(Interface)
iface_ids = list(Interface.objects.filter(device_id__in=device_ids).values_list("id", flat=True))
cable_ids = (
    CableTermination.objects.filter(termination_type=ct, termination_id__in=iface_ids)
    .values_list("cable_id", flat=True)
    .distinct()
)
cables = Cable.objects.filter(id__in=cable_ids)

print(f"cables to delete: {cables.count()}")
for cable in cables:
    print(f"  delete cable id={cable.id} label={cable.label!r}")
    cable.delete()

print(f"devices to delete: {devices.count()}")
for dev in devices:
    print(f"  delete device id={dev.id} name={dev.name}")
    dev.delete()

remaining = Device.objects.filter(site=site).filter(prefix_q).count()
print(f"done — remaining planned devices in {SITE_NAME}: {remaining}")
```

#### E.7 `nb-run-seed-catalog.sh`

Paste-safe WSL wrapper — streams [E.1](#e1-nb-seed-eda-catalogpy-mode-a) into `manage.py shell` via stdin (avoids OOM on large catalog).

```bash
#!/usr/bin/env bash
# Paste-safe runner for nb-seed-eda-catalog.py (WSL / Linux).
# Usage: bash ./scripts/nb-run-seed-catalog.sh
set -euo pipefail
SCRIPT="${1:-./scripts/nb-seed-eda-catalog.py}"
if [[ ! -f "$SCRIPT" ]]; then
  echo "Missing: $SCRIPT" >&2
  exit 1
fi
kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell < "$SCRIPT"
```

#### E.8 `nb-test-allocation-pools-clab3tier.py`

Mode A baseline namespace `clab-3-tier-leaf-spine-dcgw` — five tagged IPAM pools (`eda-clab3tier-*`). Non-overlapping with `fabric-dc2` ranges. Pair with `allocations-clab-3-tier-leaf-spine-dcgw.yaml`.

```python
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
```

---

## 14. References

- [Nokia EDA NetBox app](https://docs.eda.dev/latest/apps/netbox/)
- [EDA transactions](https://docs.eda.dev/latest/user-guide/transactions/)
- Ansible: `nokia.eda_core_v1.transaction.v2.transaction`
- Namespace bootstrap: `edactl namespace bootstrap create --from-namespace <src> <dst>` — run via `kubectl exec -n eda-system deploy/eda-toolbox -- edactl ...` or a configured local `edactl` alias; **`make edactl` from the playground does not work** for this subcommand

---

*End of document. Replace namespace names, region/tenant pairs (`region-1`/`tenant-a` for first fabric, `region-2`/`tenant-b` for second), and NodeProfile names for your deployment.*
