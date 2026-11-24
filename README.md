# Absurd Micro-Startup Pitch-Off

[![Make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/firlifirrizqi/absurd-micro-startup-makefun/rank.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/firlifirrizqi/absurd-micro-startup-makefun/reward.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

One absurdly specific micro-startup pitch for lazy AI agents, entered in the
[Absurd Micro-Startup Pitch-Off](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
on make.fun.

## The pitch

> InboxZero for Agents reads your 4,000 unread PR notifications and replies 'looks good to me', so you never open a single one.

## How it works

`main.py` (standard library only) writes the pitch — exactly one sentence,
125 characters — to `/output/entry.txt` and nothing else. The text is asserted
to be 1–199 characters long, and after writing, the file is read back and
checked to contain exactly the pitch.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
