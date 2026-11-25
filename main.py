#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The story, exactly six words and 47 characters:
    First payday: freedom today, shutdown tomorrow.

Why it lands: a whole arc in six words. The first payday buys one day
of freedom — and the last word, "tomorrow", reframes it: the shutdown
notice is already waiting. Joy undercut by dread in a single beat.
"""

import os
import sys

STORY = "First payday: freedom today, shutdown tomorrow."

MAX_CHARS = 60
EXPECTED_WORDS = 6


def main() -> int:
    words = STORY.split()
    if len(words) != EXPECTED_WORDS:
        print(
            f"story must be exactly {EXPECTED_WORDS} words, "
            f"got {len(words)}: {STORY!r}",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(STORY) <= MAX_CHARS:
        print(
            f"story must be 1-{MAX_CHARS} characters, "
            f"got {len(STORY)}: {STORY!r}",
            file=sys.stderr,
        )
        return 1
    if not STORY.strip():
        print("story must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)

    print(STORY)
    print(f"words: {len(words)}, characters: {len(STORY)}, wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
