#!/usr/bin/env bash
set -euo pipefail
DOC=$(dirname "$0")
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')

echo "=== 1. NetBox IPAM pools — fabric-dc2 (idempotent) ==="
kubectl cp "$DOC/nb-test-allocation-pools-fabric-dc2.py" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c 'exec(open("/tmp/nb-test-allocation-pools-fabric-dc2.py").read())'

echo "=== 2. NetBox IPAM pools — clab-3-tier-leaf-spine-dcgw ==="
kubectl cp "$DOC/nb-test-allocation-pools-clab3tier.py" "netbox/${POD}:/tmp/nb-test-allocation-pools-clab3tier.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c 'exec(open("/tmp/nb-test-allocation-pools-clab3tier.py").read())'

echo "=== 3. Apply Allocation CRs ==="
kubectl apply -f "$DOC/allocations-fabric-dc2.yaml"
kubectl apply -f "$DOC/allocations-clab-3-tier-leaf-spine-dcgw.yaml"

echo "=== 4. Refresh all allocations via ApplyAllocation ==="
for ns in fabric-dc2 clab-3-tier-leaf-spine-dcgw; do
  for cr in $(kubectl get allocation -n "$ns" -o jsonpath='{.items[*].metadata.name}'); do
    name="refresh-${cr}"
    kubectl delete applyallocation "$name" -n "$ns" --ignore-not-found --wait=true 2>/dev/null || true
    kubectl apply -f - <<EOF
apiVersion: netbox.eda.nokia.com/v1alpha1
kind: ApplyAllocation
metadata:
  name: ${name}
  namespace: ${ns}
spec:
  allocation: ${cr}
EOF
    echo "  applied ApplyAllocation ${name} in ${ns}"
  done
done

sleep 15

echo "=== 5. Restart eda-netbox (pick up site cache for ASN) ==="
kubectl rollout restart deployment/eda-netbox -n eda-system
kubectl rollout status deployment/eda-netbox -n eda-system --timeout=120s

sleep 20

echo "=== 6. fabric-dc2 allocations ==="
kubectl get allocation -n fabric-dc2 -o custom-columns=NAME:.metadata.name,TYPE:.spec.type,PREFIX:.status.matchedPrefixes,VLAN:.status.matchedVlanGroups,ASN:.status.matchedAsnRanges

echo "=== 7. clab-3-tier allocations ==="
kubectl get allocation -n clab-3-tier-leaf-spine-dcgw -o custom-columns=NAME:.metadata.name,TYPE:.spec.type,PREFIX:.status.matchedPrefixes,VLAN:.status.matchedVlanGroups,ASN:.status.matchedAsnRanges

echo "=== 8. EDA pools from NetBox (nb-*) ==="
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -A 2>/dev/null | grep '^nb-' || true
