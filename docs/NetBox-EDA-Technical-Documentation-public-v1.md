Darren Richards, Cloud & Enterprise

August 14, 2026

Document version: Public v1

Note: This is a Lab-validated integration guide. This is a summary of the full technical documentation and is not official Nokia product documentation.

EDA Base Release: 26.4.2.

NetBox App: v4.0.3

# Table of Contents

[Introduction — EDA NetBox App [2](#introduction-eda-netbox-app)](#introduction-eda-netbox-app)

[What the app provides [3](#what-the-app-provides)](#what-the-app-provides)

[IPAM integration model [3](#ipam-integration-model)](#ipam-integration-model)

[Topology integration model [3](#topology-integration-model)](#topology-integration-model)

[Event-driven operation [4](#event-driven-operation)](#event-driven-operation)

[Relationship to this guide [4](#relationship-to-this-guide)](#relationship-to-this-guide)

[Executive summary [4](#executive-summary)](#executive-summary)

[Document conventions [5](#document-conventions)](#document-conventions)

[1. Scope and audience [5](#scope-and-audience)](#scope-and-audience)

[1.1 Scope [5](#scope)](#scope)

[1.2 Audience [5](#audience)](#audience)

[2. Definitions and acronyms [6](#definitions-and-acronyms)](#definitions-and-acronyms)

[Part I — Foundation [6](#part-i-foundation)](#part-i-foundation)

[3. Architecture overview [6](#architecture-overview)](#architecture-overview)

[3.1 Integration paths and namespace model [6](#integration-paths-and-namespace-model)](#integration-paths-and-namespace-model)

[3.2 Namespace instantiation (onboarding prerequisites) [7](#namespace-instantiation-onboarding-prerequisites)](#namespace-instantiation-onboarding-prerequisites)

[Part II — Operating Models [9](#part-ii-operating-models)](#part-ii-operating-models)

[4. Mode A — EDA-managed DCIM sync [9](#mode-a-eda-managed-dcim-sync)](#mode-a-eda-managed-dcim-sync)

[4.1 Mode A — EDA-managed (topology sync on) [9](#mode-a-eda-managed-topology-sync-on)](#mode-a-eda-managed-topology-sync-on)

[4.3 The EDAManaged tag [13](#_Toc237609193)](#_Toc237609193)

[4.4 NetBox Instance CR (Mode A) [15](#_Toc237609194)](#_Toc237609194)

[5. Mode B — NetBox-managed DCIM import [18](#mode-b-netbox-managed-dcim-import)](#mode-b-netbox-managed-dcim-import)

[5.1 Overview [18](#overview)](#overview)

[5.2 EDA namespace + instantiation (fabric-dc2) [19](#eda-namespace-instantiation-fabric-dc2)](#eda-namespace-instantiation-fabric-dc2)

[5.3 NetBox prerequisites (fabric-dc2) [20](#netbox-prerequisites-fabric-dc2)](#netbox-prerequisites-fabric-dc2)

[5.4 Secrets + Instance CR (fabric-dc2) [23](#secrets-instance-cr-fabric-dc2)](#secrets-instance-cr-fabric-dc2)

[5.5 NetBox DCIM modelling — devices, interfaces, cables [24](#netbox-dcim-modelling-devices-interfaces-cables)](#netbox-dcim-modelling-devices-interfaces-cables)

[5.6 ApplyTopology CR [25](#applytopology-cr)](#applytopology-cr)

[5.7 NetBox allocation pools (fabric-dc2) [25](#netbox-allocation-pools-fabric-dc2)](#netbox-allocation-pools-fabric-dc2)

[Mode A vs Mode B (summary) [31](#mode-a-vs-mode-b-summary-1)](#mode-a-vs-mode-b-summary-1)

[Part III — IPAM and Multi-Fabric Design [32](#part-iii-ipam-and-multi-fabric-design)](#part-iii-ipam-and-multi-fabric-design)

[6. Allocations — IPAM pools [32](#allocations-ipam-pools)](#allocations-ipam-pools)

[6.1 Architecture — one Instance per EDA namespace [32](#architecture-one-instance-per-eda-namespace)](#architecture-one-instance-per-eda-namespace)

[6.2 Instance CR — full options [33](#instance-cr-full-options)](#instance-cr-full-options)

[6.3 Allocation CR — all pool types [34](#allocation-cr-all-pool-types)](#allocation-cr-all-pool-types)

[6.4 Lab examples — all pool types (fabric-dc2) [37](#lab-examples-all-pool-types-fabric-dc2)](#lab-examples-all-pool-types-fabric-dc2)

[7. Decoupling topology from allocations [40](#decoupling-topology-from-allocations)](#decoupling-topology-from-allocations)

[7.1 Two paths, one namespace [40](#two-paths-one-namespace)](#two-paths-one-namespace)

[7.1.1 Bootstrap allocation pools vs NetBox-backed pools [40](#bootstrap-allocation-pools-vs-netbox-backed-pools)](#bootstrap-allocation-pools-vs-netbox-backed-pools)

[7.2 Combined deployment patterns [41](#combined-deployment-patterns)](#combined-deployment-patterns)

[7.3 What is shared vs isolated [42](#what-is-shared-vs-isolated)](#what-is-shared-vs-isolated)

[7.4 Recommended build order [42](#recommended-build-order)](#recommended-build-order)

[8. Multi-namespace conventions and permissions [42](#multi-namespace-conventions-and-permissions)](#multi-namespace-conventions-and-permissions)

[8.1 Webhook URLs and tag naming [42](#webhook-urls-and-tag-naming)](#webhook-urls-and-tag-naming)

[8.2 API token and webhook secrets (lab convention) [43](#api-token-and-webhook-secrets-lab-convention)](#api-token-and-webhook-secrets-lab-convention)

[8.3 NetBox API permissions [43](#netbox-api-permissions)](#netbox-api-permissions)

[Part IV — Operations and Constraints [44](#part-iv-operations-and-constraints)](#part-iv-operations-and-constraints)

[11. EDA transactions [44](#eda-transactions)](#eda-transactions)

[11.1 Per-resource operation types [44](#per-resource-operation-types)](#per-resource-operation-types)

[11.2 Rule of thumb (NetBox-imported fabric) [44](#rule-of-thumb-netbox-imported-fabric)](#rule-of-thumb-netbox-imported-fabric)

[11.3 Transaction vs topology import [44](#transaction-vs-topology-import)](#transaction-vs-topology-import)

[11.4 Execution and inspection [45](#execution-and-inspection)](#execution-and-inspection)

[12. Constraints and anti-patterns [45](#constraints-and-anti-patterns)](#constraints-and-anti-patterns)

## Introduction — EDA NetBox App

The **EDA NetBox app** (netbox.eda.nokia.com, built-in EDA Store catalog) integrates Nokia Event-Driven Automation with [NetBox](https://netboxlabs.com/) so IPAM and DCIM data can drive fabric automation while NetBox remains the inventory system of record. Per the [official EDA NetBox app documentation](https://docs.eda.dev/latest/apps/netbox/), the app synchronizes resources between the two systems rather than replacing either platform’s native model.

### What the app provides

The NetBox app exposes four primary custom resources (API group netbox.eda.nokia.com/v1alpha1). **Instance** and **Allocation** must live in the same Kubernetes namespace (not eda-system).

| Resource            | Purpose                                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Instance**        | Target NetBox connection (URL, API token secret, webhook signature secret); optional topology mirror when spec.sync.enabled is true |
| **Allocation**      | Maps tagged NetBox IPAM objects to named EDA allocation pools                                                                       |
| **ApplyTopology**   | Workflow CR: import a NetBox Site (Devices and Cables) into EDA as TopoNode / TopoLink objects                                      |
| **ApplyAllocation** | Workflow CR: on-demand reconcile of a single Allocation (for example after bulk NetBox edits or when webhooks are disabled)         |

The app depends on the EDA Topology app (topologies.eda.nokia.com); it is installed from the EDA Store or via an AppInstaller CR.

### IPAM integration model

EDA continues to allocate from its own pool CRs (IPAllocationPool, SubnetAllocationPool, IndexAllocationPool, and related types). The NetBox app **creates those pools dynamically** from NetBox source objects and **posts allocated values back** to NetBox:

| NetBox source object | NetBox status | Allocation.spec.type    | EDA pool created         | Typical fabric use             |
|----------------------|---------------|-------------------------|--------------------------|--------------------------------|
| IPAM Prefix          | Active        | ip-address              | IPAllocationPool         | System IP (host address)       |
| IPAM Prefix          | Active        | ip-in-subnet            | IPInSubnetAllocationPool | Management IP (address + mask) |
| IPAM Prefix          | Container     | subnet (+ subnetLength) | SubnetAllocationPool     | Inter-switch link subnets      |
| ASN Range            | —             | asn                     | IndexAllocationPool      | BGP ASN                        |
| VLAN Group           | —             | vlan                    | IndexAllocationPool      | VLAN ID                        |

When more than one NetBox prefix, ASN range, or VLAN group should feed the same pool, assign a **distinct tag** in NetBox and reference that tag in Allocation.spec.tags. The Allocation resource **name** becomes the EDA allocation pool name.

### Topology integration model

Two complementary paths exist:

-   **Topology sync (EDA → NetBox):** With Instance.spec.sync.enabled: true, EDA pushes TopoNode and TopoLink objects to NetBox as Devices and Cables. Synced objects are tagged **EDAManaged**; spec.sync.region and spec.sync.tenant scope the mirrored Site.

-   **ApplyTopology (NetBox → EDA):** Imports an existing NetBox Site into EDA for bootstrap when NetBox is the DCIM source of truth. Only devices whose NetBox Platform is srl become TopoNode objects; other devices may still appear as cable endpoints.

### Event-driven operation

NetBox **Event Rules** trigger a **Webhook** on create, update, or delete of IPAM and DCIM objects EDA cares about (Prefixes, VLANs, ASNs, Devices, Cables, Sites, and related types). The webhook URL is namespace- and instance-scoped:

    https://<eda-host>:<port>/core/httpproxy/v1/netbox/webhook/<namespace>/<instance-name>

NetBox must also expose an API token (write-capable for IPAM; DCIM write when topology sync or ApplyTopology is used). The controller automatically creates the **EDAManaged** tag and matching eda_managed custom field in NetBox—do not rename or remove them.

Note: Webhook connectivity is not mandatory. It is optional, if dynamic update of NetBox is not preferred, use workflows (within EDA).

### Relationship to this guide

Product documentation covers installation, CR schemas, supported objects, and an end-to-end fabric example. **This document** applies that model to a multi-namespace lab: **Mode A** (EDA-managed topology sync) and **Mode B** (NetBox-managed import via ApplyTopology), plus allocation-only paths, webhook isolation, validation scripts, and constraints validated on clab-3-tier-leaf-spine-dcgw and fabric-dc2.

## Executive summary

Nokia Event-Driven Automation (EDA) integrates with NetBox through the **EDA NetBox application**, supporting two topology operating models and a decoupled **IPAM allocation** path:

| Model                         | Direction                                                        | sync.enabled | Primary use                                                            |
|-------------------------------|------------------------------------------------------------------|--------------|------------------------------------------------------------------------|
| **Mode A** — EDA-managed      | EDA → NetBox DCIM mirror                                         | true         | Containerlab / live fabric; NetBox reflects deployed topology          |
| **Mode B** — NetBox-managed   | NetBox → EDA via ApplyTopology                                   | false        | Planned / greenfield design; NetBox is DCIM source of truth            |
| **Allocations** (either mode) | NetBox tagged pools → EDA pools → consumed values back to NetBox | n/a          | VLAN, ASN, system IP, management IP, ISL subnets (IPv4 /31, IPv6 /127) |

**Design rule:** one EDA Kubernetes namespace = one fabric context = one Instance CR + one dedicated webhook URL.

This guide covers architecture, prerequisites, step-by-step procedures, Kubernetes manifests, NetBox Django scripts, and lab-validated constraints (including known gaps such as Mode B ASN allocation).

Allocations support both webhook and workflow models.

## Document conventions

| Convention          | Meaning                                                          |
|---------------------|------------------------------------------------------------------|
| **§N** / **§N.M**   | Section references (e.g. §5.3 = NetBox prerequisites for Mode B) |
| **Mode A / Mode B** | EDA-managed sync vs NetBox-managed import — see §4 and §5        |
| **EDAManaged**      | NetBox tag marking objects created or claimed by EDA             |
| **kubectl**         | Run from **WSL** against the lab cluster unless noted            |
| **Scripts**         | ../scripts/ relative to this repo root                           |
| **Manifests**       | ../manifests/ — Kubernetes YAML and secret templates             |
| **Pass criteria**   | Explicit checks after each procedure block                       |

**Section numbering:** §4 = Mode A · §5 = Mode B (step number = section number in §5.1 build order) · §6 = IPAM Allocations.

## 1. Scope and audience

### 1.1 Scope

**In scope:**

-   EDA NetBox app: Instance, Allocation, ApplyTopology, ApplyAllocation

-   DCIM topology (Site, Device, Interface, Cable) and IPAM pools (Prefix, VLAN Group, ASN Range)

-   SR Linux (platform: srl) devices as TopoNode objects

-   Lab cluster: clab-srl-leaf-spine-dcgw (EDA-managed) and fabric-dc2 (NetBox-managed pattern)

**Out of scope:**

-   NetBox installation and Helm chart configuration (except ENFORCE_GLOBAL_UNIQUE)

-   Non-SRL platforms as TopoNode (may appear as cable endpoints only)

-   EDA application development beyond the NetBox app

### 1.2 Audience

| Role                 | Primary sections |
|----------------------|------------------|
| Network architect    | 3, 4, 5, 7       |
| EDA operator         | 5, 8, 9, 10      |
| NetBox administrator | 5, 8             |
| Automation engineer  | 5, 9, 10         |

## 2. Definitions and acronyms

| Term                        | Definition                                                                                                                                  |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **DCIM**                    | NetBox Data Center Infrastructure Management (sites, devices, cables)                                                                       |
| **IPAM**                    | NetBox IP Address Management (prefixes, VLANs, ASNs)                                                                                        |
| **CR**                      | Kubernetes Custom Resource in EDA                                                                                                           |
| **Instance**                | netbox.eda.nokia.com/v1alpha1 CR — connection to one NetBox server per EDA namespace                                                        |
| **Allocation**              | CR mapping tagged NetBox IPAM objects to EDA allocation pools                                                                               |
| **ApplyTopology**           | Workflow CR importing a NetBox site into EDA as TopoNode/TopoLink                                                                           |
| **EDAManaged**              | Reserved NetBox tag (+ eda_managed field) marking objects EDA created or claimed — see §4.2                                                 |
| **TopoNode**                | EDA topology CR representing an SR Linux node                                                                                               |
| **Reconcile**               | ApplyTopology default — desired state = NetBox site only; orphans deleted                                                                   |
| **Namespace instantiation** | CRs labeled eda.nokia.com/bootstrap=true form the template onboarding kit; EDA copies them into new namespaces via instantiation — see §3.2 |

# Part I — Foundation

## 3. Architecture overview

### 3.1 Integration paths and namespace model

Nokia EDA’s NetBox app exposes **two independent integration paths**:

| Path                     | NetBox module | Primary direction                                   | Trigger                                |
|--------------------------|---------------|-----------------------------------------------------|----------------------------------------|
| **Topology / inventory** | DCIM          | Mode-dependent                                      | ApplyTopology + optional sync.enabled  |
| **Allocations**          | IPAM          | NetBox pools → EDA → consumed values back to NetBox | Allocation + webhook / ApplyAllocation |

| Concept           | Where it lives                      | Notes                                                                                                                                                                                       |
|-------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **K8s namespace** | EDA                                 | Created first; all CRs (Instance, TopoNode, Allocation, …) live here                                                                                                                        |
| **NetBox site**   | NetBox                              | **Maps to the EDA namespace** — naming convention ties them together. Also appears as a **label** on imported TopoNodes (site: fabric-dc2); the label is metadata, not the namespace itself |
| **Node profile**  | EDA NodeProfile + NetBox device tag | eda.nokia.com/node-profile=\<name\>                                                                                                                                                         |

**Site ↔ namespace mapping (lab convention):**

| Mode                        | Who owns topology                | EDA namespace                               | NetBox site                                                     | How they align                                                                                               |
|-----------------------------|----------------------------------|---------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Mode A** — EDA-managed    | EDA (Containerlab / live fabric) | e.g. clab-3-tier-leaf-spine-dcgw            | Created by **sync** — site name typically matches the namespace | Instance.spec.sync pushes DCIM; NetBox **Site** is populated from EDA with region / tenant from the Instance |
| **Mode B** — NetBox-managed | NetBox (design source)           | Created to match site name, e.g. fabric-dc2 | You create **Site** fabric-dc2 in NetBox first                  | ApplyTopology.spec.siteName imports that site into the **same-named** EDA namespace                          |

**Namespace is defined in EDA, not NetBox.** NetBox holds sites and devices; EDA decides target namespace via Instance placement and (Mode B) ApplyTopology in that namespace. The site=\<name\> device tag and TopoNode label mirror the NetBox site name for import filtering — they do not replace the K8s namespace.

| Fabric                 | Example namespace        | Direction                                                        |
|------------------------|--------------------------|------------------------------------------------------------------|
| **A — EDA-managed**    | clab-srl-leaf-spine-dcgw | sync.enabled=true → NetBox DCIM mirror (EDAManaged)              |
| **B — NetBox-managed** | fabric-dc2               | NetBox design source ← ApplyTopology import (sync.enabled=false) |

### 3.2 Namespace instantiation (onboarding prerequisites)

Every new fabric namespace needs relevant **onboarding** CRs before TopoNodes can onboard: NodeProfile, NodeUser, Init, mgmt/system IP pools, and related supporting resources. You do not need to hand-author these if namespace instantiation works.

#### How it works

At **EDA installation**, the default user namespace (typically eda) is populated with CRs that carry the label **eda.nokia.com/bootstrap: "true"** on each resource — NodeProfiles, NodeUsers, Init, allocation pools, etc. These are the **template** onboarding objects.

**Recommended — EDA Namespace CR** (same as EDA UI → Create namespace):

    apiVersion: core.eda.nokia.com/v1
    kind: Namespace
    metadata:
      name: fabric-dc2
      namespace: eda-system          # CR object lives in eda-system
    spec:
      bootstrap:
        fromNamespace: eda           # copy onboarding kit from template namespace

EDA creates the Kubernetes namespace fabric-dc2 and copies relevant onboarding CRs in one step. Use from Namespace: clab-3-tier-leaf-spine-dcgw (or another fabric) to inherit that namespace’s NodeProfile set instead of generic eda profiles if required.

| What gets copied (typical)                      | Purpose                                                                                       |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **NodeProfile**                                 | OS/version, onboarding creds, mgmt pool — name goes in NetBox eda.nokia.com/node-profile= tag |
| **NodeUser**                                    | Permanent management user; referenced by NodeProfile                                          |
| **NodeGroup** / **NodeUserGroup**               | Group bindings for NodeUser                                                                   |
| **Init**                                        | Day-0 bootstrap for selected TopoNodes                                                        |
| **IPAllocationPool** / **SubnetAllocationPool** | Mgmt and system IP pools for onboarding                                                       |

**This is independent of NetBox** — namespace instantiation is pure EDA onboarding. It does **not** set sync.enabled or NetBox integration; that comes later via the Instance CR.

#### Alternative Namespace creation (edactl CLI)

Same result as the EDA Namespace CR — run via **eda-toolbox**:

    kubectl exec -n eda-system deploy/eda-toolbox -- \
      edactl namespace bootstrap create --from-namespace eda fabric-dc2

    kubectl exec -n eda-system deploy/eda-toolbox -- \
      edactl -n fabric-dc2 namespace bootstrap list

    kubectl get nodeprofiles,nodeusers,inits,ipallocationpools,subnetallocationpools -n fabric-dc2

Use --from-namespace clab-3-tier-leaf-spine-dcgw to match clab NodeProfile names.

| Approach                              | When to use                                                                                      |
|---------------------------------------|--------------------------------------------------------------------------------------------------|
| **EDA Namespace CR**                  | **Recommended** — EDA UI or kubectl apply; creates namespace + copies onboarding kit in one step |
| **edactl namespace bootstrap create** | CLI equivalent when the namespace already exists but instantiation was never run                 |
| **Manual YAML**                       | Custom NodeProfiles / onboarding kit only — apply NodeProfile, NodeUser, Init, pools yourself    |

**After instantiation — NetBox-specific adjustments:**

1.  Note the **NodeProfile name** copied into the namespace (e.g. srl-leaf-spine-dcgw-srlinux-26.3.1) — set matching tag on NetBox devices.

2.  **Patch NodeUser nodeSelector** if imported TopoNodes use labels different from the clab template (e.g. add eda.nokia.com/source=netbox).

3.  **Patch Init nodeSelectors** similarly if nodes will onboard via ZTP.

4.  Namespace instantiation does **not** create NetBox Instance / Allocation CRs — add those separately.

The eda.nokia.com/bootstrap=true label marks which CRs belong to the **onboarding CR’s**. Playground / clab namespaces receive the relevant CR’s from the eda-kpt-playground package at install time; new fabric namespaces get the same core set via **namespace instantiation** (EDA Namespace CR or edactl namespace bootstrap create).

# Part II — Operating Models

## 4. Mode A — EDA-managed DCIM sync

Mode A: EDA owns topology (TopoNode / TopoLink); NetBox mirrors DCIM with EDAManaged.

### 4.1 Mode A — EDA-managed (topology sync on)

**Pattern:** EDA owns the live fabric; NetBox is a **mirror** for visibility and IPAM bookkeeping.

| EDA (source of truth)                   | Sync              | NetBox (mirror)       |
|-----------------------------------------|-------------------|-----------------------|
| Namespace e.g. clab-srl-leaf-spine-dcgw | sync.enabled=true | Site, Devices, Cables |
| TopoNode / TopoLink / Interface         | → push            | Tagged EDAManaged     |

| Setting                    | Value                                                      |
|----------------------------|------------------------------------------------------------|
| Instance.spec.sync.enabled | true                                                       |
| Instance.spec.sync.region  | NetBox Region for synced Site                              |
| Instance.spec.sync.tenant  | NetBox Tenant for synced Site                              |
| NetBox Site                | **Created/updated by EDA** — not your design source        |
| ApplyTopology              | Usually **not** used (topology born in EDA / Containerlab) |

**What EDA pushes to NetBox (when sync runs):**

| EDA object | NetBox object         | Notes                              |
|------------|-----------------------|------------------------------------|
| TopoNode   | Device (+ DeviceType) | Under synced Site                  |
| TopoLink   | Cable                 | Between device interfaces          |
| (implicit) | Site                  | Named from namespace / sync config |
| Interfaces | Device interfaces     | Created as part of device sync     |

All pushed DCIM objects receive the **EDAManaged** tag and eda_managed custom field. **Only EDA should mutate EDAManaged DCIM objects.**

**Typical lab example:** Containerlab fabric in clab-3-tier-leaf-spine-dcgw with sync.enabled: true, region region-1, tenant tenant-a. NetBox site mirrors the clab topology; devices carry EDAManaged.

**Direction of truth:** EDA → NetBox for devices/cables. Changes made manually in NetBox to EDAManaged devices risk being overwritten on the next sync cycle.

**Important:** With sync.enabled: true, adding a Device manually in NetBox does **not** create a TopoNode in EDA (lab: srl-leaf-9 stayed NetBox-only). Sync is **EDA → NetBox** for DCIM inventory.

#### 4.1.1 Mode A — NetBox catalog prerequisites (before sync)

Before enabling Instance.spec.sync.enabled, seed NetBox with the **DCIM catalog** objects EDA needs to materialize TopoNode/TopoLink records. You are **not** creating individual device inventory here — EDA creates Sites, Devices, Cables, and (often) DeviceTypes during sync. You **are** ensuring lookup tables exist so the first reconcile succeeds.

| NetBox object                          | Required before sync?                           | Who creates device records?                                                                                                                                                                                                                                     | Notes                                                                               |
|----------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| **Region**                             | Yes — must match Instance.spec.sync.region      | EDA creates Site under this region                                                                                                                                                                                                                              | See tenancy table below                                                             |
| **Tenant**                             | Yes — must match Instance.spec.sync.tenant      | EDA assigns to synced Site/Devices                                                                                                                                                                                                                              | See tenancy table below                                                             |
| **Manufacturer**                       | Yes (recommended)                               | —                                                                                                                                                                                                                                                               | Lab: Nokia                                                                          |
| **DeviceType**                         | Yes — model must match TopoNode.spec.platform   | EDA may also create DeviceTypes on push; pre-seeding avoids mapping errors                                                                                                                                                                                      | Lab: 7220 IXR-D2L, 7220 IXR-D3L, 7220 IXR-D4, 7750 SR-1, 7250 IXR-X1B, 7250 IXR-X3B |
| **Platform**                           | Recommended                                     | EDA sets platform on synced devices when mapped                                                                                                                                                                                                                 | Lab: srl, sros — see nb-fix-platforms.py post-sync                                  |
| **DeviceRole**                         | Recommended                                     | EDA maps from **eda.nokia.com/role** label on each TopoNode (e.g. leaf, spine, dcgw, border-leaf) — these are **fabric role labels** on nodes in that namespace, not separate NetBox sites. Pre-create matching DeviceRole records so sync can set Device.role. |                                                                                     |
| **Site / Device / Cable**              | **No** — created by sync                        | **EDA**                                                                                                                                                                                                                                                         | Tagged EDAManaged after push                                                        |
| **EDAManaged tag + eda_managed field** | Pre-create tag optional; CF usually EDA-created | **EDA controller** (or you pre-create tag)                                                                                                                                                                                                                      | See §4.2 — must exist in NetBox before EDA can tag objects                          |
| **API token**                          | Yes — DCIM write for Mode A                     | —                                                                                                                                                                                                                                                               | Same token can be reused across namespaces.                                         |
| **Webhook**                            | Yes — one per EDA namespace                     | —                                                                                                                                                                                                                                                               | URL path includes namespace + Instance name.                                        |
| **Event rule**                         | Yes — bound to that webhook                     | —                                                                                                                                                                                                                                                               | **Required, not optional.** A webhook without an event rule does nothing.           |

**Lab-validated:** Instance.status.reachable: true only proves the API token works. It does **not** prove DCIM sync is complete. If the **event rule is missing**, initial device push may partially succeed on TopoNode reconcile, but **interfaces and cables will not sync**. Configure webhook **and** event rule in NetBox **before** expecting a full mirror.

Disable or delete webhooks/event rules for namespaces you no longer use.

**Region / Tenant per fabric** — one pair per namespace with sync.enabled: true. **Baseline:** for example, first Mode A fabric uses region-1 / tenant-a; each additional fabric increments the number and tenant letter (region-2 / tenant-b, region-3 / tenant-c, …). Seed all pairs in the catalog script before enabling each NetBox Instance.

| Order              | EDA namespace (lab)         | Instance.spec.sync                 | Notes                                                 |
|--------------------|-----------------------------|------------------------------------|-------------------------------------------------------|
| **Baseline**       | clab-3-tier-leaf-spine-dcgw | region: region-1, tenant: tenant-a | First Mode A fabric                                   |
| **Second**         | clab-srl-leaf-spine-dcgw    | region: region-2, tenant: tenant-b | Second Mode A fabric                                  |
| **Planned import** | fabric-dc2                  | sync.enabled: false                | Mode B — assign Region/Tenant on NetBox Site manually |

**eda_managed vs EDAManaged:** Two linked NetBox objects created on **first EDA reconcile** (sync or allocation):

| Object          | Type                              | Purpose                                                                   |
|-----------------|-----------------------------------|---------------------------------------------------------------------------|
| **EDAManaged**  | NetBox **tag**                    | Visible in UI filters; marks “EDA owns this object”                       |
| **eda_managed** | NetBox **custom field** (boolean) | Machine-readable flag on supported models; used by the NetBox app and API |

Both are set together when EDA creates or claims an object. The catalog script only **checks** whether they exist — it does not create them. Ensure the **EDAManaged tag exists in NetBox** (pre-create or let EDA create on first reconcile with Extras Tag/CF permissions) before expecting tagged sync results.

**Roles (leaf / spine / dcgw):** In EDA, each TopoNode carries labels such as eda.nokia.com/role=leaf and site: \<fabric-name\>. The fabric is the EDA **namespace** (and synced NetBox **Site**). Role labels describe the node’s function **in that fabric**. The catalog seed pre-creates NetBox DeviceRole entries with the same names so Mode A sync can populate Device.role. Mode B: you set equivalent tags on NetBox devices before ApplyTopology.

**Lab fabric platforms** (match TopoNode.spec.platform in clab namespaces):

| TopoNode.spec.platform | u_height | OS (typical) |
|------------------------|----------|--------------|
| 7220 IXR-D2L           | 1        | SR Linux     |
| 7220 IXR-D3L           | 1        | SR Linux     |
| 7220 IXR-D4            | 1        | SR Linux     |
| 7750 SR-1              | 2        | SR OS        |
| 7250 IXR-X1B           | 1        | SR Linux     |
| 7250 IXR-X3B           | 1        | SR Linux     |

**Adding more hardware:** The seed script loads **lab + extended** Nokia SKUs by default (DEVICE_TYPES = LAB_DEVICE_TYPES + EXTENDED_DEVICE_TYPES). Trim to LAB_DEVICE_TYPES only if you want a minimal catalog. Every distinct TopoNode.spec.platform needs a matching DeviceType.model (exact string). Re-run the script — get_or_create is idempotent and updates u_height for example if changed.

**Extended Nokia catalog (EXTENDED_DEVICE_TYPES):** Merged into the default seed list below. u_height from Nokia hardware datasheets. Lab models (D2L/D3L/D4, SR-1, X1B/X3B) are in LAB_DEVICE_TYPES; extended adds the rest.

| Family         | DeviceType.model | u_height | Notes                                            |
|----------------|------------------|----------|--------------------------------------------------|
| **7215 IXS**   | 7215 IXS-A1      | 1        |                                                  |
| **7220 IXR-D** | 7220 IXR-D1      | 1        | D2L, D3L, D4 in lab table                        |
|                | 7220 IXR-D5      | 1        |                                                  |
| **7220 IXR-H** | 7220 IXR-H2      | 4        |                                                  |
|                | 7220 IXR-H3      | 1        |                                                  |
|                | 7220 IXR-H4-32D  | 1        |                                                  |
|                | 7220 IXR-H4      | 2        |                                                  |
|                | 7220 IXR-H5-32D  | 1        |                                                  |
|                | 7220 IXR-H5-64D  | 2        |                                                  |
|                | 7220 IXR-H5-64O  | 2        | OSFP112 variant                                  |
|                | 7220 IXR-H6-64   | 3        |                                                  |
| **7250 IXR-X** | 7250 IXR-X4      | 1        | X1B/X3B in lab table                             |
| **7250 IXR-e** | 7250 IXR-6e      | 10       |                                                  |
|                | 7250 IXR-10e     | 16       |                                                  |
|                | 7250 IXR-18e     | 35       |                                                  |
| **7750 SR**    | 7750 SR-7        | 8        | SR-1 in lab table                                |
|                | 7750 SR-12       | 14       |                                                  |
|                | 7750 SR-12e      | 22       |                                                  |
| **7750 SR-1x** | 7750 SR-1x-48D   | 2        | 48D family                                       |
|                | 7750 SR-1-48D    | 2        |                                                  |
|                | 7750 SR-1-24D    | 2        |                                                  |
|                | 7750 SR-1x-92S   | 2        | 92S family                                       |
|                | 7750 SR-1-92S    | 2        |                                                  |
|                | 7750 SR-1-46S    | 2        |                                                  |
| **7750 SR-s**  | 7750 SR-1s       | 3        |                                                  |
|                | 7750 SR-1se      | 3        |                                                  |
|                | 7750 SR-2s       | 5        |                                                  |
|                | 7750 SR-2se      | 5        |                                                  |
|                | 7750 SR-7s       | 17       | Datasheet: 16 or 17 RU depending on power config |
|                | 7750 SR-14s      | 28       | Datasheet: 27 or 28 RU depending on power config |

**Platform string matching:** DeviceType.model must match TopoNode.spec.platform exactly (case/spacing). Lab uses 7250 IXR-X1B and 7250 IXR-X3B. Check platforms with:  
kubectl get toponodes -n \<ns\> -o jsonpath='{range .items\[\*\]}{.spec.platform}{"\\n"}{end}' \| sort -u  
Interface port templates (QSFP-DD counts, etc.) are **not** created by the catalog script.

**Build order (Mode A):**

1.  NetBox: Region, Tenant, Manufacturer, DeviceTypes, Platforms, DeviceRoles (catalog seed — check Git Repository referenced later)

2.  NetBox: API token (DCIM write), **webhook + event rule** for this namespace— **before** expecting full sync

3.  EDA: namespace exists; Containerlab / workflows have TopoNode/TopoLink CRs

4.  EDA: Instance CR with sync.enabled: true, matching region/tenant → verify reachable=true

5.  Wait for sync — Devices, interfaces, Site, Cables appear in NetBox with EDAManaged

6.  Optional post-sync fixes: Changes to platform assignment, device-type u_height etc (run nb-fix-platforms.py)

### 4.2 The EDAManaged tag

EDAManaged is a **reserved NetBox tag** (and matching **eda_managed boolean custom field**) used by the Nokia EDA NetBox app to mark objects EDA created or claimed.

**Important:** The tag is **not** defined on the EDA Instance CR. It is a **NetBox object** that must exist (or be created by EDA) before EDA can tag synced or allocated objects. Mode B design devices must **not** carry this tag — see [§5](#X7a3a2779116ddf5ce4f6c09e6413eaa09d922d8).

#### Who creates EDAManaged / eda_managed

| Object                       | Typical creator                                                               | When                                                     |
|------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------|
| **EDAManaged tag**           | EDA NetBox controller on **first reconcile**, **or you** pre-create in NetBox | Before/at first sync or first allocation write-back      |
| **eda_managed custom field** | EDA controller on first reconcile (recommended)                               | Same — requires **Extras → Custom Field** API permission |

EDA needs **Extras → Tag** and **Extras → Custom Field** write permission on the API token to auto-create these. If reconcile fails to tag objects, verify permissions and that the EDAManaged tag exists in NetBox (**Customization → Tags**).

**Pre-create (optional but valid):** Create tag **EDAManaged** (slug edamanaged) in NetBox before applying the Instance CR if you want the tag visible before first reconcile. Do **not** rename or delete after EDA uses it. The eda_managed custom field is best left for EDA to create on first reconcile.

#### What it marks

Objects NetBox should treat as **owned by EDA**:

| Object                                          | When it gets EDAManaged                                                        |
|-------------------------------------------------|--------------------------------------------------------------------------------|
| **Site, Device, Cable, DeviceType** (sync path) | EDA pushes them via topology sync (sync.enabled: true)                         |
| **IP Address, VLAN, ASN** (allocation path)     | EDA allocates a value from a pool and writes it back to NetBox                 |
| **Your design site/devices** (Mode B)           | **Never** — you create these without EDAManaged; EDA imports them to TopoNodes |

#### What “only EDA should mutate” means

-   **Do not manually edit** EDAManaged devices, cables, or sites in the NetBox UI for routine changes — EDA is the source of truth for those objects (Mode A) or for tracking allocation ownership (IPAM).

-   On the next **sync cycle**, EDA may **overwrite** manual NetBox edits to EDAManaged DCIM objects.

-   **Do not delete** the EDAManaged tag or eda_managed custom field — the NetBox app depends on them.

-   **Do not run ApplyTopology** against a site or devices that already carry EDAManaged — the workflow expects a NetBox-owned design source (Mode B only).

#### How to use it in practice

| Task                                 | Action                                                                                   |
|--------------------------------------|------------------------------------------------------------------------------------------|
| See what EDA synced from clab        | NetBox → Devices → filter tag **EDAManaged**                                             |
| See what EDA allocated from pools    | NetBox → IP Addresses / VLANs → filter **EDAManaged**                                    |
| Your planned fabric (Mode B)         | Site and devices **without** EDAManaged; only consumed IPs/VLANs get it after allocation |
| Troubleshoot “who owns this device?” | If EDAManaged → EDA; if not → your team (or not yet synced)                              |

### 4.3 NetBox Instance CR (Mode A)

The **NetBox Instance CR** connects EDA to NetBox for this namespace. For Mode A, set sync.enabled: true with matching region / tenant.

After you configure NetBox webhook and verify sync. Site and devices are **created by EDA on first sync** — not pre-modelled in NetBox.

Allocation pool tags and Allocation CRs are in [§6](#Xe8cc2cfa4755709b38f2594420d8a02e2b0e30e) (orthogonal to DCIM).

**Region / Tenant convention:** baseline namespace clab-3-tier-leaf-spine-dcgw → region-1 / tenant-a. Each additional Mode A namespace increments: region-2 / tenant-b, region-3 / tenant-c, … in this implementation example.

**Baseline fabric:** clab-3-tier-leaf-spine-dcgw. Apply **secrets YAML first**, then **Instance YAML** — same EDA namespace.

**Multi-line YAML:** Each yaml code block below is a complete file with line breaks and indentation. If you see everything on one line, open the lab file directly: ../manifests/instance-clab-3-tier-leaf-spine-dcgw.yaml (or use the canvas — it now renders YAML in a \<pre\> block, not inline code).

**Credentials** — edit stringData in the secrets file before apply:

| Value          | NetBox UI location                                                 | YAML key                                                   |
|----------------|--------------------------------------------------------------------|------------------------------------------------------------|
| API token      | Admin → Authentication → API Tokens                                | stringData.apiToken on Secret netbox-api-token             |
| Webhook secret | Operations → Integrations → Webhooks → **Secret** (this namespace) | stringData.signatureKey on Secret netbox-webhook-signature |

Lab: one API token across namespaces is possible; webhook secret **unique per namespace**.

#### Mode A baseline — clab-3-tier-leaf-spine-dcgw (region-1 / tenant-a)

Save each block below as the named file, edit stringData, then apply in order.

##### secrets-clab-3-tier-leaf-spine-dcgw.yaml

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

##### instance-clab-3-tier-leaf-spine-dcgw.yaml

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
    kubectl apply -f secrets-clab-3-tier-leaf-spine-dcgw.yaml
    kubectl apply -f instance-clab-3-tier-leaf-spine-dcgw.yaml
    kubectl get instance.netbox.eda.nokia.com netbox -n clab-3-tier-leaf-spine-dcgw -o jsonpath='reachable={.status.reachable}{"\n"}'

**Pass:** reachable=true

#### Mode A second fabric — clab-srl-leaf-spine-dcgw (region-2 / tenant-b)

##### secrets-clab-srl-leaf-spine-dcgw.yaml

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

##### instance-clab-srl-leaf-spine-dcgw.yaml

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
    kubectl apply -f secrets-clab-srl-leaf-spine-dcgw.yaml
    kubectl apply -f instance-clab-srl-leaf-spine-dcgw.yaml
    kubectl get instance.netbox.eda.nokia.com netbox -n clab-srl-leaf-spine-dcgw -o jsonpath='reachable={.status.reachable}{"\n"}'

| NetBox Instance field      | Purpose                                       |
|----------------------------|-----------------------------------------------|
| spec.url                   | NetBox API base URL                           |
| spec.apiToken              | Kubernetes Secret with NetBox REST token      |
| spec.signatureKey          | Kubernetes Secret with webhook HMAC secret    |
| spec.sync.enabled          | true for Mode A (EDA → NetBox push)           |
| spec.sync.region / .tenant | NetBox Region and Tenant for synced Site      |
| spec.disableWebhook        | true disables auto-reconcile on NetBox events |

**Status:** status.reachable, status.errorReason, status.lastChecked — reachable: true before sync.

#### Mode A checklist (before first sync)

| \#  | NetBox                                                      | EDA                                                                  |
|-----|-------------------------------------------------------------|----------------------------------------------------------------------|
| 1   | Region + Tenant exist                                       | TopoNodes in namespace                                               |
| 2   | Catalog seeded — DeviceTypes, Roles                         | Namespace instantiated                                               |
| 3   | API token + **webhook + event rule** — both required        | Secrets applied                                                      |
| 4   | EDAManaged pre-created **or** token has Extras Tag/CF write | Instance CR applied; reachable=true                                  |
| 5   | —                                                           | Wait for sync → Site + devices + interfaces + cables with EDAManaged |

## 5. Mode B — NetBox-managed DCIM import

NetBox is the **design source** for DCIM. EDA imports topology via **ApplyTopology**. IPAM allocation pools are optional.

**Lab example:** EDA namespace fabric-dc2, NetBox site fabric-dc2, sync.enabled: false.

### 5.1 Overview

| From (NetBox)                        | To (EDA)                      | Mechanism     |
|--------------------------------------|-------------------------------|---------------|
| DCIM site fabric-dc2 (no EDAManaged) | Namespace fabric-dc2          | ApplyTopology |
| Devices, interfaces, cables          | TopoNode, Interface, TopoLink | Import only   |

| Setting                    | Value                                                              |
|----------------------------|--------------------------------------------------------------------|
| Instance.spec.sync.enabled | false                                                              |
| NetBox Site                | **You create** — must **not** be EDAManaged                        |
| ApplyTopology              | **Required** — workflow CR reads NetBox site → TopoNode / TopoLink |
| Device tags                | eda.nokia.com/node-profile=... (required), role, custom labels     |

**NetBox → EDA mapping:**

| NetBox (DCIM) | EDA CR                            | Requirements                                                   |
|---------------|-----------------------------------|----------------------------------------------------------------|
| Device        | TopoNode                          | Platform = srl; eda.nokia.com/node-profile=\<NodeProfile\> tag |
| Interface     | Interface                         | On SRL devices                                                 |
| Cable         | TopoLink                          | Both ends resolved                                             |
| Site name     | TopoNode label site: \<siteName\> | Not an EDA namespace                                           |

**ApplyTopology default:** operation: Reconcile — orphans in the EDA namespace are **deleted**. Use a **dedicated** namespace; never import into a clab/Mode A namespace.

**Build order** — section number = step number:

| Step | Action                                                                                    |
|------|-------------------------------------------------------------------------------------------|
| 1    | EDA namespace + instantiation; NodeUser patch                                             |
| 2    | NetBox prerequisites (region, tenant, site, webhook, event rule) — **before** EDA secrets |
| 3    | secrets-fabric-dc2.yaml + instance-fabric-dc2.yaml → reachable=true                       |
| 4    | NetBox DCIM — nb-test-fabric-dc2.py (devices, interfaces, cables)                         |
| 5    | applytopology-fabric-dc2.yaml → TopoNodes / TopoLinks                                     |
| 6    | (Optional) NetBox IPAM allocation pools + allocations-fabric-dc2.yaml                     |

### 5.2 EDA namespace + instantiation (fabric-dc2)

Create a **dedicated** fabric namespace before any NetBox Instance or ApplyTopology.

**File: eda-namespace-fabric-dc2.yaml** (same as EDA UI → Create namespace)

    # Mode B — recommended. Matches EDA UI "Create namespace".
    apiVersion: core.eda.nokia.com/v1
    kind: Namespace
    metadata:
      name: fabric-dc2
      namespace: eda-system          # CR object is stored in eda-system
    spec:
      bootstrap:
        fromNamespace: eda           # or clab-3-tier-leaf-spine-dcgw | clab-srl-leaf-spine-dcgw

Refer to Section 4 for further details on how to validate.

| Onboarding object                               | Purpose for Mode B                                                            |
|-------------------------------------------------|-------------------------------------------------------------------------------|
| **NodeProfile**                                 | Name goes in NetBox device tag eda.nokia.com/node-profile=\<name\>            |
| **NodeUser** / **Init**                         | Onboarding when TopoNodes are deployed (patch below for NetBox-sourced nodes) |
| **IPAllocationPool** / **SubnetAllocationPool** | Mgmt and system IP pools for future node onboarding                           |

Empty onboarding CR’s after apply? If the K8s namespace fabric-dc2 exists but kubectl get nodeprofiles -n fabric-dc2 returns nothing, namespace instantiation did not run — apply the EDA **Namespace CR** with spec.bootstrap.fromNamespace or run **edactl namespace bootstrap create**. If the namespace was created without the onboarding CR’s, delete it and recreate. Do not rely on a plain K8s namespace label alone.

**EDA UI:** fabric-dc2 may not appear meaningfully until onboarding kit CRs exist. Refresh after apply or edactl.

**You do not hand-create** NodeProfile, NodeUser, Init, or IP pools — namespace instantiation (EDA Namespace CR or edactl namespace bootstrap create) copies them from the template namespace. The only post-instantiation edit in this lab is the **NodeUser patch** below so imported TopoNodes match SSH bindings.

**Patch NodeUser** so imported TopoNodes (label eda.nokia.com/source=netbox from your NetBox device tags) match SSH/credential bindings:

    kubectl patch nodeuser admin -n fabric-dc2 --type=json -p='[
      {"op":"add","path":"/spec/groupBindings/-","value":{
        "groups":["sudo"],
        "nodeSelector":["eda.nokia.com/source=netbox"]
      }}
    ]'

**Pass:** kubectl get nodeprofiles -n fabric-dc2 returns at least one profile; NODE_PROFILE printed for use

### 5.3 NetBox prerequisites (fabric-dc2)

#### 5.3.1 Catalog objects (verify — usually already seeded)

If you already ran nb-seed-eda-catalog.py, these already exist in NetBox. Confirm in the UI; re-run the seed script if anything is missing.

| Object       | NetBox UI path           | Lab value                 | Needed for Mode B                  |
|--------------|--------------------------|---------------------------|------------------------------------|
| Manufacturer | DCIM → Manufacturers     | Nokia                     | Yes                                |
| Device type  | DCIM → Device Types      | 7220 IXR-D3L, 7220 IXR-D4 | Yes — device script looks up types |
| Platform     | DCIM → Platforms         | srl                       | Yes                                |
| Device role  | DCIM → Device Roles      | leaf, spine               | Yes                                |
| Region       | Tenancy → Regions        | region-3                  | Yes — assign to site               |
| Tenant       | Tenancy → Tenants        | tenant-c                  | Yes                                |
| API token    | Admin → API Tokens → Add | One token (reuse Mode A)  | Yes                                |

**API token (if you do not already have one from Mode A):**

| Field             | Value                                                                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description**   | e.g. EDA lab                                                                                                                                              |
| **Write enabled** | Yes                                                                                                                                                       |
| **Permissions**   | Grant **write** on DCIM (Device, Interface, Cable, Site), IPAM (Prefix, VLAN Group, ASN Range, IP Address, VLAN, ASN), and **Extras** (Tag, Custom Field) |

Copy the token once — it goes in secrets-fabric-dc2.yaml → apiToken.

#### 5.3.2 Create region, tenant, and site in NetBox

**NetBox UI only** — Tenancy and DCIM menus.

**Example — Region**

1.  **Tenancy → Regions → Add**

2.  Name: region-3

3.  **Create**

**Example — Tenant**

1.  **Tenancy → Tenants → Add**

2.  Name: tenant-c

3.  **Create**

**Example — Site** (must match ApplyTopology.spec.siteName)

1.  **DCIM → Sites → Add**

2.  **Name:** fabric-dc2

3.  **Status:** Planned

4.  **Region:** region-3

5.  **Tenant:** tenant-c

6.  **Tags:** leave empty — **do not** add EDAManaged

7.  **Create**

| \#  | NetBox UI path              | Lab value           | Notes                                                                       |
|-----|-----------------------------|---------------------|-----------------------------------------------------------------------------|
| 1   | **Tenancy → Regions → Add** | Name region-3       | Skip if catalog seed already created it                                     |
| 2   | **Tenancy → Tenants → Add** | Name tenant-c       | Skip if catalog seed already created it                                     |
| 3   | **DCIM → Sites → Add**      | Name **fabric-dc2** | Region region-3, Tenant tenant-c, Status **planned**; **no** EDAManaged tag |

Site name must match ApplyTopology.spec.siteName (fabric-dc2). The device script can get_or_create the site if you skip step 3 — creating it here assigns region/tenant in the UI first.

#### 5.3.3 Create webhook in NetBox

**NetBox UI only** — **Customization → Webhooks → Add** (NetBox 4.x: **Operations → Integrations → Webhooks → Add**)

**Full example:**

| Field                 | Value                                                                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**              | EDA fabric-dc2                                                                                                                                                              |
| **Enabled**           | ✓                                                                                                                                                                           |
| **URL**               | https://eda-api.eda-system.svc.cluster.local:443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox                                                                         |
| **HTTP method**       | POST                                                                                                                                                                        |
| **HTTP content type** | application/json                                                                                                                                                            |
| **Secret**            | e.g. fabric-dc2-wh-secret-change-me — **generate a new random string**; copy for secrets-fabric-dc2.yaml → signatureKey ([§5.4](#Xf05e880280a4a5b3338c39b84f7bb0b25917f82)) |
| **SSL verification**  | Disabled (lab self-signed)                                                                                                                                                  |
| **CA file path**      | (empty)                                                                                                                                                                     |

URL must be reachable **from the NetBox pod** (not browser localhost):

    kubectl get svc eda-api -n eda-system
    # Typical in-cluster URL:
    # https://eda-api.eda-system.svc.cluster.local:443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox

Do **not** reuse the clab webhook URL or signing secret — each EDA namespace needs its own webhook + secret.

#### 5.3.4 Create event rule in NetBox

**NetBox UI only** — **Customization → Event Rules → Add** (NetBox 4.x: **Operations → Integrations → Event Rules → Add**)

**Full example:**

| Field            | Value                                            |
|------------------|--------------------------------------------------|
| **Name**         | EDA fabric-dc2 events                            |
| **Enabled**      | ✓                                                |
| **Event types**  | Object created · Object updated · Object deleted |
| **Action type**  | Webhook                                          |
| **Webhook**      | EDA fabric-dc2                                   |
| **Object types** | Enable all rows below                            |

| Object type (NetBox UI) | Topology | Allocations |
|-------------------------|----------|-------------|
| DCIM → Cable            | Optional | —           |
| DCIM → Device           | Optional | —           |
| DCIM → Device Type      | Optional | —           |
| DCIM → Site             | Optional | —           |
| IPAM → ASN              | —        | **Yes**     |
| IPAM → ASN Range        | —        | **Yes**     |
| IPAM → IP Address       | —        | **Yes**     |
| IPAM → Prefix           | —        | **Yes**     |
| IPAM → VLAN             | —        | **Yes**     |
| IPAM → VLAN Group       | —        | **Yes**     |

For the full lab (topology + optional allocations), enable **all** types — same object set as Mode A; only the webhook URL targets fabric-dc2.

#### 5.3.5 Not needed until later

| Item                              | When                                                                      |
|-----------------------------------|---------------------------------------------------------------------------|
| Devices, interfaces, cables       | [§5.5](#Xce1083a30d7f944425b8b6bdce7076a55b765fa) — nb-test-fabric-dc2.py |
| VLAN groups, prefixes, ASN ranges | [§5.7](#X69c0b58b636e24406d804afba17593991378e2a) — optional              |
| EDAManaged on site or devices     | **Never** on Mode B design objects                                        |

#### 5.3.6 Global setting (one-time, NetBox UI or admin)

Confirm ENFORCE_GLOBAL_UNIQUE=false ([§8.3](#Xc20f2c56567c9b18f710108fbbe1fa5aa27d0d8)).

**Pass:** Site fabric-dc2 visible in NetBox UI (no EDAManaged); webhook + event rule saved; webhook **Secret** and API token copied ready for [§5.4](#Xf05e880280a4a5b3338c39b84f7bb0b25917f82).

### 5.4 Secrets + Instance CR (fabric-dc2)

#### 5.4.1 secrets-fabric-dc2.yaml

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

#### 5.4.2 instance-fabric-dc2.yaml

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
    kubectl apply -f secrets-fabric-dc2.yaml
    kubectl apply -f instance-fabric-dc2.yaml
    kubectl get instance.netbox.eda.nokia.com netbox -n fabric-dc2 -o jsonpath='reachable={.status.reachable}{"\n"}'

### 5.5 NetBox DCIM modelling — devices, interfaces, cables

After [§5.4](#Xf05e880280a4a5b3338c39b84f7bb0b25917f82) (Instance reachable). Creates leaf/spine devices **in NetBox** — via the script below (run inside NetBox pod) or manually in the NetBox UI.

#### 5.5.1 Topology summary

Django ORM script executed **inside the NetBox pod** (manage.py shell). Creates devices, interfaces, and cables at site fabric-dc2. Site may already exist from [§5.3.2](#Xc84e6688adb5391ee329353f3d96b874913c13a); script uses get_or_create.

| Role  | Names                      | Device type  | Uplinks                                            |
|-------|----------------------------|--------------|----------------------------------------------------|
| Leaf  | leaf-dc2-01 … leaf-dc2-04  | 7220 IXR-D3L | ethernet-1/49 → spine-01, ethernet-1/50 → spine-02 |
| Spine | spine-dc2-01, spine-dc2-02 | 7220 IXR-D4  | ethernet-1/1–ethernet-1/4 (one per leaf link)      |

#### 5.5.2 Prepare the script

Copy scripts/nb-test-fabric-dc2.py to manifests/nb-test-fabric-dc2.py and **edit NODE_PROFILE** to match [§5.2](#X56a525b261cd0ea68478e0fd4da6a41a11274cf) NodeProfile from namespace instantiation:

    kubectl get nodeprofiles -n fabric-dc2 -o jsonpath='{.items[0].metadata.name}{"\n"}'

| Setting      | Requirement                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SITE         | fabric-dc2 — must match ApplyTopology.spec.siteName                                                                                                                                                                                         |
| NODE_PROFILE | Must match a NodeProfile in fabric-dc2                                                                                                                                                                                                      |
| Device tags  | eda.nokia.com/node-profile=…, eda.nokia.com/role=leaf or spine, site=fabric-dc2 — **do not** tag devices with eda.nokia.com/source=netbox (EDA sets that label on TopoNodes; putting it on NetBox device tags causes ApplyTopology to fail) |
| Cable tag    | eda.nokia.com/role=interSwitch on each ISL                                                                                                                                                                                                  |
| Cable type   | **Optional** — leave unset (same as Mode A sync). Not used by ApplyTopology; NetBox bookkeeping only                                                                                                                                        |

Script is idempotent — safe to re-run.

#### 5.5.3 Run the script

After saving the script to disk, copy into the NetBox pod and execute:

    # From WSL — lab file path
    SCRIPT=../manifests/nb-test-fabric-dc2.py

    POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
    kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-fabric-dc2.py"
    kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-fabric-dc2.py').read())"

**Pass:** NetBox UI → DCIM → Devices at site fabric-dc2 shows **6 devices**, **8 cables**; no EDAManaged tag on site or devices.

#### 5.5.4 Manual alternative (NetBox UI)

Create each device in **DCIM → Devices** with platform srl, device types above, and tags:

    eda.nokia.com/node-profile=<NodeProfile-from-§5.2>
    eda.nokia.com/role=leaf
    site=fabric-dc2

Add interfaces and cables in DCIM. Optional cable tag: eda.nokia.com/role=interSwitch. Cable **type** is optional in NetBox — leave blank unless you want DCIM documentation; it is not imported into EDA. Plain string tags without = are ignored by ApplyTopology except site=\<siteName\>.

**Do not** add eda.nokia.com/source=netbox to device tags. EDA applies that label internally on imported TopoNodes; NetBox device tags with that key are copied to TopoNode labels and rejected by the CE.

### 5.6 ApplyTopology CR

**File: applytopology-fabric-dc2.yaml**

    apiVersion: netbox.eda.nokia.com/v1alpha1
    kind: ApplyTopology
    metadata:
      name: import-fabric-dc2
      namespace: fabric-dc2
    spec:
      instanceName: netbox
      siteName: fabric-dc2
      deviceTags: []
    kubectl apply -f applytopology-fabric-dc2.yaml
    kubectl get applytopology import-fabric-dc2 -n fabric-dc2 -o yaml
    kubectl get toponodes -n fabric-dc2

**Pass:** TopoNode / TopoLink count matches NetBox site (6 TopoNodes, 8 TopoLinks for this lab).

Hands-on walkthrough and reference detail are in the full technical documentation.

### 5.7 NetBox allocation pools (fabric-dc2)

**Optional step 6** in [§5.1](#Xc719e00ed9ce0b2b0576dca6ea38b4056582a83). Requires [§5.4](#Xf05e880280a4a5b3338c39b84f7bb0b25917f82) (Instance reachable) and IPAM object types enabled in the event rule ([§5.3.4](#Xd225876499b0239d3068f1e1f611ffb5c625337)). Allocation pool tags can be pre-created — see below.

Create tagged IPAM objects in NetBox **before** kubectl apply -f allocations-fabric-dc2.yaml. Tags are **plain strings** (not key=value device tags). Theory and CR matrix: [§6.3](#X3737d0a92ed47a6e83651f30fc15c4019ff0dd0).

If you create the pools through the NetBox UI, create the tags first — the script below creates them for you:

1.  **Customization → Tags → Add** (repeat for each)

| Tag name                | Used on            |
|-------------------------|--------------------|
| eda-fabric-dc2-vlan     | VLAN Group         |
| eda-fabric-dc2-asn      | ASN Range          |
| eda-fabric-dc2-systemip | Prefix (Active)    |
| eda-fabric-dc2-mgmt     | Prefix (Active)    |
| eda-fabric-dc2-isl      | Prefix (Container) |

#### 5.7.0 Create all pools at once (script)

**File:** nb-test-allocation-pools-fabric-dc2.py. Creates all five NetBox objects + tags in one run:

    SCRIPT=../scripts/nb-test-allocation-pools-fabric-dc2.py
    POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
    kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
    kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-fabric-dc2.py').read())"

Then apply EDA side ([§5.7.6](#X52bda211813cfe30511d3cac016630961c9e65d)).

#### 5.7.1 VLAN pool (type: vlan)

**NetBox UI — create VLAN Group**

1.  **IPAM → VLAN Groups → Add**

2.  **Name:** fabric-dc2-vlans

3.  **Slug:** fabric-dc2-vlans

4.  **Minimum VID / Maximum VID:** 100 / 199 (or add VID ranges after create)

5.  **Tags:** eda-fabric-dc2-vlan (create the tag if missing)

6.  **Create**

**EDA Allocation CR** (nb-fabric-dc2-vlan-pool → IndexAllocationPool):

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

#### 5.7.2 ASN pool (type: asn)

**NetBox UI — create ASN Range**

1.  **IPAM → ASN Ranges → Add**

2.  **Name:** fabric-dc2-asns

3.  **RIR:** Private

4.  **Start ASN / End ASN:** 4200000000 / 4200000999

5.  **Tags:** eda-fabric-dc2-asn

6.  **Create**

**EDA Allocation CR** (nb-fabric-dc2-asn-pool → IndexAllocationPool):

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

#### 5.7.3 System IP pool (type: ip-address)

**NetBox UI — create Prefix (Active)**

1.  **IPAM → Prefixes → Add**

2.  **Prefix:** 10.0.1.0/24

3.  **Status:** **Active** (required — not Container)

4.  **Tags:** eda-fabric-dc2-systemip

5.  **Create**

**EDA Allocation CR** (nb-fabric-dc2-systemip → IPAllocationPool):

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

#### 5.7.4 Management IP pool (type: ip-in-subnet)

**NetBox UI — create Prefix (Active)**

1.  **IPAM → Prefixes → Add**

2.  **Prefix:** 192.168.100.0/24

3.  **Status:** **Active**

4.  **Tags:** eda-fabric-dc2-mgmt

5.  **Create**

**EDA Allocation CR** (nb-fabric-dc2-mgmt → IPInSubnetAllocationPool):

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

#### 5.7.5 ISL subnet pool (type: subnet)

Point-to-point ISL links use **/31 subnets** (RFC 3021). Set spec.subnetLength: 31 on the Allocation CR.

**NetBox UI — create Prefix (Container)**

1.  **IPAM → Prefixes → Add**

2.  **Prefix:** 10.255.0.0/16

3.  **Status:** **Container** (required for subnet allocation)

4.  **Tags:** eda-fabric-dc2-isl

5.  **Create**

**EDA Allocation CR** (nb-fabric-dc2-isl → SubnetAllocationPool):

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
      subnetLength: 31

#### 5.7.5a Mode A lab example — IPv6 ISL (clab-3-tier-leaf-spine-dcgw)

Use a **separate** IPv6 container from system/loopback space. In this lab, **do not** use 121::/… for ISL — reserve that range for **system IP** (type: ip-address). ISL IPv6 uses **2005::/64** as the NetBox container; EDA carves **/127** subnets for point-to-point ISLs.

| Item                   | Lab value                                                    |
|------------------------|--------------------------------------------------------------|
| **NetBox prefix**      | 2005::/64                                                    |
| **Status**             | **Container**                                                |
| **Tag**                | eda-clab3tier-isl-ipv6                                       |
| **Allocation CR name** | eda-isl-ipv6 (matches Fabric.spec.interSwitchLinks.poolIPv6) |
| **spec.type**          | subnet                                                       |
| **spec.subnetLength**  | 127                                                          |
| **EDA pool CRD**       | SubnetAllocationPool                                         |

**NetBox — script or UI**

    # All clab3tier pools (v4 + v6 ISL): scripts/nb-test-allocation-pools-clab3tier.py
    # IPv6 ISL only: scripts/nb-add-clab3tier-isl-ipv6-only.py
    POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
    kubectl cp scripts/nb-add-clab3tier-isl-ipv6-only.py "netbox/${POD}:/tmp/nb-add-isl-v6.py"
    kubectl exec -n netbox "$POD" -- /opt/netbox/venv/bin/python /tmp/nb-add-isl-v6.py

**EDA — excerpt from manifests/allocations-clab-3-tier-leaf-spine-dcgw.yaml:**

    apiVersion: netbox.eda.nokia.com/v1alpha1
    kind: Allocation
    metadata:
      name: eda-isl-ipv6
      namespace: clab-3-tier-leaf-spine-dcgw
    spec:
      enabled: true
      instance: netbox
      tags: [eda-clab3tier-isl-ipv6]
      type: subnet
      subnetLength: 127

**Verify**

    kubectl get allocation eda-isl-ipv6 -n clab-3-tier-leaf-spine-dcgw \
      -o jsonpath='matched={.status.matchedPrefixes}{"\n"}'
    kubectl get subnetallocationpool eda-isl-ipv6 -n clab-3-tier-leaf-spine-dcgw

Child /127 prefixes appear in NetBox **after** the fabric consumes the pool (underlay ISL provisioning), not when the container prefix is first matched.

**Bootstrap vs NetBox:** Namespace instantiation may already create a SubnetAllocationPool named eda-isl-ipv6 **without** a NetBox Allocation CR. That pool is **onboarding kit**, not IPAM-backed. To sync with NetBox, create the tagged prefix above, apply the Allocation CR, confirm status.matchedPrefixes, then remove a duplicate bootstrap pool only if the controller does not adopt it — see [§7.1.1](#Xc9e009074bdeda6879241181d8a78c1dd75f6ec).

#### 5.7.6 Apply all Allocation CRs

**File: allocations-fabric-dc2.yaml** (multi-document — combines §5.7.1–§5.7.5):

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
      subnetLength: 31
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
    kubectl apply -f allocations-fabric-dc2.yaml
    kubectl get allocation -n fabric-dc2

#### 5.7.7 Verify all pools

    kubectl get allocation -n fabric-dc2
    kubectl get allocation nb-fabric-dc2-vlan-pool -n fabric-dc2 -o jsonpath='matched={.status.matchedPrefixes}{"\n"}'
    kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n fabric-dc2

| Allocation CR           | EDA pool kind            | Pass                            |
|-------------------------|--------------------------|---------------------------------|
| nb-fabric-dc2-vlan-pool | IndexAllocationPool      | status shows matched VLAN group |
| nb-fabric-dc2-asn-pool  | IndexAllocationPool      | matched ASN range               |
| nb-fabric-dc2-systemip  | IPAllocationPool         | matched Active prefix           |
| nb-fabric-dc2-mgmt      | IPInSubnetAllocationPool | matched Active prefix           |
| nb-fabric-dc2-isl       | SubnetAllocationPool     | matched Container prefix        |

The hands-on walkthrough is in the full technical documentation.

### 5.8 Mode A vs Mode B (summary)

|                      | Mode A                   | Mode B                          |
|----------------------|--------------------------|---------------------------------|
| **Source of truth**  | EDA TopoNode / TopoLink  | NetBox Site / Devices / Cables  |
| **NetBox Site**      | EDA creates on sync      | **You create** — not EDAManaged |
| **sync.enabled**     | true                     | false                           |
| **Import to EDA**    | Containerlab / workflows | **ApplyTopology**               |
| **DCIM token perms** | create / update / delete | read (import only)              |

| Mode                                         | EDAManaged on DCIM source?         | EDAManaged on allocated IPAM?        |
|----------------------------------------------|------------------------------------|--------------------------------------|
| **A — EDA-managed** (sync.enabled: true)     | Yes — all synced Site/Device/Cable | Yes — when EDA hands out pool values |
| **B — NetBox-managed** (sync.enabled: false) | **No** on your design site/devices | Yes — when EDA hands out pool values |

**Rule:** Never run ApplyTopology against a site that EDA already owns (EDAManaged). Never enable sync.enabled on a namespace whose NetBox site is your design source.

# Part III — IPAM and Multi-Fabric Design

## 6. Allocations — IPAM pools

This section covers architecture and CR reference – we are using Mode B namespace for reference.

IPAM allocation pools are **orthogonal** to DCIM Mode A and Mode B . Same Instance CR; pool tags on NetBox IPAM objects.

### 6.1 Architecture — one Instance per EDA namespace

A single NetBox **server** can serve many EDA namespaces. Each namespace gets its **own** integration binding:

| NetBox (one server)            | Webhook path pattern                 |
|--------------------------------|--------------------------------------|
| DCIM sites + tagged IPAM pools | /eda/\<namespace\>/netbox per fabric |

| EDA namespace            | Instance            | TopoNodes        | Allocation CRs         |
|--------------------------|---------------------|------------------|------------------------|
| clab-srl-leaf-spine-dcgw | sync.enabled: true  | EDA-owned (clab) | IndexAllocationPool, … |
| fabric-dc2               | sync.enabled: false | NetBox-imported  | IPAllocationPool, …    |

**Per namespace you deploy:**

1.  Secrets: netbox-api-token, netbox-webhook-signature (lab reuses one API token; webhook secret is always per namespace)

2.  Instance CR

3.  NetBox webhook URL: https://\<EDA\>:9443/core/httpproxy/v1/netbox/webhook/\<NAMESPACE\>/\<INSTANCE_NAME\>

4.  NetBox Event Rule (can be one rule covering all object types — webhook URL differs per namespace)

5.  Zero or more Allocation CRs

6.  Optional: ApplyTopology / ApplyAllocation workflows

Instance and Allocation **must** live in the **same namespace**. The Allocation controller resolves spec.instance by name within that namespace only.

### 6.2 Instance CR — full options

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

| Field                     | Affects topology?                      | Affects allocations?                           |
|---------------------------|----------------------------------------|------------------------------------------------|
| sync.enabled              | **Yes** — EDA→NetBox device/cable push | **No**                                         |
| sync.region / sync.tenant | Yes (synced Site metadata)             | No                                             |
| disableWebhook            | No (sync is controller-driven)         | **Yes** — use ApplyAllocation manually if true |
| url, apiToken, TLS        | Both                                   | Both                                           |

**Status fields:** reachable, errorReason, lastChecked

### 6.3 Allocation CR — all pool types

Allocation maps **tagged NetBox IPAM objects** → **EDA allocation pools**. Matching is by **plain string tags** on IPAM objects (not key=value device tags).

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
      # subnetLength: 31              # required for type: subnet only (ISL point-to-point /31)
      description: ""                 # optional

#### Complete type matrix

| spec.type    | NetBox source | Prefix status | EDA pool CRD             | Typical use                       |
|--------------|---------------|---------------|--------------------------|-----------------------------------|
| ip-address   | Prefix        | **Active**    | IPAllocationPool         | System / loopback IPs             |
| ip-in-subnet | Prefix        | **Active**    | IPInSubnetAllocationPool | Management IP (address + mask)    |
| subnet       | Prefix        | **Container** | SubnetAllocationPool     | ISL / point-to-point link subnets |
| asn          | ASN Range     | n/a           | IndexAllocationPool      | BGP private ASNs                  |
| vlan         | VLAN Group    | n/a           | IndexAllocationPool      | VLAN IDs                          |

#### ASN allocation and sync.enabled (lab finding)

VLAN and prefix-based pools (vlan, ip-address, ip-in-subnet, subnet) reconcile from **tagged NetBox IPAM objects only** — they work in both Mode A and Mode B.

**ASN behaviour is different in App version 4.0.3.** The eda-netbox allocation reconciler seems to require the namespace site to be in its internal **synced-site cache**. That cache is populated when Instance.spec.sync.enabled: true (Mode A DCIM sync). With sync.enabled: false (Mode B), even a correctly tagged ASN range in NetBox and a healthy ApplyTopology import will log:

    site not yet synced ... sync.enabled=false

| Mode                                          | sync.enabled | VLAN / IP pools | ASN pool                          |
|-----------------------------------------------|--------------|-----------------|-----------------------------------|
| A — EDA-managed (clab-3-tier-leaf-spine-dcgw) | true         | Matched         | **Matched**                       |
| B — NetBox-managed (fabric-dc2)               | false        | Matched         | **Blocked** (Under investigation) |

Sharing the same Instance name (netbox) across namespaces — each namespace resolves spec.instance locally and overlapping ASN numeric ranges is suppotred — matching is by **tag**.

In this release combination - Mode B lab: expect **4/5** Allocation CRs matched; use Mode A namespace for full ASN pool testing until Nokia documents a Mode B workaround.

**Tag rule:** one distinct tag per pool mapping. Multiple NetBox objects with the same tag can feed one Allocation (status shows matchedPrefixes / matched ranges).

**Example — five pools in one namespace (fabric-dc2 tags per [§8.1](#Xfc815d572f9671d4de3122f480daaf02418e3cd)):**

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
      subnetLength: 31

#### NetBox IPAM setup (summary)

| spec.type    | NetBox object | Tag (fabric-dc2)        | Status / range                   |
|--------------|---------------|-------------------------|----------------------------------|
| vlan         | VLAN Group    | eda-fabric-dc2-vlan     | VID range e.g. 100–199           |
| asn          | ASN Range     | eda-fabric-dc2-asn      | e.g. 4200000000–4200000999       |
| ip-address   | Prefix        | eda-fabric-dc2-systemip | **Active** e.g. 10.0.1.0/24      |
| ip-in-subnet | Prefix        | eda-fabric-dc2-mgmt     | **Active** e.g. 192.168.100.0/24 |
| subnet       | Prefix        | eda-fabric-dc2-isl      | **Container** e.g. 10.255.0.0/16 |

Full NetBox UI steps and per-pool examples:

IPAM objects are **not scoped to a DCIM site**. Separation across namespaces is by **tag naming**, not site membership.

#### Trigger and verify

**File: applyallocation-refresh-fabric-dc2.yaml** (on-demand reconcile — repeat per pool name)

    apiVersion: netbox.eda.nokia.com/v1alpha1
    kind: ApplyAllocation
    metadata:
      name: refresh-fabric-dc2-vlan
      namespace: fabric-dc2
    spec:
      allocation: nb-fabric-dc2-vlan-pool
    kubectl apply -f applyallocation-refresh-fabric-dc2.yaml
    kubectl get instance,allocation -n fabric-dc2
    kubectl get allocation nb-fabric-dc2-vlan-pool -n fabric-dc2 -o yaml
    kubectl get ipallocationpools,subnetallocationpools,indexallocationpools -n fabric-dc2

**When EDA consumes a value** (Fabric app, onboarding, etc.):

-   Individual IP / VLAN / ASN is **created in NetBox IPAM**

-   Object gets **EDAManaged** tag + EDA custom fields (allocation owner, requesting CR)

-   Parent pool prefix / VLAN group / ASN range stays **your** object — not fully taken over

### 6.4 Lab examples — all pool types (fabric-dc2)

**Canonical walkthrough:** This subsection is a short index; full NetBox UI steps, per-pool Allocation YAML, and allocations-fabric-dc2.yaml are in the Git Repo.

Create tagged IPAM objects in NetBox **before** kubectl apply -f allocations-fabric-dc2.yaml. Tags are **plain strings** (not key=value device tags).

#### 6.4.0 Run all pools (script)

**File:** nb-test-allocation-pools-fabric-dc2.py. Creates all five objects + tags in one run:

    SCRIPT=../scripts/nb-test-allocation-pools-fabric-dc2.py
    POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
    kubectl cp "$SCRIPT" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
    kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-fabric-dc2.py').read())"

Then apply EDA side:

    kubectl apply -f allocations-fabric-dc2.yaml
    kubectl get allocation -n fabric-dc2

#### 6.4.1 VLAN (type: vlan)

| Item              | Lab value                                                                    |
|-------------------|------------------------------------------------------------------------------|
| **NetBox UI**     | IPAM → VLAN Groups → Add                                                     |
| **Name**          | fabric-dc2-vlans                                                             |
| **VID ranges**    | 100–199                                                                      |
| **Tag**           | eda-fabric-dc2-vlan (Extras → Tags → Add if missing; assign on VLAN Group)   |
| **Allocation CR** | nb-fabric-dc2-vlan-pool, spec.type: vlan, spec.tags: \[eda-fabric-dc2-vlan\] |
| **EDA pool CRD**  | IndexAllocationPool                                                          |

#### 6.4.2 ASN (type: asn)

| Item              | Lab value                              |
|-------------------|----------------------------------------|
| **NetBox UI**     | IPAM → ASN Ranges → Add                |
| **Name**          | fabric-dc2-asns                        |
| **RIR**           | Private                                |
| **Range**         | 4200000000 – 4200000999                |
| **Tag**           | eda-fabric-dc2-asn                     |
| **Allocation CR** | nb-fabric-dc2-asn-pool, spec.type: asn |
| **EDA pool CRD**  | IndexAllocationPool                    |

#### 6.4.3 System IP (type: ip-address)

| Item              | Lab value                                     |
|-------------------|-----------------------------------------------|
| **NetBox UI**     | IPAM → Prefixes → Add                         |
| **Prefix**        | 10.0.1.0/24                                   |
| **Status**        | **Active** (required — not Container)         |
| **Tag**           | eda-fabric-dc2-systemip                       |
| **Allocation CR** | nb-fabric-dc2-systemip, spec.type: ip-address |
| **EDA pool CRD**  | IPAllocationPool                              |

#### 6.4.4 Management IP (type: ip-in-subnet)

| Item              | Lab value                                   |
|-------------------|---------------------------------------------|
| **NetBox UI**     | IPAM → Prefixes → Add                       |
| **Prefix**        | 192.168.100.0/24                            |
| **Status**        | **Active**                                  |
| **Tag**           | eda-fabric-dc2-mgmt                         |
| **Allocation CR** | nb-fabric-dc2-mgmt, spec.type: ip-in-subnet |
| **EDA pool CRD**  | IPInSubnetAllocationPool                    |

#### 6.4.5 ISL subnet (type: subnet)

Point-to-point ISL links use **/31 subnets**. The Allocation CR sets spec.subnetLength: 31.

| Item              | Lab value                                                   |
|-------------------|-------------------------------------------------------------|
| **NetBox UI**     | IPAM → Prefixes → Add                                       |
| **Prefix**        | 10.255.0.0/16                                               |
| **Status**        | **Container** (required for subnet allocation)              |
| **Tag**           | eda-fabric-dc2-isl                                          |
| **Allocation CR** | nb-fabric-dc2-isl, spec.type: subnet, spec.subnetLength: 31 |
| **EDA pool CRD**  | SubnetAllocationPool                                        |

#### 6.4.6 Verify all pools

    kubectl get allocation -n fabric-dc2
    kubectl get allocation nb-fabric-dc2-vlan-pool -n fabric-dc2 -o jsonpath='matched={.status.matchedPrefixes}{"\n"}'
    kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n fabric-dc2

| Allocation CR           | EDA pool kind            | Pass                            |
|-------------------------|--------------------------|---------------------------------|
| nb-fabric-dc2-vlan-pool | IndexAllocationPool      | status shows matched VLAN group |
| nb-fabric-dc2-asn-pool  | IndexAllocationPool      | matched ASN range               |
| nb-fabric-dc2-systemip  | IPAllocationPool         | matched Active prefix           |
| nb-fabric-dc2-mgmt      | IPInSubnetAllocationPool | matched Active prefix           |
| nb-fabric-dc2-isl       | SubnetAllocationPool     | matched Container prefix        |

#### 6.4.7 Mode A — clab-3-tier-leaf-spine-dcgw (six Allocation CRs)

File: manifests/allocations-clab-3-tier-leaf-spine-dcgw.yaml. Seed NetBox IPAM with scripts/nb-test-allocation-pools-clab3tier.py (or nb-add-clab3tier-isl-ipv6-only.py for IPv6 ISL only). Full walkthrough:

| Allocation CR          | type         | NetBox tag             | Prefix / object         | subnetLength |
|------------------------|--------------|------------------------|-------------------------|--------------|
| nb-clab3tier-systemip  | ip-address   | eda-clab3tier-systemip | 10.0.10.0/24 Active     | —            |
| nb-clab3tier-mgmt      | ip-in-subnet | eda-clab3tier-mgmt     | 192.168.110.0/24 Active | —            |
| nb-clab3tier-isl       | subnet       | eda-clab3tier-isl      | 10.254.0.0/16 Container | 31           |
| eda-isl-ipv6           | subnet       | eda-clab3tier-isl-ipv6 | 2005::/64 Container     | 127          |
| nb-clab3tier-asn-pool  | asn          | eda-clab3tier-asn      | ASN range               | —            |
| nb-clab3tier-vlan-pool | vlan         | eda-clab3tier-vlan     | VLAN group              | —            |

## 7. Decoupling topology from allocations

### 7.1 Two paths, one namespace

**EDA namespace fabric-dc2 — two independent paths:**

| Path                   | Trigger        | EDA objects                                                 | sync.enabled                      |
|------------------------|----------------|-------------------------------------------------------------|-----------------------------------|
| **Topology (DCIM)**    | ApplyTopology  | TopoNode, Interface, TopoLink                               | false (no EDA→NetBox device push) |
| **Allocations (IPAM)** | Allocation CRs | IPAllocationPool, SubnetAllocationPool, IndexAllocationPool | Independent of sync               |

| NetBox source (Mode B)                                  | Consumed by    |
|---------------------------------------------------------|----------------|
| DCIM — Site, Devices, Cables (your design)              | ApplyTopology  |
| IPAM — Prefixes, VLAN Groups, ASN Ranges (tagged pools) | Allocation CRs |

| Dimension                      | Topology (DCIM)                               | Allocations (IPAM)                    |
|--------------------------------|-----------------------------------------------|---------------------------------------|
| **Scoped by**                  | NetBox **site** (ApplyTopology.spec.siteName) | **Tags** on IPAM objects              |
| **Site association**           | Required for devices/cables                   | **Not required**                      |
| **EDA workflow**               | ApplyTopology                                 | Allocation + ApplyAllocation          |
| **Controlled by sync.enabled** | **Yes** (EDA→NetBox push)                     | **No**                                |
| **Import direction**           | NetBox → EDA (when managed)                   | NetBox pool defs → EDA pools          |
| **Export direction**           | EDA → NetBox (when sync on)                   | EDA allocations → NetBox IPAM objects |
| **EDAManaged on source**       | Mode A: all synced DCIM                       | Never on pool definitions             |
| **EDAManaged on consumption**  | N/A                                           | Individual allocated IPs/VLANs/ASNs   |

### 7.1.1 Bootstrap allocation pools vs NetBox-backed pools

Two different mechanisms can create **SubnetAllocationPool** (and other pool kinds) in an EDA namespace:

| Source                  | How it appears                                                   | Allocation CR (netbox.eda.nokia.com)? | Prefix / range in NetBox?    |
|-------------------------|------------------------------------------------------------------|---------------------------------------|------------------------------|
| **Namespace bootstrap** | Copied from template namespace (eda.nokia.com/bootstrap: "true") | **No**                                | **No**                       |
| **NetBox app**          | Allocation reconciles tagged IPAM → pool                         | **Yes**                               | **Yes** (parent pool object) |

Webhooks do **not** create pool definitions; they refresh reconciliation after IPAM changes. The **Allocation CR** is the integration object for NetBox-backed pools.

**Lab migration (e.g. IPv6 ISL eda-isl-ipv6):**

1.  Create NetBox container prefix (2005::/64, tag eda-clab3tier-isl-ipv6).

2.  Apply Allocation eda-isl-ipv6 with subnetLength: 127.

3.  Confirm status.matchedPrefixes on the Allocation.

4.  Only then remove a **bootstrap-only** SubnetAllocationPool with the same name if it never links to NetBox (avoid deleting a pool already owned by a matched Allocation).

### 7.2 Combined deployment patterns

#### Pattern 1 — Clab / EDA-managed fabric (lab default)

| Component             | Setting                                       |
|-----------------------|-----------------------------------------------|
| Namespace             | clab-srl-leaf-spine-dcgw                      |
| Instance.sync.enabled | true                                          |
| Topology              | Born in EDA; mirrored to NetBox               |
| Allocations           | Optional Allocation CRs for VLAN/ASN/IP pools |
| NetBox DCIM           | Read-only mirror (EDAManaged)                 |
| NetBox IPAM           | Tagged pools + EDAManaged on consumed values  |

#### Pattern 2 — Greenfield planned fabric (NetBox design source)

| Component             | Setting                                                    |
|-----------------------|------------------------------------------------------------|
| Namespace             | fabric-dc2 (dedicated)                                     |
| Instance.sync.enabled | false                                                      |
| Topology              | Modelled in NetBox → ApplyTopology                         |
| Allocations           | Allocation CRs + IPAM pools (can pre-exist before devices) |
| NetBox DCIM           | Your source of truth (no EDAManaged)                       |
| NetBox IPAM           | Pools untagged/EDAManaged only on allocations              |

#### Pattern 3 — Hybrid (common in production)

-   **NetBox-managed** planned site imported to EDA (sync.enabled: false)

-   **Shared IPAM pools** tagged per namespace (e.g. eda-fabric-dc2-vlan vs eda-clab-vlan)

-   Same NetBox server, **separate** Instance + webhook per namespace

-   Fabric / Init / NodeProfile reference allocation pools **in their namespace**

### 7.3 What is shared vs isolated

| Shared across namespaces (lab)                                                                    | Per namespace (always)                                          |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| NetBox API token **value** (one token in NetBox UI, same literal in each netbox-api-token secret) | K8s Secret objects (netbox-api-token, netbox-webhook-signature) |
| NetBox server URL (Instance.spec.url)                                                             | Webhook URL path (.../webhook/\<namespace\>/netbox)             |
|                                                                                                   | Webhook signatureKey (unique signing secret)                    |
|                                                                                                   | Instance CR, sync.region / sync.tenant                          |

### 7.4 Recommended build order

1.  Create EDA namespace via namespace instantiation — **edactl namespace bootstrap create** or EDA Namespace CR (NodeProfile, NodeUser, Init, pools)

2.  Secrets + **Instance** + NetBox webhook for **this namespace**

3.  **Allocation CRs** + NetBox IPAM pools (optional but do before Fabric/onboarding)

4.  NetBox DCIM: site, devices, interfaces, cables

5.  **ApplyTopology**

6.  **ApplyAllocation** if webhooks did not reconcile pools

## 8. Multi-namespace conventions and permissions

### 8.1 Webhook URLs and tag naming

**One webhook URL per namespace** — the path includes namespace and Instance name:

Examples (webhook — use address **reachable from NetBox pod**, not browser localhost):

    https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-3-tier-leaf-spine-dcgw/netbox
    https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/clab-srl-leaf-spine-dcgw/netbox
    https://<EDA-WEBHOOK-HOST>:9443/core/httpproxy/v1/netbox/webhook/fabric-dc2/netbox

| Access from                                    | EDA URL                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Your browser** (UI, EDA Explorer)            | https://localhost:9443                                                                                                       |
| **NetBox webhook** (HTTP call from NetBox pod) | https://eda-api.eda-system.svc.cluster.local:443/... or LB IP from kubectl get svc eda-api -n eda-system — **not** localhost |

**Suggested tag naming** to avoid cross-namespace pool collisions (fabric-dc2 lab):

| Namespace                   | VLAN                | ASN                | System IP               | Mgmt IP             | ISL IPv4                                         | ISL IPv6                                                              |
|-----------------------------|---------------------|--------------------|-------------------------|---------------------|--------------------------------------------------|-----------------------------------------------------------------------|
| clab-3-tier-leaf-spine-dcgw | eda-clab3tier-vlan  | eda-clab3tier-asn  | eda-clab3tier-systemip  | eda-clab3tier-mgmt  | eda-clab3tier-isl → 10.254.0.0/16 Container, /31 | eda-clab3tier-isl-ipv6 → 2005::/64 Container, /127; pool eda-isl-ipv6 |
| clab-srl-leaf-spine-dcgw    | eda-clab-vlan       | eda-clab-asn       | eda-clab-systemip       | eda-clab-mgmt       | eda-clab-isl                                     | —                                                                     |
| fabric-dc2                  | eda-fabric-dc2-vlan | eda-fabric-dc2-asn | eda-fabric-dc2-systemip | eda-fabric-dc2-mgmt | eda-fabric-dc2-isl                               | —                                                                     |

Device tags remain key=value (e.g. eda.nokia.com/node-profile=fabric-dc2-srlinux-26.3.1).

### 8.2 API token and webhook secrets (lab convention)

**This lab uses one NetBox API token across all EDA namespaces.** Create a single token in NetBox (Admin → API tokens) with the permissions. Store the **same literal value** in each fabric namespace’s Secret/netbox-api-token. Each namespace still has its **own** Secret object — EDA only reads secrets in the Instance’s namespace.

**Webhook signing secrets are always per namespace.** Each fabric gets a unique signatureKey in Secret/netbox-webhook-signature and a matching NetBox webhook whose URL path includes that namespace. Do not reuse webhook secrets across namespaces.

| Credential               | This lab                                                                 | Alternative (stricter isolation)                                        |
|--------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **NetBox API token**     | One token; duplicate value into each namespace’s netbox-api-token secret | Issue a separate NetBox token per fabric with scoped object permissions |
| **Webhook signatureKey** | Unique per namespace + dedicated NetBox webhook                          | Same — always per namespace                                             |

You can mix approaches: e.g. shared API token for all Mode A clab fabrics, but a dedicated token for a production fabric-dc2 namespace with tighter DCIM scope.

### 8.3 NetBox API permissions

These are the **object permissions** on the NetBox API token referenced by Instance.spec.apiToken. EDA calls the NetBox REST API as that token user.

| Mode                                             | NetBox token needs                                 | Why                                                                               |
|--------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------|
| NetBox-managed import only (sync.enabled: false) | IPAM: read+write (for allocations); DCIM: **read** | ApplyTopology workflow **reads** site/devices/cables; it does not write DCIM back |
| EDA-managed sync (sync.enabled: true)            | IPAM: read+write; DCIM: **create/update/delete**   | Sync **creates and updates** Site, Device, Cable, interfaces in NetBox            |
| Allocations only                                 | IPAM: read+write; DCIM: read                       | Pools and consumed values only                                                    |

Also required: Extras \> Tag, Extras \> Custom Field (for EDAManaged / eda_managed automation).

1.  write); webhook + event rule per namespace ([§5.3](#X08c76b492512916b5f41cbb08b83e6945858d02) for Mode B); ENFORCE_GLOBAL_UNIQUE=false

2.  EDA: namespace + **namespace instantiation** ([§5.2](#X56a525b261cd0ea68478e0fd4da6a41a11274cf) / §3.2)

3.  EDA: secrets + **Instance CR** → verify status.reachable: true ([§4.3](#X7c0b2c60ed3f490ac6b5591e75229dfb1359826) Mode A, [§5.4](#Xf05e880280a4a5b3338c39b84f7bb0b25917f82) Mode B)

4.  EDA: **Allocation** CRs (pool tags must already exist on NetBox IPAM)

5.  NetBox: DCIM site/devices/interfaces/cables (**Mode B only** — [§5.5](#Xce1083a30d7f944425b8b6bdce7076a55b765fa))

6.  EDA: **ApplyTopology** ([§5.6](#X4a3ffe4d06dc00073f385cc04534b893755ccab), Mode B) or let sync run (Mode A)

7.  EDA: **ApplyAllocation** if pools did not reconcile via webhook

# Part IV — Operations and Constraints

## 9. EDA transactions

Individual CR changes use EDA **transactions** (atomic, Git-backed). Distinct from ApplyTopology workflow ops (create / reconcile / replace).

### 9.1 Per-resource operation types

| Op          | Resource exists | Resource missing | Behaviour                        |
|-------------|-----------------|------------------|----------------------------------|
| **create**  | Fails           | Creates          | Strict create only               |
| **modify**  | Updates         | Fails            | In-place update                  |
| **replace** | Full overwrite  | Creates (upsert) | Whole resource replaced          |
| **patch**   | Field update    | Fails            | JSON Patch (RFC 6902)            |
| **delete**  | Deletes         | Fails            | Remove by GVK + name + namespace |

### 9.2 Rule of thumb (NetBox-imported fabric)

| Goal                             | Use                                    |
|----------------------------------|----------------------------------------|
| Patch TopoNode label or npp.mode | modify or patch                        |
| Redefine whole TopoNode          | replace                                |
| Add TopoLink without reconcile   | transaction create or kubectl apply    |
| Add device from NetBox           | ApplyTopology with **Create** workflow |
| Remove one resource              | delete                                 |

### 9.3 Transaction vs topology import

| Mechanism                         | Orphans in namespace            |
|-----------------------------------|---------------------------------|
| Transaction ops on named CRs      | Untouched                       |
| ApplyTopology reconcile           | **Deleted** if not in site spec |
| NetworkTopology operation: create | Untouched                       |

### 9.4 Execution and inspection

-   **dryRun:** validate without pushing to nodes

-   **detailLevel:** basic \| standard \| detailed

-   **CLI:** edactl apply\|replace\|patch\|delete -f ... -d -m "message"

-   **Inspect:** edactl transaction \<id\> cr-change\|node-change

See [EDA transactions documentation](https://docs.eda.dev/latest/user-guide/transactions/) for full API and rollback (Revert / Restore).

## 10. Constraints and anti-patterns

| Mistake                                                | Consequence                                                                                                            |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| One namespace, clab + NetBox planned                   | ApplyTopology **Reconcile** removes TopoNodes not in the NetBox site — live fabric nodes in that namespace are deleted |
| sync.enabled: true on NetBox-design namespace          | EDA overwrites your DCIM                                                                                               |
| ApplyTopology on EDAManaged site                       | Conflict / workflow failure                                                                                            |
| Same IPAM tag on pools for two namespaces              | Wrong pool matched / shared consumption                                                                                |
| Stale API token secret                                 | Empty Allocation.status; pools never appear                                                                            |
| ENFORCE_GLOBAL_UNIQUE=true with overlapping topologies | Duplicate IP allocation failures                                                                                       |

## References

This document is a summary of the full NetBox-EDA technical documentation. Both documents, together with the scripts and manifests they reference, are published in the integration repository below.

**Repository:** https://github.com/dtrichards01/netbox-eda-integration

**Full guide:** docs/NetBox-EDA-Technical-Documentation.md — full technical documentation, adding the CR reference, the implementation procedures, the manual test guide and the appendices.

**This summary:** docs/NetBox-EDA-Technical-Documentation-public-v1.docx — this document.

**Scripts:** scripts/ — seeding, verification and test scripts referenced throughout.

**Manifests:** manifests/ — Instance, ApplyTopology and Allocation CR examples, plus secret templates.

**EDA docs:** https://docs.eda.dev/ — Nokia Event-Driven Automation documentation.

**EDA transactions:** https://docs.eda.dev/latest/user-guide/transactions/ — transaction API, Revert and Restore.

**NetBox:** https://netboxlabs.com/ — NetBox documentation and releases.

**Review feedback:** Please raise comments as issues in the repository above, or return annotated copies of this document.
