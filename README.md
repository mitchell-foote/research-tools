# Research Project

*Replace this line with one sentence about your project.*

## How this project works

You do the research. Claude helps with syntax and tools. Anything Claude writes, you
should be able to change on your own. The test: *"Could you make the next change to
this yourself, without asking Claude?"*

## The files

| File | What it's for | Who edits it |
|------|---------------|--------------|
| `CLAUDE.md` | Instructions Claude reads at the start of every session | You and your advisor |
| `LOG.md` | Your research log, one entry per session | You, in your own words |
| `PROMPTS.md` | Short prompts to paste in when you want a guardrail | You, as you find better ones |
| `.gitignore` | Files git should not track | You, when you add new kinds of files |
| `.claude/skills/start-session/` | The `/start-session` command: catch up and make a prediction | You, if the routine changes |
| `.claude/agents/referee.md` | A skeptical reviewer that checks a result with fresh eyes | You and your advisor |
| `.claude/skills/setup/` | The `/setup` command: finish anything missing from setup | You, if the setup list changes |
| `.claude/check_setup.py` | Checks what setup is missing at the start of each session | You, to add or remove checks |
| `.claude/settings.json` | Tells Claude Code to run `check_setup.py` when a session starts | Rarely |

## Your first session

1. Start Claude Code in this folder and type `/setup`. The first time, Claude Code will
   ask you to approve the project's startup check; that's expected.
2. `/setup` walks you through what's missing: reviewing the boundary in `CLAUDE.md`
   with your advisor, filling in **Project state**, describing the project here, and
   your first git commit.
3. Then type `/start-session` and begin.

*On Windows, if the startup check fails, change `python3` to `python` in
`.claude/settings.json`.*

## Every session

- **Start:** type `/start-session`, then write your prediction in `LOG.md` before you
  run anything.
- **During:** use `PROMPTS.md` whenever you want Claude to slow down or hand you the
  next step. Before you trust a result, ask the referee to look at it.
- **End:** write today's LOG entry yourself, in your own words.
