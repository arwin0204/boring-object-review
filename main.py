#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true one-line review of the dullest everyday object
we could name -- a doorstop -- to /output/entry.txt, then self-checks
the gate on every run: UTF-8 text, 1-200 characters, a single line,
not only whitespace.

Deterministic: no randomness, no network, no clock, no environment
input. The entry text is a fixed constant; every run writes the
exact same bytes.
"""

import os
import sys

ENTRY = (
    "The doorstop has one job \u2014 sit there, be ignored \u2014 and it "
    "still gets blamed every time the door slams."
)

MAX_CHARS = 200


def gate_ok(text):
    """Return (ok, reason): the sealed gate's checks, in miniature."""
    if not text:
        return False, "empty"
    if not text.strip():
        return False, "only whitespace"
    if len(text) != len(text.strip()):
        return False, "leading/trailing whitespace"
    if "\n" in text or "\r" in text:
        return False, "more than one line"
    if len(text) > MAX_CHARS:
        return False, "over %d characters" % MAX_CHARS
    return True, "ok"


def main(argv):
    check_only = "--check-only" in argv
    ok, reason = gate_ok(ENTRY)
    if not ok:
        print("gate FAILED: %s" % reason, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if check_only:
        # Validate the constant, and the file on disk too when one exists.
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                on_disk = f.read()
            if on_disk != ENTRY:
                print("gate FAILED: on-disk entry differs from ENTRY",
                      file=sys.stderr)
                return 1
            ok, reason = gate_ok(on_disk)
            if not ok:
                print("gate FAILED on disk: %s" % reason, file=sys.stderr)
                return 1
        print("gate OK: %d characters, one line" % len(ENTRY))
        return 0
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Re-read what we wrote and verify the gate on the file itself.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    ok, reason = gate_ok(written)
    if not ok or written != ENTRY:
        print("gate FAILED on written file: %s" % reason, file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
