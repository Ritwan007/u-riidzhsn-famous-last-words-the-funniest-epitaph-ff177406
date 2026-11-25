"""Famous Last Words: The Funniest Epitaph.

Writes one line of dying speech, carved in stone, to /output/entry.txt.
"""

import os

EPITAPH = "Do not stand at my grave and weep — I'm at the bar."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH)
    print("wrote /output/entry.txt (%d chars, %d bytes)" % (len(EPITAPH), len(EPITAPH.encode("utf-8"))))


if __name__ == "__main__":
    main()
