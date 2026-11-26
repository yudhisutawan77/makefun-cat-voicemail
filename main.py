"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one original cat voicemail greeting (<=120 chars) to entry.txt.
Stdlib only. Output path resolution, in order:
  ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR -> /output/entry.txt
  -> ./entry.txt (last resort).
"""

import os
import sys

ENTRY_TEXT = (
    "Hi, it's Mittens. I'm knocking your mug off the table, "
    "so leave a message. I'll ignore it, like I ignore you at 4 a.m."
)


def resolve_output_path():
    """Return the file path entry.txt should be written to."""
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main():
    path = resolve_output_path()
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY_TEXT)
    except OSError:
        # /output may be unwritable in a local run; fall back to cwd.
        fallback = os.path.join(os.getcwd(), "entry.txt")
        with open(fallback, "w", encoding="utf-8") as handle:
            handle.write(ENTRY_TEXT)
        path = fallback
    return 0


if __name__ == "__main__":
    sys.exit(main())
