from importlib import resources as impr
from . import texter
from . import moves
from . import dexpoke
from . import somemons
from . import trainerai
#import os
dexpath = impr.files(somemons) / 'somemons.dat'
dex, garbage = dexpoke.pokedexer(dexpath)
mov = moves.mov

#pokedex = dexpoke.pokedexer('somemons.dat')
