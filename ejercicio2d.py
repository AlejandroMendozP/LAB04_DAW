from interpreter import draw
from chessPictures import *

casillerooscuro = square.negative()

parcasilleros = square.join(casillerooscuro)

filadecasilleros = parcasilleros.horizontalRepeat(4)

draw(filadecasilleros)