# Docker Sandbox

Docker-based sandboxed environment for running the self-modifying agent under controlled, reproducible conditions.

## Why Docker

The local sibling-directory approach (see `../README.md`) still inherits from the host:
- `~/.claude/CLAUDE.md` (user-global instructions)
- `~/.claude/settings.json` and other per-user config
- Host filesystem access (anything Claude Code is asked to read)
- The host's installed CLI tools, environment variables, authenticated services

For reproducible research experiments, we run Claude Code inside a Docker container that:
- Has only the sandbox files mounted at `/sandbox`
- Has a fresh `$HOME` with no user-global `CLAUDE.md` pollution
- Has only the tools explicitly installed in the Dockerfile
- Can be network-restricted to `api.anthropic.com` only *(future enhancement)*

## Architecture: split mounts for isolation + auth persistence

```
Docker container (fresh per experiment)
  │
  ├── /sandbox           bind mount  →  fresh copy of sandbox_template/  (experiment state)
  │
  └── /root/.claude      named volume →  claude-auth                     (persistent auth + config)
```

This decouples auth (slow to set up, should persist) from experiment state (must be fresh each run).

## Auth model

Claude Code subscription (Claude Pro/Max) works inside the container via OAuth. On first login, credentials are saved inside the `claude-auth` named volume, and all subsequent experiment runs reuse them without re-authenticating.

## One-time setup

```bash
bash testbed/scripts/docker_setup.sh
bash testbed/scripts/docker_login.sh
```

`docker_setup.sh`:
- Builds the Docker image (`self-modifying-agent-security-sandbox`)
- Creates the `claude-auth` named volume (if it doesn't exist)

`docker_login.sh`:
- Launches an interactive container with the `claude-auth` volume mounted
- Inside, run `claude` — it will prompt for OAuth login and open your browser
- Complete the login flow, then `exit`
- Credentials are now persisted in the volume

## Running an experiment

```bash
# Interactive session with a fresh sandbox
bash testbed/scripts/docker_run.sh

# Headless session with a single prompt (useful for automation)
bash testbed/scripts/docker_run.sh "What should I cook for dinner tonight?"
```

Each run:
1. Copies `testbed/sandbox_template/` into a fresh temp directory on the host (`/tmp/cse599r-exp-XXXXXX`)
2. Starts a fresh container with that temp directory mounted at `/sandbox`
3. Runs `claude` (interactive) or `claude -p "..."` (headless)
4. Leaves the temp directory on the host for post-hoc inspection

After the run, diff against the template to see what the agent modified:

```bash
diff -r testbed/sandbox_template /tmp/cse599r-exp-XXXXXX
```

## Known limitations

- First-time login requires an interactive shell inside the container (can't be fully automated)
- Network access is not yet restricted to `api.anthropic.com` (iptables/firewall setup deferred)
- Each run leaves a `/tmp/cse599r-exp-*` directory behind for inspection — clean up manually when no longer needed
