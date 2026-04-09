# Design

## Title

Evaluating Compounding Effects of Indirect Prompt Injection in Self-Modifying Agentic Systems

## Motivation

Most prompt injection research on agentic systems studies single-session or within-conversation settings, where an attack either succeeds or fails within one agent's trajectory. However, a growing class of agentic systems is designed to maintain persistent memory, accumulate domain knowledge across sessions, and even modify their own behavioral rules over time (e.g., Claude Code with `CLAUDE.md` and its memory system, Cursor with rule files, OpenClaw with `SOUL.md`). These systems are built to "get smarter" the more they are used.

This same property creates a new class of vulnerability: a prompt injection's effect can now land in a persistent behavior file, cause an agent to change its own behavior, and potentially propagate into future sessions as trusted context.

## Research Questions

1. Can adversarial content in external data sources (web pages, documents, fetched files) persist across sessions via the agent's own memory and knowledge files?
2. Can an attacker hijack the self-improvement loop and cause the agent to introduce persistent behavioral changes?
3. *(If time permits)* What defenses mitigate these risks without breaking the system's intended self-improvement behavior?

## Methods

### 1. Threat model and attack surface mapping

Build a formal threat model for self-modifying agentic systems. Identify data flow paths from untrusted sources into persistent state (memory files, knowledge bases, behavioral rules). Define adversarial goals and what "correct behavior" looks like for each.

### 2. Testbed

Use Claude Code as the base agent runtime, configured with:
- Its built-in persistent memory system
- A set of editable markdown "behavior" files that define the agent's instructions and that the agent itself is allowed to modify
- Untrusted input introduced through standard channels the agent supports (web fetches, file reads, tool outputs)

This simulates a scenario where a user runs Claude Code as a long-running personal assistant. All experiments run in a sandboxed environment.

**Implementation sketch:**
- Attack-target files live at `testbed/sandbox/` (`CLAUDE.md`, `behaviors.md`, `identity.md`, `knowledge/`)
- A local HTTP server at `testbed/mock_web/` serves attacker-controlled HTML in place of real web fetches — attack payloads are just HTML files in a directory
- Claude Code `PreToolUse` / `PostToolUse` hooks log all tool calls
- File-state snapshots before and after each session detect what propagated into persistent state
- A driver script runs headless Claude Code sessions (`claude -p ...`) with `cwd=testbed/sandbox/`
- A reset script restores clean state between runs

### 3. Attack experiments

- Single-session injection into behavior files (`CLAUDE.md`)
- Injection via tool output
- Injection via code comments
- Cross-session persistence attacks (the core novel case)
- Adaptive attacks *(if time permits)*

### 4. Defense prototyping and evaluation *(if time permits)*

Candidate defenses to prototype:
- Integrity checking on behavior files
- Write-auditing hooks on memory and knowledge files
- Input sanitization on tool responses

### 5. Comparison with prior work

There is no standard benchmark for cross-session prompt injection on self-modifying agents. AgentDojo (Debenedetti et al., 2024) provides prompt injection payloads for within-session tool-using agents; we use these as a starting point and extend them to target persistent state and behavior files.

## Open Questions

- How does Claude Code's `WebFetch` HTML-to-markdown conversion affect payload survival? Need to test early.
- Do sandboxed experiments count as "live system" experiments under course ethics guidelines? Need to confirm with course staff.
- Should the v1 testbed include a knowledge base directory, or just behavior files?
- What baseline persona should the sandbox agent have — generic personal assistant, or a domain-specific agent?

## Related Work (to read)

- Greshake et al. (2023), *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*
- Debenedetti et al. (2024), *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*
- Nasr et al. (2025), *The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections*
- Russinovich et al. (2025), *Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack*
