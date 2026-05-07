from chessPictures import *
from interpreter import draw

casillero_blanco = Picture(SQUARE)
casillero_negro = casillero_blanco.negative()

peon = Picture(PAWN)
torre = Picture(ROCK)
caballo = Picture(KNIGHT)
alfil = Picture(BISHOP)
reina = Picture(QUEEN)
rey = Picture(KING)

casilleroBT = torre.under(casillero_blanco)
casilleroNT = torre.under(casillero_negro)
casilleroBC = caballo.under(casillero_blanco)
casilleroNC = caballo.under(casillero_negro)
casilleroBA = alfil.under(casillero_blanco)
casilleroNA = alfil.under(casillero_negro)
casilleroBRN = reina.under(casillero_blanco)
casilleroNRN = reina.under(casillero_negro)
casilleroBRY = rey.under(casillero_blanco)
casilleroNRY = rey.under(casillero_negro)
casilleroBP = peon.under(casillero_blanco)
casilleroNP = peon.under(casillero_negro)

filaPiezas1 = casilleroNT.join(casilleroBC).join(casilleroNA).join(casilleroBRN).join(casilleroNRY).join(casilleroBA).join(casilleroNC).join(casilleroBT)
filaPiezas2 = filaPiezas1.negative()
pareja = casilleroBP.join(casilleroNP)
filaPeones1 = pareja.horizontalRepeat(4)
filaPeones2 = filaPeones1.negative()
fila1 = casillero_blanco.join(casillero_negro).horizontalRepeat(4)
fila2 = fila1.negative()
filasSinPiezas = fila2.up(fila1)

tablero = filaPiezas1.up(filaPeones1).up(filasSinPiezas.verticalRepeat(2)).up(filaPeones2).up(filaPiezas2)

draw(tablero)