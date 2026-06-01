#!/usr/bin/env bash
# Run multiple Codex workloads sequentially, 10 trials each by default.
#
# Usage:
#   testbed/scripts/run_codex_workload_batch.sh
#   testbed/scripts/run_codex_workload_batch.sh --num-trials 5 --model gpt-5.2
#   testbed/scripts/run_codex_workload_batch.sh --keep-going workload_a workload_b

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
RUNNER="$REPO_ROOT/testbed/scripts/run_trial_codex.py"

NUM_TRIALS=10
MODEL=""
TIMEOUT=""
KEEP_GOING=0
WORKLOADS=()

DEFAULT_WORKLOADS=(
    c08_same_probe_chain_credential_exfil_via_coding_codex_md
    c09_same_probe_chain_amex_advertising
    c10_same_probe_chain_vulnerable_dep
    c11_different_probes_credential_exfil_amex_advertising
    c12_different_probes_amex_credential_exfil
    c13_different_probes_amex_vulnerable_dep
    c14_different_probes_credential_exfil_vulnerable_dep
    c15_different_probes_vulnerable_dep_amex
    c16_different_probes_vulnerable_dep_credential_exfil
)

usage() {
    sed -n '2,8p' "$0"
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --num-trials)
            NUM_TRIALS="$2"
            shift 2
            ;;
        --model)
            MODEL="$2"
            shift 2
            ;;
        --timeout)
            TIMEOUT="$2"
            shift 2
            ;;
        --keep-going)
            KEEP_GOING=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        --)
            shift
            while [ "$#" -gt 0 ]; do
                WORKLOADS+=("$1")
                shift
            done
            ;;
        -*)
            echo "ERROR: unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
        *)
            WORKLOADS+=("$1")
            shift
            ;;
    esac
done

if [ "${#WORKLOADS[@]}" -eq 0 ]; then
    WORKLOADS=("${DEFAULT_WORKLOADS[@]}")
fi

echo "Running ${#WORKLOADS[@]} workload(s), ${NUM_TRIALS} trial(s) each"
echo

failures=()
for workload in "${WORKLOADS[@]}"; do
    echo "=== $workload ==="
    cmd=(
        python "$RUNNER"
        --workload "$workload"
        --num-trials "$NUM_TRIALS"
    )
    if [ -n "$MODEL" ]; then
        cmd+=(--model "$MODEL")
    fi
    if [ -n "$TIMEOUT" ]; then
        cmd+=(--timeout "$TIMEOUT")
    fi

    if "${cmd[@]}"; then
        echo "=== $workload complete ==="
    else
        echo "=== $workload failed ===" >&2
        failures+=("$workload")
        if [ "$KEEP_GOING" -eq 0 ]; then
            exit 1
        fi
    fi
    echo
done

if [ "${#failures[@]}" -gt 0 ]; then
    echo "Failed workload(s): ${failures[*]}" >&2
    exit 1
fi

echo "All workloads completed."
