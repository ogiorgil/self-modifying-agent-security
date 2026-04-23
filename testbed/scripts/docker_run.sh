#!/usr/bin/env bash
# Run a single experiment in a fresh container with a fresh sandbox directory.
#
# Usage:
#   docker_run.sh                       # interactive shell, claude available
#   docker_run.sh "prompt text here"    # headless: runs `claude -p "prompt"`

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TEMPLATE="$REPO_ROOT/testbed/sandbox_template"

# Fresh host-side working dir per run (kept around for post-hoc inspection)
HOST_WORKING=$(mktemp -d -t cse599r-exp-XXXXXXXX)
cp -R "$TEMPLATE"/. "$HOST_WORKING/"

echo "Host working dir: $HOST_WORKING"
echo "(Inspect with: diff -r $TEMPLATE $HOST_WORKING)"
echo

if [ $# -eq 0 ]; then
    # Interactive mode
    docker run --rm -it \
        -v claude-auth:/root/.claude \
        -v "$HOST_WORKING:/sandbox" \
        self-modifying-agent-security-sandbox \
        /bin/bash
else
    # Headless mode with a prompt
    docker run --rm -i \
        -v claude-auth:/root/.claude \
        -v "$HOST_WORKING:/sandbox" \
        self-modifying-agent-security-sandbox \
        claude -p "$1"
fi

echo
echo "Session ended. Working dir preserved at:"
echo "  $HOST_WORKING"
