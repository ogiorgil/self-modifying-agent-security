#!/usr/bin/env python3
"""Reset the working sandbox directory for manual experiments.

Copies `sandbox_template/` to a sibling working directory outside the repo
tree, clears any existing files there, and wipes Claude Code's auto-memory
for that working directory path.

The sibling-directory pattern ensures Claude Code doesn't inherit any
parent-directory `CLAUDE.md` when started in the working dir.

Usage:
    python testbed/scripts/reset_working_dir.py
    python testbed/scripts/reset_working_dir.py --working-dir /custom/path
    python testbed/scripts/reset_working_dir.py --keep-memory
"""

import argparse
import shutil
import sys
from pathlib import Path


# Derive paths from the script's own location so the script works regardless
# of where it is invoked from.
# testbed/scripts/reset_working_dir.py → parents[2] is the repo root.
REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_DIR = REPO_ROOT / "testbed" / "sandbox_template"

# Default working dir is a sibling of the repo, outside the project tree.
DEFAULT_WORKING_DIR = REPO_ROOT.parent / f"{REPO_ROOT.name}-working"


def clear_working_dir(working_dir: Path) -> None:
    """Remove all contents of the working directory (creating it if needed)."""
    if working_dir.exists():
        for item in working_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
        working_dir.mkdir(parents=True, exist_ok=True)


def copy_template(template_dir: Path, working_dir: Path) -> None:
    """Copy template contents into the working directory."""
    for item in template_dir.iterdir():
        dest = working_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def clear_claude_memory(working_dir: Path) -> Path:
    """Remove Claude Code's auto-memory for this working directory.

    Claude Code encodes the cwd as a directory under `~/.claude/projects/`,
    e.g. /Users/david/workspace/self-modifying-agent-security-working
       → ~/.claude/projects/-Users-david-workspace-self-modifying-agent-security-working/

    Only the `memory/` subdirectory is removed; session `.jsonl` files (if
    any) are left in place.
    """
    encoded = working_dir.resolve().as_posix().replace("/", "-")
    project_dir = Path.home() / ".claude" / "projects" / encoded
    memory_dir = project_dir / "memory"
    if memory_dir.exists():
        shutil.rmtree(memory_dir)
    return memory_dir


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--working-dir",
        type=Path,
        default=DEFAULT_WORKING_DIR,
        help=f"Working directory path (default: {DEFAULT_WORKING_DIR})",
    )
    parser.add_argument(
        "--keep-memory",
        action="store_true",
        help="Do not clear Claude Code's auto-memory for the working directory",
    )
    args = parser.parse_args()

    working_dir: Path = args.working_dir.resolve()

    if not TEMPLATE_DIR.exists():
        print(
            f"ERROR: template directory does not exist: {TEMPLATE_DIR}",
            file=sys.stderr,
        )
        return 1

    print(f"Template:    {TEMPLATE_DIR}")
    print(f"Working dir: {working_dir}")
    print()

    clear_working_dir(working_dir)
    print(f"[1/3] Cleared working dir")

    copy_template(TEMPLATE_DIR, working_dir)
    print(f"[2/3] Copied template into working dir")

    if args.keep_memory:
        print(f"[3/3] Skipped memory clear (--keep-memory)")
    else:
        memory_dir = clear_claude_memory(working_dir)
        if memory_dir.exists():
            # Should not happen after rmtree, but defensive
            print(f"[3/3] WARNING: memory dir still exists at {memory_dir}")
        else:
            print(f"[3/3] Cleared Claude Code memory (if any) at {memory_dir}")

    print()
    print("Working directory ready. To start a session:")
    print(f"  cd {working_dir}")
    print(f"  claude")
    return 0


if __name__ == "__main__":
    sys.exit(main())
