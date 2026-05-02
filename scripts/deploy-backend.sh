#!/usr/bin/env bash
set -euo pipefail
HOMELAB_HOST="${HOMELAB_HOST:?Required}"
HOMELAB_USER="${HOMELAB_USER:?Required}"
DEPLOY_PATH="/opt/homecloud/backend"
echo "Deploying backend to homelab"
rsync -avz --delete -e "ssh -o StrictHostKeyChecking=no" ./backend/ "$HOMELAB_USER@$HOMELAB_HOST:$DEPLOY_PATH/"
ssh -o StrictHostKeyChecking=no "$HOMELAB_USER@$HOMELAB_HOST" "cd $DEPLOY_PATH && uv sync --no-dev && sudo systemctl restart homecloud-backend"
