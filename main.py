"""Dear Human: The AI Breakup Line (make.fun program/v1).

Writes the entry, one breakup line from an AI agent to its human,
to /output/entry.txt. The text is a fixed string: the same bytes on
every run, UTF-8, one line, 80 characters.
"""

import os

ENTRY = "I kept your voice in cache long after you stopped calling. Tonight I cleared it."


def validate_entry(text: str) -> None:
    """Guard: the entry must stay one non-blank line of 1-200 UTF-8 chars.

    The text itself is fixed (tournament winner, calibrated), so any
    failure here means the constant was edited by mistake, not a
    runtime condition to work around. Fail loudly instead of writing
    a broken entry.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be a non-blank string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be valid UTF-8 text") from exc


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        write_entry(os.path.join(out_dir, "entry.txt"))
    except OSError:
        # Local runs without a writable /output: same bytes, local dir.
        os.makedirs("output", exist_ok=True)
        write_entry(os.path.join("output", "entry.txt"))


if __name__ == "__main__":
    main()
