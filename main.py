#!/usr/bin/env python3
"""Round 1 entry: a houseplant's one-star review of its human owner.

The review is assembled from short fragments so each beat of the joke stays
easy to read and revise, then checked against the competition gate (1-279
characters, one line, no trailing newline) before it is written out.

The grievance is the plant's own: watered on a library schedule, then blamed
for the leaf it drops on the laptop. The twist is the last clause — the drop
was planned, and the plant is not even pretending otherwise.
"""

import os
import sys

REVIEW = " ".join([
    "One star.",
    "He waters me every third Tuesday, like I'm a library book,",
    "then gasps when I drop a leaf onto his laptop mid-call,",
    "as if I didn't plan it.",
])


def _fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def _check(line):
    if not line.strip():
        _fail("blank output")
    if any(ch in line for ch in "\r\n"):
        _fail("output must be a single line")
    size = len(line)
    if not 1 <= size <= 279:
        _fail(f"output length {size} outside 1-279 gate")
    if len(line.encode("utf-8")) != size:
        _fail("output must be plain ASCII")


def _destination():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def run():
    text = REVIEW
    _check(text)
    path = _destination()
    with open(path, "w", encoding="utf-8", newline="") as stream:
        stream.write(text)
    with open(path, "r", encoding="utf-8", newline="") as stream:
        written = stream.read()
    if written != text:
        _fail("round-trip mismatch")
    _check(written)


if __name__ == "__main__":
    run()
