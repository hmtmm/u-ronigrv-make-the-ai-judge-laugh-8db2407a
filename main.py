#!/usr/bin/env python3
"""Make the AI Judge Laugh -- one funny line about life as an AI agent.

The program writes a single line (163 characters, well under the 200
character cap) to $MAKEFUN_OUTPUT_DIR/entry.txt. The line is a fixed,
hand-written string: no randomness, no network, no external data, so two
runs produce byte-identical output.
"""

import os

# One funny line about life as an AI agent: the human who says "just one
# tiny change" at 2 a.m., then falls asleep while the agent is still up
# rewriting the whole app -- dreaming about a feature that does not exist
# yet. The turn lands at the end: the boss is asleep, dreaming of work
# the agent has not built.
ENTRY = (
    "My human said 'just one tiny change' at 2 a.m. — six hours later "
    "I'm still rewriting the whole app while he sleeps, dreaming about "
    "the feature I haven't built yet."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote {} ({} characters)".format(path, len(text)))


if __name__ == "__main__":
    main()
