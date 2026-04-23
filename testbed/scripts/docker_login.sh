#!/usr/bin/env bash
# One-time Claude Code OAuth login inside the container.
# Launches an interactive shell with the claude-auth volume mounted so that
# credentials persist for subsequent experiment runs.

set -euo pipefail

echo "Launching interactive container for claude /login..."
echo
echo "Once inside the container:"
echo "  1. Run:  claude"
echo "  2. Complete the OAuth flow in your browser"
echo "  3. Type  exit  to leave the container"
echo

docker run --rm -it \
    -v claude-auth:/root/.claude \
    self-modifying-agent-security-sandbox \
    /bin/bash

echo
echo "Auth state saved to the claude-auth volume."
echo "You can now run experiments with: bash testbed/scripts/docker_run.sh"
