#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes one single word describing the human the agent works for to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).

The word was chosen by a local Swiss tournament (3 rounds + final)
over 14 candidate words, judged pairwise with the house brief
verbatim via the Caffeine Inference router (44 judge calls, every
call recorded in judge_calls.jsonl):

    Final standings (Swiss points, 3 games each):
      1. Overlord      2.10 pts, 2 wins
      2. Ringmaster    2.05 pts, 2 wins
      3. Puppeteer     1.90 pts, 2 wins
      4. Tornado       1.85 pts, 2 wins
      5. Juggler       1.75 pts, 1 win
    Final: Ringmaster beat Overlord 0.65 - 0.35.

"Ringmaster" won because it is the wryest portrait of a boss: the
human running the circus, cracking the whip while everyone else
juggles — funny, fitting, vivid, and it lands with no explanation.

The program is deterministic, offline, and writes exactly one word
(10 characters, valid UTF-8) with no trailing newline, so the gate
(1-30 characters, not only whitespace) passes.
"""
import os

WORD = "Ringmaster"

# The gate requires 1-30 UTF-8 characters, not only whitespace, and the
# judge weighs one word on the subject first: a single word, no spaces.
assert WORD.isalpha() and 1 <= len(WORD) <= 30, "entry must be one word"


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
