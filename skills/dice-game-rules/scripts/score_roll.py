#!/usr/bin/env python3
"""Calculate one turn in the two-six-sided-dice, exact-twenty game."""

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current-score", type=int, required=True)
    parser.add_argument("--die-one", type=int, choices=range(1, 7), required=True)
    parser.add_argument("--die-two", type=int, choices=range(1, 7), required=True)
    parser.add_argument("--target-score", type=int, default=20)
    arguments = parser.parse_args()

    if arguments.target_score < 1:
        parser.error("--target-score must be positive")
    if not 0 <= arguments.current_score < arguments.target_score:
        parser.error("--current-score must be at least zero and below the target")

    turn_total = arguments.die_one + arguments.die_two
    unadjusted_score = arguments.current_score + turn_total
    overshot = unadjusted_score > arguments.target_score
    final_score = 0 if overshot else unadjusted_score
    result = {
        "die_one": arguments.die_one,
        "die_two": arguments.die_two,
        "turn_total": turn_total,
        "score": final_score,
        "overshot": overshot,
        "won": final_score == arguments.target_score,
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())