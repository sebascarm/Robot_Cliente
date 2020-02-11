""" Prueba de uso de binarios """

# Esto es para poder hacer el from desde un nivel atras y funciona con launch.json
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import time
from conexion.cliente_tcp import Cliente_TCP

tcp = Cliente_TCP()

def fun_calback(Codigo, Mensaje):
    print("COD: ", Codigo, "Men: ", Mensaje)

tcp.config("192.168.0.26", 50001, fun_calback, binario=True)
tcp.conectar()

time.sleep(100)