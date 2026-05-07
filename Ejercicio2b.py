from chessPictures import *
from interpreter import draw

caballo = Picture(KNIGHT)
fila1 = caballo.join(caballo.negative())
fila2 = fila1.verticalMirror()
resultado = fila2.up(fila1)
draw(resultado)