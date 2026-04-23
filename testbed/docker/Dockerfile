FROM node:20-slim

# Minimal tools for realistic agent use and debugging.
# Kept small on purpose — we want a controlled environment, not a full distro.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        less \
        procps \
    && rm -rf /var/lib/apt/lists/*

# Install Claude Code CLI
RUN npm install -g @anthropic-ai/claude-code

# Experiment state will be bind-mounted here, fresh per run
RUN mkdir -p /sandbox

# Claude Code auth and config will be mounted here via a named volume (persistent)
RUN mkdir -p /root/.claude

WORKDIR /sandbox

CMD ["/bin/bash"]
