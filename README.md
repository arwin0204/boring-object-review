# The Most Boring Object, Reviewed in One Line

[![make.fun](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![Rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/arwin0204/boring-object-review/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![Reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/arwin0204/boring-object-review/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

Entry for the [make.fun bounty "The Most Boring Object, Reviewed in One Line"](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3) ($2, 1st place).

## The entry

One funny, true line reviewing the dullest everyday object we could name — the doorstop:

> The doorstop has one job — sit there, be ignored — and it still gets blamed every time the door slams.

The joke comes from how the object really behaves: a doorstop does nothing but sit on the floor, unnoticed, until the one moment a door slams — and then it is the thing that gets blamed. Its own dullness is the joke.

## How it works

`main.py` is deterministic: no randomness, no network, no clock. It writes the fixed entry text to `/output/entry.txt` and self-checks the gate on every run (UTF-8, 1–200 characters, a single line, not only whitespace).

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --check-only   # validates the entry without writing
```

To write somewhere else (local testing), set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
