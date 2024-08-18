## pokemonpy-package log

### v0.3.0
Date: 2024 change the pokemon.py gameversion

Thinking about:
- abilities
- move unification - get spikes working on ceaseless edge
- snow
- save file versioning = compatibility with older versions of the game (movedex)
- grounding/ungrounding pokemon
- status screen completion
- losing a battle has weird text
- defog...

#### Major
- abilities
- double battles
- triple+ battles
- rotation battles
- defog + grounding/ungrounding + hazards + status screen completion

#### Minor
- move unification
- snow
- battle texts

### v0.2.5
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
* UPDATE: Pokemon.py now has a variable to hold the current game version. Prints current version when 'about' is entered on the main menu.
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

