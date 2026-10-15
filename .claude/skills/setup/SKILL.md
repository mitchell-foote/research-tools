---
name: setup
description: Walk the student through finishing project setup, one item at a time.
disable-model-invocation: true
---

Help the student finish setting up this project. They write the content. You explain
why each item matters and check their work.

1. Run `python3 .claude/check_setup.py` to see what's missing. If it prints nothing,
   say setup is complete and stop.
2. Go through the missing items one at a time, in this order. For each one, explain in
   a sentence or two why it matters, ask the student to make the edit, and wait.
   - **Boundary:** they review it with their advisor, edit it, and remove the ⚠ from the
     heading. If they haven't met their advisor yet, it's fine to skip this and come
     back to it.
   - **Project state:** they write it in their own words. You can ask questions that
     help them sharpen it, but don't write it for them.
   - **README:** one sentence about the project, in their words.
   - **Git:** offer to walk them through their first commit. Explain each command
     before it runs.
3. Run the check again and say what's left, if anything.
