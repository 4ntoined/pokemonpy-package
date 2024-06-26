# Anybody here play Pokémon?
Just me? That's fine.

This program is a text-based game that simulates Pokémon and Pokémon battles and runs right in the terminal.
For a more detailed description of the game, check out [game_blurb.md](https://github.com/4ntoined/pokemonpy/blob/master/documentation/game_blurb.md).
For a demonstration of how to play the game, check out [this YouTube video](https://youtu.be/0SFg-sSOZBY) (and like and comment and subscribe).
The packaged version of the game is maintained here: https://github.com/4ntoined/pokemonpy-package.

## Installing the game
Installing and playing the game requires (1) access to the command line and (2) Python 3.

#### Access to the command line/terminal:
   - Search your computer for 'terminal' or 'command line'.
   - On Windows, you'll probably want to use PowerShell and NOT the Command Prompt (cmd.exe).
   - Alternatively, there is [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install), which gives you a Linux-like command line environment, if you're will to jump through a few hoops. This is my preferred way to play in Windows as I have no idea how to use PowerShell or CMD.
#### Python:
   - Python 3.7(ish) or later
   - https://www.python.org
   - For Windows players check out: https://learn.microsoft.com/en-us/windows/python/beginners

### pip
The game is available on the Python Package Index [(package here)](https://pypi.org/project/pokemonpy/) and can be installed via [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/):

`pip install pokemonpy`

### conda
The game is also available as a package through the [Anaconda distribution](https://www.anaconda.com/data-science-platform) of Python [(package here)](https://anaconda.org/antoi/pokemonpy) and can be installed with [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html):

`conda install antoi::pokemonpy`

## Starting the game
With the package installed, you can start the game using the `rungame.py` script in the `scripts` folder:

`python3 rungame.py`

You can give the script some optional arguments when you call it:

```
python3 rungame.py -m -c config_file_path -n "your name" -o "rivals name" -w how_big_to_display_the_game -p number_of_starter_parties -s number_of_pokémon_per_party`

-m to mute the game start-up
-c to tell the game to use a particular configuration file
-n to set your name, used to display in battles
-o to set the name of the rival trainer in the Battle! mode.
-w to set the length of banners and headers throughout the game, defaults to 64 I think
-p to set the number of parties you start with
-s to set the number of Pokémon in each of those parties
-h to have all of this told to you again but by python
```

Alternatively, you can:

1. start a live session of Python
2. import the package, initialize the game object, and start the game:

```
python3
import pokemonpy.pokemon as pk
game1 = pk.game()
game1.startgame()
```

The options for the startgame() function:

```
pokemonpy.pokemon.game.startgame(
    configname='config.txt', mutegame=(True or False), username="Your Name", opponentname="Op Name", nparty=1, nstart=6, gw=64)

configname - str, to have the game use a particular configuration file
mutegame - bool, set to True to skip the pre-game text
username - str, your name
opponentname - str, the name of the rival trainer
nparty - int, number of Pokémon parties you start with
nstart - int, number of Pokémon in each party
gw - int, sets the length of banners and headers
```

## Some fun things to try with the package

```
from pokemonpy.base_pokemon import *
parties, fields = maker(2,6,2)
bb = battle(parties[0],parties[1],fields[0],usr_name='Your Name',cpu_name='The Ops')
bb.startbattle()
```

That's a Pokémon battle in 4 lines. I'm a legend.

Try:
```
from pokemonpy.base_pokemon import *
parties, fields = maker(2,6,2)
print_party(parties[0])
parties[0][0].summary()
parties[0][0].appraisal()
parties[0][0].save('poke.sav')
```

