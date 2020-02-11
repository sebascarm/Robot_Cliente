# Esto es para poder hacer el from desde un nivel atras y funciona con launch.json
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from componentes.comunicacion import Comunicacion
import time

serv = Comunicacion()

def callback(codigo, mensaje):
    print("CALL: ", codigo, mensaje)
    if codigo == 2:
        for i in range(25000):
            serv.enviar("m" + str(i))


serv.config("127.0.0.1", cliente=False, callback=callback)
serv.config_packet("<", ">", 100)
serv.iniciar()

time.sleep(1000)
