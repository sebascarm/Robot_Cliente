# Esto es para poder hacer el from desde un nivel atras y funciona con launch.json
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from componentes.comunicacion import Comunicacion
import time

cli = Comunicacion()

def callback(codigo, mensaje):
    print("CALL: ", codigo, mensaje)


cli.config("127.0.0.1", cliente=True, callback=callback)
cli.config_packet("<", ">", 100)
cli.iniciar()

time.sleep(1000)
