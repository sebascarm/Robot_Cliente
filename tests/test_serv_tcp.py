# Esto es para poder hacer el from desde un nivel atras y funciona con launch.json
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import time
from componentes.comunicacion import Comunicacion

serv = Comunicacion()

def callback(codigo, mensaje):
    print("CALL: ", codigo, mensaje)

serv.config("127.0.0.1",Cliente=False ,Callback=callback)
serv.config_packet("<",">",100)
serv.iniciar()

time.sleep(1000)