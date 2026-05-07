from pieces import *
from picture import *
from interpreter import draw

king   = Picture(KING)
queen  = Picture(QUEEN)
rook   = Picture(ROCK)
bishop = Picture(BISHOP)
knight = Picture(KNIGHT)
pawn   = Picture(PAWN)
light  = Picture(SQUARE)     
dark   = light.negative()     

WHITE = {'K':king, 'Q':queen, 'R':rook, 'B':bishop, 'N':knight, 'P':pawn}

def square_at(c, color):
    bg = light if color == 'L' else dark
    if c == '.':
        return bg
    piece = WHITE[c.upper()]
    if c.islower():
        piece = piece.negative()
    return piece.under(bg)

def build_row(rank, start):
    sqs = []
    for i, c in enumerate(rank):
        col = start if i % 2 == 0 else ('D' if start == 'L' else 'L')
        sqs.append(square_at(c, col))
    row = sqs[0]
    for sq in sqs[1:]:
        row = row.join(sq)
    return row


position = [
    "r.bqkbnr",  
    "pppp.ppp",  
    "..n.....",  
    "....p...",  
    "...PP...",  
    ".....N..",  
    "PPP..PPP",  
    "RNBQKB.R",  
]
starts = ['L','D','L','D','L','D','L','D']

rows = [build_row(position[i], starts[i]) for i in range(8)]

board = rows[7]
for i in range(6, -1, -1):
    board = board.up(rows[i])

draw(board)