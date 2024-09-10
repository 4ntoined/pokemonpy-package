## pokemonpy-package log

### v0.3.0
Title: **Double Battles**

Date: 2024 change the pokemon.py gameversion

here's what im thinking for double battles stuff

- implement semifield (big step, im already upset about it)
- invent PPS (Pokémon Positioning System), orient 4 Pokémon in a battle *
- rework moves.py to target one or two or all mons
- rework move info to report range
- rework game to have player select a target(s)
- spread damage in the damage calculation
- have the player manage 2 active Pokémon at once
- update the battle UI, status screen to account for 4 Pokémon

*
i am thinking that this "orientation" idea is technically moot for doubles.
Moves either target (1) one of the two opponents, (2) both opponents at once [rock slide],
(3) the user's ally [helping hand], (4) both the user and its ally [Life Dew],
(5) all Pokémon on the field [Perish Song]
In doubles, targeting has nothing to do with positioning, just allegiance.
But this is an important thing to do anyway for Triple+ Battles,
where some Pokémon are out of range of other Pokémon's moves because of where they are in
"physical" space.


Thinking about:

#### Major
- double battles 0.3.0
- abilities 0.4.0
- defog + grounding/ungrounding + hazards + status screen completion 0.5.0
- triple+ battles
- rotation battles

#### Minor
- move unification
- snow
- battle texts
- savefile versioning
- we start the battle with the player's lead pokémon
even if that pokémon is fainted...
- multiparty tweaks:
- opponent party setting should use all of player's parties for selection,
- allow user to equip an empty party, so that you can load mons into a fresh party
        - proof the game for in case the player has equipped an empty party
- allow user to choose which party loaded mons are stored in

### v0.2.6
Title: **Pre-Doubles**

Date: 2024 September 6
* UPDATE: Added a switch to change the CPU trainer's logic + a new logic option: random.
* UPDATE: Parties preloaded via the config file are loaded into the player's party list
before the game-generated starter parties.
The first pre-loaded party will be equipped when the game starts.
* UPDATE: The player can now rename their parties.
* UPDATE: Trainer call-outs updated and randomized.
* UPDATE: New cheat code introduced.
* FIXED: The way the game kept track of how many parties the player has was broken. Fixed it.
* TECHNICAL UPDATE: Switching Pokémon in battle is a function now.

### v0.2.5
Title: **Moves ((Part 1))**

Date: 2024 August 18
* UPDATE: Big focus on moves.
	* 100+ new moves with a focus on signature moves and status moves.
	* Updated/standardized move descriptions.
	* Some new move mechanics.
		* Terrain Pulse - changes type on terrain
		* Crush Grip - does damage based on target's remaining HP
		* Chloroblast - user loses 1/2 max HP in recoil
		* Focus Energy - Pokémon can get pumped, increased chance of landing critical hits
		* Revelation Dance - changes type based on user's primary type
		* Collision Course/Electro Drift - damage boost for supereffective hits
		* Scald/Scorching Sands/Steam Eruption - non-Fire-type moves that can thaw frozen Pokémon
		* Fickle Beam - 30% chance to double in power
		* Electro Shot - 2-turn move that boosts Special Attack on first turn AND charges immediately in rain
		* Hydro Steam/Psyblade - move-specific damage boost in Sun/on Electric Terrain
		* Ruination/Nature's Madness/Super Fang - damage equal to half of target's remaining HP
		* Shore Up - The user recovers more HP in sandstorm
	* Textwrap in move descriptions.
	* [moves] main menu option prints descriptions of all moves.
	* Add moves by name with Move Tutor
* FIXED: Psychic Terrain now protects grounded Pokémon from priority moves.
* FIXED: Toxic used by Poison-types bypasses accuracy check to always hit.
* TECHNICAL UPDATE: The saved party featured in the [game demo](https://youtu.be/0SFg-sSOZBY?t=438) is now included in the package: src/pokemonpy/saves/demoteam.sav
* TECHNICAL UPDATE: Readme is updated with more involved sample scripts.

### v0.2.4
Date: 2024 June 27
* UPDATE: Some new moves.

### v0.2.3
Date: 2024 June 25
* FIXED: Reverted the battle UI change because I realized I didn't like it.
* FIXED: Fighting-type moves were super-effective against Fire-types instead of Normal-types. Fixed this.
* FIXED: Typo in Fake Out description has been corrected.
* UPDATE: The game will no longer break if it can't find the config file.
* UPDATE: The game now reports Pokémon HP when Pokémon heal or take indirect damage.
* UPDATE: Added Goku.
* TECHNICAL UPDATE: The game itself is now a class/function. 
* TECHNICAL UPDATE: Added a script to run the game (scripts/rungame.py). 

### v0.1.2
Date: 2024 April 20
* UPDATE: Pokemon.py now has a variable to hold the current game version.
Prints current version when 'about' is entered on the main menu.
* UPDATE: Hall of Fame banner has been updated.
* UPDATE: New cheat code introduced.
* UPDATE: You can now close the game. Enter 'quit' on the main menu to close the game.
* UPDATE: You can change the name of your opponent in the 'Battle!' battle.
* UPDATE: Main menu changes. Showing previously hidden options now.
* UPDATE: Game settings are pre-recorded in 'config' files. Basic ones are stored in the configurations/ directory.
The game checks for 'config.txt', so edit that file or overwrite it with the preferred config file.
* UPDATE: Battle UI takes up the full extent of the game width.
* FIXED: The nerf by Grassy Terrain of Earthquake is reported in the damage readouts now.

### v0.1.1
Date: 2024 March 29
* UPDATE: Added Name Rater feature to change Pokémon names, Mint Store to
  change Pokémon natures, and the Gender Editor to change Pokémon gender.
  All are found in the Training from the main menu.

### v0.1.0
Date: 2024 March 29
* UPDATE: The game has achieved an arbitrary level of completeness.

