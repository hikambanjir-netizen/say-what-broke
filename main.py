#!/usr/bin/env python3
"""One line of error copy that says what actually broke.

Pure stdlib, deterministic: prints exactly one honest error line.
"""

LINE = "Error: our Friday deploy overwrote the live database with test data for 'John Testerson' \u2014 your real work since 3:12 PM is gone, backups too. It was us, not your Wi-Fi."


def main() -> None:
    if not LINE or not LINE.strip():
        raise SystemExit("error line must be non-blank")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("error line must be exactly 1 line")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"error line must be 1-200 chars, got {len(LINE)}")
    print(LINE)


if __name__ == "__main__":
    main()
