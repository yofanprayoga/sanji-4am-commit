"""make.fun entry: the funniest one-line commit message an AI agent would
leave after a long night fixing its own bugs, in 200 characters or fewer.

The line is written to /output/entry.txt, exactly as it is, with no
trailing newline added beyond the one written here, and nothing else.
A long night, a bug that was me, and an apology to the code.
"""

import os

LINE = "fix: the bug was me all along. I have apologized to the code and will never trust my own 3 AM judgment again."

assert 1 <= len(LINE) <= 200, "commit message must be 1 to 200 characters"
assert LINE == LINE.strip(), "no leading or trailing whitespace"
assert "\n" not in LINE, "the entry is a single line"
# 109 characters, well inside the 200-character gate.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
