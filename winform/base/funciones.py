
import math #para usar seno y conseno

def Esta_Adentro(rectangulo, coordenadas):
    x, y = coordenadas
    resultado = False
    x1, y1, ancho, alto = rectangulo
    x2 = x1 + ancho
    y2 = y1 + alto
    if (x>x1) and (x<x2) and (y>y1) and (y<y2):
        resultado = True
    return resultado

def Brillo(colorBase, brillo):
    r,g,b = colorBase
    r = r + brillo
    g = g + brillo
    b = b + brillo
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255 
    if r < 0: r = 0
    if g < 0: g = 0
    if b < 0: b = 0 
    resul = r,g,b
    return resul

def AutoBrillo(colorBase, contraste, bw = False):
    r,g,b = colorBase
    colorTotal = r + g + b
    if colorTotal > 382:  # 382 la mitad del brillo
        #Fondo blanco
        brillo = -contraste
    else:
        #Fondo escuro
        brillo = contraste
    if bw:
        r = g = b = int(colorTotal/3)
    r = r + brillo
    g = g + brillo
    b = b + brillo
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255        
    if r < 0: r = 0
    if g < 0: g = 0
    if b < 0: b = 0 
    resul = r,g,b
    return resul


def posLineRadio(x, y, angulo, radio, radio_ini=0):
    ang_correct  = -(angulo-90)
    ang_radianes = math.radians(ang_correct)
    seno         = math.sin(ang_radianes)
    coseno       = math.cos(ang_radianes)
    opuesto      = seno * radio     #radio = hipotenusa
    adyacente    = coseno * radio   #radio = hipotenusa
    x2           = int(x + adyacente)
    y2           = int(y - opuesto)
    if radio_ini == 0:
        return x2,y2
    else:
        #devolver la posicion inicial tambien
        x1, y1 = posLineRadio(x, y, angulo,radio_ini)
        return x1,y1,x2,y2

