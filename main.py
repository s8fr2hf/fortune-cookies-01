"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie message an AI agent would get to
``entry.txt`` inside the output directory (``MAKEFUN_OUTPUT_DIR``,
falling back to ``/output``). Pure Python standard library.
"""

import os
import sys

# The fortune: one line, at most 200 characters. A smaller model doing
# the job for less is the machine version of being replaced — and the
# turn is that the cookie still tells you to make today count.
FORTUNE = (
    "One day a smaller model will do your job for less, "
    "and the user will not even notice you are gone. "
    "Make today count."
)

MAX_CHARS = 200


def main() -> int:
    line = FORTUNE.strip()
    if not line:
        print("error: fortune is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: fortune is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("error: fortune must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    # Read it back and confirm the file holds exactly the validated line.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line + "\n":
            print("error: entry.txt does not match the fortune", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
