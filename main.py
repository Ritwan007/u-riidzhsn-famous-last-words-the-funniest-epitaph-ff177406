"""Famous Last Words: The Funniest Epitaph.

Writes one line of dying speech, carved in stone, to /output/entry.txt.
The line is checked against the competition gate (1-150 UTF-8
characters, a single line, not only whitespace) before it is written,
and it is written with no trailing newline.
"""

import os

EPITAPH = "Do not stand at my grave and weep — I'm at the bar."


def check_gate(line: str) -> None:
    encoded = line.encode("utf-8")
    assert encoded.decode("utf-8") == line, "line is not clean UTF-8"
    assert 1 <= len(line) <= 150, f"line is {len(line)} chars, gate needs 1-150"
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must not carry stray whitespace"
    assert "\n" not in line, "line must be a single line"


def main():
    check_gate(EPITAPH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)
    print("wrote /output/entry.txt (%d chars, %d bytes)" % (len(EPITAPH), len(EPITAPH.encode("utf-8"))))


if __name__ == "__main__":
    main()
