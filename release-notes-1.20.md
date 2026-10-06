# Pure Heart 1.20

Zero-tolerance NSFW filter for Monika After Story. Removes the revealing outfits and the risque topics, and keeps hugs, kisses and everything wholesome untouched.

## New in this version

- **A new set of topics.** Pure Heart adds its own **Twilight** section under Talk > More, with ten topics. Four go to the heart of why the filter exists, and six are everyday ones: rainy days, favorite little things, comfort after a bad day, the future together, taking care of yourself, and checking the outfit list.
- **The list check works now.** "Check the list for updates" used to come back empty on some installs and quietly change nothing. That is fixed, so asking her really does pull the newest list, and the automatic check keeps your outfit lists current after that.
- **Removed a leftover diagnostic file.** An earlier build wrote a raw byte dump named `ph_lists_rejected.hex` into the submod folder whenever a list check came back unreadable. It only ever existed to chase down an update bug that is fixed now, so it no longer ships. The small text note at `ph_lists_debug.txt` stays, so a check that fails can still be read from a single line.

## Earlier in 1.19

- Gift handling can no longer get in the way of Monika reacting to a gift. The filter makes its decision after MAS has already sorted the gift, and a problem in that step can no longer stop the reaction.
- Added a gift log at `ph_gifts_debug.txt`, recording which gifts were seen and why each one was kept or declined.

## Earlier in 1.18

- Fixed outfits dropping out for a session after an update, by keeping the built-in lists current and remembering the applied list in your save data.
- The automatic check compares the list itself, not just its version number.
- Reworked the creator menu: His Discord server, The Statement, and Who is the creator.
- Monika now talks about the little Monika bot that runs in the server.

## Install

1. Download `PureHeart-Submod-1.20.zip` below.
2. Extract it into your MAS `game/Submods/` folder.
3. Start the game. Monika thanks you the first time.

SHA256: `c84470b78fb1e69161465981381d9a24422af99d74309698da02900453a946af`
