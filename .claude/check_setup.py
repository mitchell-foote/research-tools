"""Check whether this project's setup is finished.

Claude Code runs this at the start of each new session (see .claude/settings.json).
Anything it prints is passed to Claude. If setup is complete, it prints nothing.

Lines you're most likely to change: the checks in the middle section, if you want to
add or remove something from the setup list.
"""

import re
import subprocess
from pathlib import Path

# The project folder is the parent of the .claude folder this script lives in.
PROJECT = Path(__file__).resolve().parent.parent


def read(name):
    """Return the text of a project file, or "" if it doesn't exist."""
    path = PROJECT / name
    return path.read_text(encoding="utf-8") if path.exists() else ""


problems = []

# --- The checks ---

claude_md = read("CLAUDE.md")

# The boundary heading keeps its ⚠ until the student has reviewed it with an advisor.
if re.search(r"^## The boundary.*⚠", claude_md, re.MULTILINE):
    problems.append("The boundary in CLAUDE.md hasn't been reviewed with an advisor.")

# A Project state field is empty if nothing follows the colon.
for field in ["Current question", "Current dataset", "Next step"]:
    if re.search(rf"^- \*\*{field}:\*\*\s*$", claude_md, re.MULTILINE):
        problems.append(f"Project state in CLAUDE.md: '{field}' is empty.")

if "*Replace this line" in read("README.md"):
    problems.append("README.md still has the placeholder project description.")

# "git rev-parse HEAD" fails if there are no commits (or git isn't installed).
try:
    result = subprocess.run(["git", "rev-parse", "--verify", "HEAD"],
                            cwd=PROJECT, capture_output=True)
    if result.returncode != 0:
        problems.append("The project has no git commits yet.")
except FileNotFoundError:
    problems.append("git isn't installed, or isn't on the PATH.")

# --- The message to Claude ---

if problems:
    print("Project setup isn't finished:")
    for problem in problems:
        print("- " + problem)
    print("Mention this briefly in your first reply and suggest the student run /setup. "
          "Then help with whatever they asked; don't block on it.")
