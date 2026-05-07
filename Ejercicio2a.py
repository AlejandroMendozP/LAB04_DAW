
from chessPictures import *
from interpreter import draw

blackknight = knight.negative()

top_row = knight.join(blackknight)

botomrow = blackknight.join(knight)

finalpicture = botomrow.up(top_row)


draw(finalpicture)