# Esto es para poder hacer el from desde un nivel atras y funciona con launch.json
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

# objetos
from winform.screen    import Screen
from winform.form      import Form
from winform.label     import Label 
from winform.imagen    import Imagen 

from conexion.cliente_tcp import Cliente_TCP

RESOLUCION  = 900, 600
COLOR_FORM  = 40, 0, 50
POS_VENTANA = 0, 0

tcp = Cliente_TCP()

# Crear pantalla, objeto unico y principal
SCREEN = Screen("Test recibir imagen 2", RESOLUCION, 1,1.0)  # enviamos el tamano al inicio
SCREEN.dibujar()
FORM1 = Form(SCREEN, "control", RESOLUCION, POS_VENTANA, COLOR_FORM)

label_t = Label(FORM1)
imagen  = Imagen(FORM1)
label_t.config("Titulo", 10, 10, 140, 25, "centrada")
imagen.config(50, 50, 100, 100)

FORM1.dibujar()
label_t.dibujar()
imagen.dibujar()

def fun_calback(Codigo, Mensaje):
    if  Codigo != 4:
        print("COD: ", Codigo, "Men: ", Mensaje)
    else:
        imagen.imagen_cv(Mensaje)

tcp.config("192.168.0.34", 50001, fun_calback, Binario=True)
tcp.conectar()

SCREEN.loop()
