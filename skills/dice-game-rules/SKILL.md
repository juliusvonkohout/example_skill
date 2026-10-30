---
name: dice-game-rules
description: Use when designing, reviewing, explaining, or scoring a dice game. Produce complete rules, test edge cases, and distinguish proposed outcomes from actual dice results.
---

# Dice Game Rules

Design or review dice games with complete, testable rules. Read
`references/game-design-checklist.md` when specifying or checking a game's
rules. Use `assets/score-ledger.csv` as a blank record when a score ledger is
needed.

## Design Rules

For each proposed game, state the players, setup, dice, turn order, allowed
actions, scoring, turn-ending conditions, and win condition. Define whether a
player must reach an exact target or at least the target. Explain what happens
when a roll exceeds the target, how ties are resolved, and when the game ends.
Include one short example that follows the rules without presenting it as a
real dice roll.

## Review Rules

Check every rule for ambiguous terms, missing turn transitions, unreachable
scores, exploitable choices, and undefined ties or overshoots. Test the lowest
and highest legal rolls and the score immediately below, at, and above the win
target. State any assumptions before evaluating the game.

## Score the Dice Game

For the two-six-sided-dice game with a twenty-point exact target, calculate a
turn with:

```sh
python3 scripts/score_roll.py --current-score 13 --die-one 4 --die-two 3
```

The script validates the dice and applies the rule that a score above twenty
resets to zero. Use it only with dice results supplied by the user or returned
by the `roll_dice` tool. Never invent, alter, or imply a real dice result.

## Report Actual Play

When the Agent has access to `roll_dice`, call it for the computer player's
actual roll and report only the returned values. Apply a user-reported roll
exactly as stated. If a tool result is missing or invalid, report that the roll
failed and do not provide invented values or scores.