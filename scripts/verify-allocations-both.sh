#!/usr/bin/env bash
set -euo pipefail

check_ns() {
  local NS=$1
  echo "========== $NS =========="
  kubectl get instance netbox -n "$NS" -o custom-columns=REACHABLE:.status.reachable,SYNC:.spec.sync.enabled 2>/dev/null || true
  echo
  echo "--- Allocation CRs ---"
  kubectl get allocation -n "$NS" -o custom-columns=NAME:.metadata.name,TYPE:.spec.type,MATCHED:.status.matchedPrefixes,VLAN:.status.matchedVlanGroups,ASN:.status.matchedAsnRanges 2>/dev/null || echo "(none)"
  echo
  echo "--- NetBox-backed EDA pools (nb-*) ---"
  kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n "$NS" 2>/dev/null | grep 'nb-' || echo "(none)"
  echo
}

check_ns fabric-dc2
check_ns clab-3-tier-leaf-spine-dcgw
