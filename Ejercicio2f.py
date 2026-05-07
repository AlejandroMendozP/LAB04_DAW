from chessPictures import *
from interpreter import draw

casileroBlanco = Picture(SQUARE)
casilleroNegro = casileroBlanco.negative()

pareja = casilleroNegro.join(casileroBlanco)
fila =  pareja.horizontalRepeat(4)
filaInversa = fila.negative()
tablero = fila.up(filaInversa).up(fila).up(filaInversa)

draw(tablero)