# Anybody here play Pokémon?
Just me? That's fine.

## The game:

[github.com/4ntoined/pokemonpy](https://github.com/4ntoined/pokemonpy)

## To play the game:

```
myterminal$ python3
python$ import pokemonpy.pokemon as pk
python$ game1 = pk.game()
python$ game1.startgame()
```

## To play with a particular config file:

```
myterminal$ python3
python$ import pokemonpy.pokemon as pk
python$ cpath = 'configurations/config.txt'
python$ game2 = pk.game()
python$ game2.startgame(cpath)
```

## Else:

```
pokemonpy.pokemon.game.startgame(
    configname='config.txt', mutegame=None, username=None, opponentname=None, nparty=None, nstart=None, gw=None)

mutegame - bool, set to True to skip the pre-game text
username - str, your name
opponentname - str, the name of the rival trainer
nparty - int, number of Pokémon parties you start with
nstart - int, number of Pokémon in each party
gw - int, sets the length of banners and headers
```

