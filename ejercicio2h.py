
from chessPictures import *
from interpreter import draw

def crear_tablero_italiana():
    
    s = square               
    d = square.negative()  

    
    r_n = rock.negative()
    n_n = knight.negative()
    b_n = bishop.negative()
    q_n = queen.negative()
    k_n = king.negative()
    p_n = pawn.negative()

    r = rock
    n = knight
    b = bishop
    q = queen
    k = king
    p = pawn

  
    row8 = r_n.under(s).join(d).join(b_n.under(s)).join(q_n.under(d)).join(k_n.under(s)).join(b_n.under(d)).join(n_n.under(s)).join(r_n.under(d))

    row7 = p_n.under(d).join(p_n.under(s)).join(p_n.under(d)).join(p_n.under(s)).join(d).join(p_n.under(s)).join(p_n.under(d)).join(p_n.under(s))
    

    row6 = s.join(d).join(n_n.under(s)).join(d).join(s).join(d).join(s).join(d)
    
    row5 = d.join(s).join(d).join(s).join(p_n.under(d)).join(s).join(d).join(s)
    
    row4 = s.join(d).join(b.under(s)).join(d).join(p.under(s)).join(d).join(s).join(d)
    
    row3 = d.join(s).join(d).join(s).join(d).join(n.under(s)).join(d).join(s)
    
    
    row2 = p.under(s).join(p.under(d)).join(p.under(s)).join(p.under(d)).join(s).join(p.under(d)).join(p.under(s)).join(p.under(d))
    

    row1 = r.under(d).join(n.under(s)).join(b.under(d)).join(q.under(s)).join(k.under(d)).join(s).join(d).join(r.under(s))

    tablero = row1.up(row2).up(row3).up(row4).up(row5).up(row6).up(row7).up(row8)
    
    return tablero

if __name__ == '__main__':
    tablero_final = crear_tablero_italiana()
    draw(tablero_final)