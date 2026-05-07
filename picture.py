from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

  def horizontalMirror(self):
        nueva_img = self.img[::-1]
        return Picture(nueva_img)

  def negative(self):
    nueva_img = []
    for fila in self.img:
       nueva_fila = ""
       for caracter in fila:
          nuevo_caracter = self._invColor(caracter)
          nueva_fila+=nuevo_caracter
       nueva_img.append(nueva_fila)
    return Picture(nueva_img)

  def join(self, p):
    nueva_img = []
    x = 0
    while x < 58:
       concatenacion = ""
       concatenacion += self.img[x] + p.img[x]
       nueva_img.append(concatenacion)
       x += 1
    return Picture(nueva_img)

  def up(self, p):
    nueva_img = p.img + self.img
    return Picture(nueva_img)

  def under(self, p):
    nueva_img = []
    for fila in range(len(self.img)):
       nueva_fila = ""
       for columna in range(len(self.img[fila])):
          if (self.img[fila][columna] == " "): nueva_fila += p.img[fila][columna]
          else: nueva_fila += self.img[fila][columna]
       nueva_img.append(nueva_fila)
    return Picture(nueva_img)
  
  def horizontalRepeat(self, n):
    nueva_img = []
    for fila in self.img:
        fila_repetida = fila * n 
        nueva_img.append(fila_repetida)
    return Picture(nueva_img)

  def verticalRepeat(self, n):
    nueva_img = self.img * n
    return Picture(nueva_img)

  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
