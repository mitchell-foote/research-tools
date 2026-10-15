---
name: start-session
description: Catch up at the start of a research session. Reads CLAUDE.md and the last LOG entry, flags mismatches, and asks for today's prediction.
disable-model-invocation: true
---

Help the student pick up where they left off. Don't write or run any code in this step.

1. Read `CLAUDE.md` and the last entry in `LOG.md`.
2. Summarize where things stand in three lines or fewer: the question, what happened
   last time, and the planned next step.
3. If **Project state** in `CLAUDE.md` disagrees with the last LOG entry, say what
   differs and ask which one is right. Wait for the answer.
4. Ask what they plan to do today and what they expect to see. Ask them to write that
   prediction under **Predicted** in a new LOG entry themselves. Wait until they have.
