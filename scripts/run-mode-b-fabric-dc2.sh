#!/usr/bin/env bash
# Full Mode B fabric-dc2 lab — §5.2 through §5.7
set -euo pipefail

DOC_DIR="$(dirname "$0")"
TMP="/mnt/c/Users/darrenri/AppData/Local/Temp"
NS="fabric-dc2"
CLAB_NS="clab-3-tier-leaf-spine-dcgw"
WEBHOOK_SECRET="${FABRIC_DC2_WEBHOOK_SECRET:-fabric-dc2-wh-secret-change-me}"

echo "=== 1. Verify namespace bootstrap (§5.2) ==="
kubectl get nodeprofiles -n "$NS" 2>/dev/null | sed -n '1,5p' || true
NODE_PROFILE=$(kubectl get nodeprofiles -n "$NS" -o jsonpath='{.items[0].metadata.name}')
echo "NODE_PROFILE=$NODE_PROFILE"

echo "=== 2. NodeUser patch (§5.2) ==="
kubectl patch nodeuser admin -n "$NS" --type=json -p='[
  {"op":"add","path":"/spec/groupBindings/-","value":{
    "groups":["sudo"],
    "nodeSelector":["eda.nokia.com/source=netbox"]
  }}
]' 2>/dev/null || echo "(patch may already exist — OK)"

echo "=== 3. NetBox prerequisites — site, tags, webhook, event rule (§5.3) ==="
POD=$(kubectl get pod -n netbox -l app.kubernetes.io/name=netbox -o jsonpath='{.items[0].metadata.name}')
export FABRIC_DC2_WEBHOOK_SECRET="$WEBHOOK_SECRET"
kubectl cp "$(dirname "$0")/../manifests/nb-setup-fabric-dc2-prereqs.py" "netbox/${POD}:/tmp/nb-setup-fabric-dc2-prereqs.py"
kubectl exec -n netbox "$POD" -- env FABRIC_DC2_WEBHOOK_SECRET="$WEBHOOK_SECRET" \
  python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-setup-fabric-dc2-prereqs.py').read())"

echo "=== 4. EDA secrets + Instance (§5.4) ==="
API_TOKEN=$(kubectl get secret netbox-api-token -n "$CLAB_NS" -o jsonpath='{.data.apiToken}' | base64 -d)
cat > "$TMP/secrets-fabric-dc2.yaml" <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: netbox-webhook-signature
  namespace: ${NS}
type: Opaque
stringData:
  signatureKey: ${WEBHOOK_SECRET}
---
apiVersion: v1
kind: Secret
metadata:
  name: netbox-api-token
  namespace: ${NS}
type: Opaque
stringData:
  apiToken: ${API_TOKEN}
EOF
kubectl apply -f "$TMP/secrets-fabric-dc2.yaml"
kubectl apply -f "$(dirname "$0")/../manifests/instance-fabric-dc2.yaml"
for i in $(seq 1 30); do
  R=$(kubectl get instance.netbox.eda.nokia.com netbox -n "$NS" -o jsonpath='{.status.reachable}' 2>/dev/null || echo "")
  echo "  reachable=$R (attempt $i)"
  [[ "$R" == "true" ]] && break
  sleep 5
done
kubectl get instance.netbox.eda.nokia.com netbox -n "$NS" -o jsonpath='reachable={.status.reachable}{"\n"}'

echo "=== 5. NetBox DCIM — devices, interfaces, cables (§5.5) ==="
sed "s/NODE_PROFILE = .*/NODE_PROFILE = \"${NODE_PROFILE}\"/" "$(dirname "$0")/../manifests/nb-test-fabric-dc2.py" > "$TMP/nb-test-fabric-dc2.py"
kubectl cp "$TMP/nb-test-fabric-dc2.py" "netbox/${POD}:/tmp/nb-test-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-fabric-dc2.py').read())"

echo "=== 6. ApplyTopology (§5.6) ==="
kubectl apply -f "$(dirname "$0")/../manifests/applytopology-fabric-dc2.yaml"
sleep 10
kubectl get applytopology import-fabric-dc2 -n "$NS" -o jsonpath='phase={.status.phase}{"\n"}' 2>/dev/null || kubectl get applytopology import-fabric-dc2 -n "$NS"
kubectl get toponodes -n "$NS" --no-headers | wc -l
kubectl get topolinks -n "$NS" --no-headers | wc -l

echo "=== 7. NetBox IPAM allocation pools (§5.7) ==="
kubectl cp "$(dirname "$0")/../manifests/nb-test-allocation-pools-fabric-dc2.py" "netbox/${POD}:/tmp/nb-test-allocation-pools-fabric-dc2.py"
kubectl exec -n netbox "$POD" -- python /opt/netbox/netbox/manage.py shell -c "exec(open('/tmp/nb-test-allocation-pools-fabric-dc2.py').read())"
kubectl apply -f "$(dirname "$0")/../manifests/allocations-fabric-dc2.yaml"
sleep 8
kubectl get allocation -n "$NS"
kubectl get indexallocationpools,ipallocationpools,subnetallocationpools,ipinsubnetallocationpools -n "$NS" 2>/dev/null | sed -n '1,20p' || true

echo "=== Done ==="
