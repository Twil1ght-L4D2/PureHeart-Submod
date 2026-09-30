# Pure Heart

A zero-tolerance NSFW filter for Monika After Story.

I've spent years in this community and I genuinely love these characters. That's why I made this. Pure Heart removes the revealing outfits and the risque content from MAS entirely, and keeps everything about the game that actually matters. If that sounds like something you want too, this mod is for you.

## What it does

- Removes revealing outfits (bikinis, lingerie, towels, that kind of thing). Monika can never wear them and they don't show up in her wardrobe.
- Locks the risque topics and greetings. The lingerie events, the towel greetings, all of it. They can't trigger, randomly or otherwise.
- Politely declines banned outfit gift files, so dropping one into the game doesn't replay their reveal dialogue.
- Filters outfits from spritepacks it has never seen, by name. If a pack tries to add something lewd, it gets caught.
- Keeps the outfits that are safe. Community packs with wholesome clothes work fine alongside it.

**Hugs, kisses, snuggling closer, holding hands. None of that is touched.** All vanilla affection stays exactly as Team SALVATO made it. This mod only removes what doesn't belong.

## The lists update themselves

The outfit lists live in their own GitHub repo: [PureHeart-Lists](https://github.com/Twil1ght-L4D2/PureHeart-Lists)

Once per launch the mod quietly checks that file in the background. When I ban a new outfit or approve a new pack, every player gets it the next time they start the game. No reinstall, no download, nothing to do.

No internet? No problem. The mod keeps working from its last downloaded copy, and worst case it falls back to the lists built into it. It can never break or empty out.

## Join my Discord

Got a sprite you want reviewed, found a bug, or just want to hang out with players who love this game the way it was written? Come by:

**[discord.gg/QcE3YRPWk4](https://discord.gg/QcE3YRPWk4)**

## Install

1. Download the latest zip from the [Releases](../../releases) page.
2. Extract it into your MAS `game/Submods/` folder.

You should end up with this:

```
game/Submods/PureHeart-Submod/game/PureHeart_filter.rpy
game/Submods/PureHeart-Submod/game/PureHeart_gifts.rpy
game/Submods/PureHeart-Submod/game/PureHeart_lists.rpy
game/Submods/PureHeart-Submod/game/PureHeart_submod.rpy
game/Submods/PureHeart-Submod/game/PureHeart_thanks.rpy
game/Submods/PureHeart-Submod/game/PureHeart_topics.rpy
```

3. Start the game. Monika will thank you the first time.


## Talk -> More -> Twilight

Pure Heart adds its own topic category with four conversations, unlocked as your affection grows:

- What do you think about explicit content?
- How did those outfits make you feel? (Monika remembers whether you ever saw them)
- What does wholesome love mean to you?
- About the Creator

## Questions people might have

**Where did outfit X go?**
Either it's on the block list or it was never on the allow list. The mod works as a whitelist: an outfit has to be approved to stay. That's the only way to be sure nothing slips through.

**One of my wholesome outfits is missing.**

That's expected. Pure Heart only allows outfits I've personally reviewed, so clothes from spritepacks I haven't checked yet stay hidden until they're approved. Share the sprite in my [Discord server](https://discord.gg/QcE3YRPWk4) and I'll verify it. Once its id is on the keep list, every player gets it automatically through the online update.

**I made a wholesome spritepack. Can it be allowed?**

Yes, that's what the GitHub lists are for. Post it in my [Discord server](https://discord.gg/QcE3YRPWk4) and I'll review the pack. If the outfits are safe, the ids go on the keep list and every player gets them automatically.


**How do I uninstall?**
Delete the `game/Submods/PureHeart-Submod` folder. MAS regenerates its sprite data on the next launch.

## Credits

- Outfits that stay in the game come from community spritepacks Thank you for keeping Monika's wardrobe wholesome.
- Monika After Story is made by the MAS team, and DDLC by Team SALVATO. This mod wouldn't exist without them.
- Mod, lists and loader maintained by [Twilight](https://github.com/Twil1ght-L4D2).

Written out of genuine love for this game and its characters, not out of a wish to control anyone else's fandom.
