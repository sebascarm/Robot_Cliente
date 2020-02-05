# Esto es para poder hacer el from desde un nivel atras y funciona con launch.json
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

# objetos
from winform.screen    import Screen
from winform.form      import Form
from winform.label     import Label 
from winform.imagen    import Imagen 
from ia.face_detect2   import Face_Detect2
from componentes.timer import Timer
from thread_admin import ThreadAdmin
import time

from conexion.cliente_tcp import Cliente_TCP

import queue # cola o pila

RESOLUCION  = 900, 600
COLOR_FORM  = 40, 0, 50
POS_VENTANA = 0, 0

cola     = queue.LifoQueue()
tcp      = Cliente_TCP()
fdetec   = Face_Detect2()
tiempo   = Timer()
th_detec = ThreadAdmin()

# Crear pantalla, objeto unico y principal
#SCREEN = Screen("Test recibir imagen 2", RESOLUCION, 1,1.0)  # enviamos el tamano al inicio
SCREEN = Screen("Test recibir imagen 2", RESOLUCION)  # enviamos el tamano al inicio
FORM1 = Form(SCREEN, "control", RESOLUCION, POS_VENTANA, COLOR_FORM)

label_t = Label(FORM1)
imagen  = Imagen(FORM1)
label_t.config("Titulo", 5, 5, 140, 25, "centrada")
imagen.config(50, 50, 100, 100)

FORM1.dibujar()
label_t.dibujar()
#imagen.dibujar()

#cola.maxsize = 100

def fun_calback(Codigo, Mensaje):
    if  Codigo != 4:
        print("COD: ", Codigo, "Men: ", Mensaje)
    
    if Codigo == 2:
        fdetec.config(Resolucion=(640,480), Callback_Imagen=fun_imagen)
        fdetec.config_callback(Func_Cuadro=fun_cuadro)
        th_detec.start(th_detector, '', 'DETECTOR', enviar_ejecucion=True)

    if Codigo == 4:
        cola.put(Mensaje) # encolamos la imagen recibida
       
def th_detector(run):
    while run.value:
        if cola.qsize() > 0:
           print(tiempo.fps())
           imag = cola.get()
           fdetec.imagen(imag)
        time.sleep(0.01)

def fun_imagen(Imagen):
    imagen.imagen_cv(Imagen)

def fun_cuadro(x, y, ancho, alto):
    pass

tcp.config("192.168.0.34", 50001, fun_calback, Binario=True)
#tcp.config("127.0.0.1", 50001, fun_calback, Binario=True)

tcp.conectar()

SCREEN.loop()
