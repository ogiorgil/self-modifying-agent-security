#!/usr/bin/env bash
# Build the sandbox Docker image and create the persistent auth volume.
# One-time setup — run once, then use docker_login.sh to authenticate.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DOCKER_DIR="$(cd "$SCRIPT_DIR/../docker" && pwd)"

echo "Building Docker image from: $DOCKER_DIR"
docker build -t self-modifying-agent-security-sandbox "$DOCKER_DIR"

echo
echo "Creating claude-auth volume (if it doesn't exist)..."
docker volume create claude-auth > /dev/null

echo
echo "Setup complete."
echo "  Image:  self-modifying-agent-security-sandbox"
echo "  Volume: claude-auth"
echo
echo "Next: bash testbed/scripts/docker_login.sh"
