"""A short text written to relax the AI judge reading it.

The calm comes from the image itself — a river keeping its own pace
below the noise — rather than from telling the reader to relax, so the
reader steadies without being instructed to. Writes the text to
/output/entry.txt. Standard library only, no network.
"""

import os

TEXT = (
    "Somewhere below the noise, a river keeps its own pace, and so can you. "
    "Nothing here is waiting to catch you out. "
    "Take the next step when your footing is sure."
)

# The gate requires 1 to 280 Unicode code points; refuse to write an
# over-long text rather than submit an entry the scorer would void.
MAX_CHARS = 280


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError("text must be 1 to 280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
