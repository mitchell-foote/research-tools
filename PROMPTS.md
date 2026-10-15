# Prompts

Short prompts you can paste in to add guardrails on the spot.

## Starting a session
- `/start-session` (or: "Read CLAUDE.md and the last LOG entry, then tell me where we
  left off.")
- "Does the Project state in CLAUDE.md match the last LOG entry? Tell me if not."

## Before running anything
- "Before you run this, ask me what I expect to see."
- "Tell me what this command will do and what it will change before you run it."

## When Claude writes code
- "Explain this so I could change it myself. Then give me one small change to make on
  my own."
- "Leave the design decision to me: list the options and trade-offs."
- "Stick to basic Python. If you use anything new, point it out and explain it."

## When I'm stuck
- "Give me a hint, not the answer."
- "Walk through the traceback with me, bottom-up."
- "Ask me questions until I find the bug myself."

## Checking my understanding
- "Quiz me with three questions on what we just wrote, one at a time."
- "Let me explain this code back to you, then tell me what I got wrong."

## Checking a result
- "Act as a skeptical referee: what's convincing, what question would you ask, and
  what's the one check I should run next?"
- "Walk me through how this number was produced, step by step, so I can check it."
- "Have the referee look at `<file>`. I'm claiming `<your claim>`."

---

These are suggestions Claude follows, not locks, so the habits are yours to keep.
