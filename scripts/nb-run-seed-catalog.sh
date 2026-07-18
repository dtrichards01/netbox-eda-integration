#!/usr/bin/env bash
# Paste-safe runner for nb-seed-eda-catalog.py (WSL / Linux).
# Usage: bash $(dirname "$0")/nb-run-seed-catalog.sh
set -euo pipefail
SCRIPT="${1:-$(dirname "$0")/nb-seed-eda-catalog.py}"
if [[ ! -f "$SCRIPT" ]]; then
  echo "Missing: $SCRIPT" >&2
  exit 1
fi
kubectl exec -n netbox -i deployment/netbox -c netbox -- python /opt/netbox/netbox/manage.py shell < "$SCRIPT"
