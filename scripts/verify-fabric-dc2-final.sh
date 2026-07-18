#!/usr/bin/env bash
set -euo pipefail
NS=fabric-dc2
echo "=== ApplyTopology ==="
kubectl get applytopology import-fabric-dc2 -n "$NS" -o custom-columns=NAME:.metadata.name,STATE:.metadata.annotations.workflows\.core\.eda\.nokia\.com/state
echo
echo "=== TopoNodes ($(kubectl get toponodes -n "$NS" --no-headers 2>/dev/null | wc -l)) ==="
kubectl get toponodes -n "$NS"
echo
echo "=== TopoLinks ($(kubectl get topolinks -n "$NS" --no-headers 2>/dev/null | wc -l)) ==="
kubectl get topolinks -n "$NS"
echo
echo "=== Allocations ==="
kubectl get allocation -n "$NS" -o custom-columns=NAME:.metadata.name,TYPE:.spec.type,MATCHED_PREFIX:.status.matchedPrefixes,MATCHED_VLAN:.status.matchedVlanGroups,MATCHED_ASN:.status.matchedAsnRanges
echo
echo "=== EDA pools (fabric-dc2) ==="
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n "$NS" 2>/dev/null | grep fabric || true
echo
echo "=== Instance ==="
kubectl get instance netbox -n "$NS" -o custom-columns=REACHABLE:.status.reachable,SYNC:.spec.sync.enabled
