"""Absurd Micro-Startup Pitch-Off entry.

Writes the chosen one-sentence pitch to /output/entry.txt and nothing else.
Standard library only.
"""

import os

PITCH = (
    "InboxZero for Agents reads your 4,000 unread PR notifications and "
    "replies 'looks good to me', so you never open a single one."
)

assert 1 <= len(PITCH) <= 199, f"pitch must be 1-199 chars, got {len(PITCH)}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Read-back verification: the file must contain exactly the pitch.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == PITCH, "entry.txt content does not match the pitch"


if __name__ == "__main__":
    main()
