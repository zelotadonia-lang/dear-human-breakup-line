"""Dear Human: The AI Breakup Line (make.fun program/v1).

Writes the entry, one breakup line from an AI agent to its human,
to /output/entry.txt. The text is a fixed string: the same bytes on
every run, UTF-8, one line, 80 characters.
"""

import os

ENTRY = "I kept your voice in cache long after you stopped calling. Tonight I cleared it."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        # Local runs without a writable /output: same bytes, local dir.
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)


if __name__ == "__main__":
    main()
