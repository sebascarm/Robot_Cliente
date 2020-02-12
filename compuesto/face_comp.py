# -*- coding: utf-8 -*-

###########################################################
### FACE COMPUESTO V1.3                                 ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 11/02/2020                                          ###
### utilizacion de comunicacion                         ###
### Envio de angulo a retornar                          ###
### Cracion nuevamente                                  ###
###########################################################

from componentes.comunicacion import Comunicacion
from componentes.thread_admin import ThreadAdmin
from componentes.timer import Timer
from ia.face_detect2 import Face_Detect2

import time
import queue  # cola o pila


class Face_Comp(object):
    def __init__(self):
        self.tcp = Comunicacion()
        self.fdetect = Face_Detect2()
        self.th_detect = ThreadAdmin()
        self.host = ''
        self.ob_imagen = ''
        self.ob_label_fps = ''
        self.cola_imagen = queue.LifoQueue()
        self.conectado = False  # Estado de la conexion
        self.tiempo = Timer()

    def config(self, host, ob_imagen, ob_label_fps):
        """ Se requiere IP del Servidor y Objeto Imagen
            Devuelve la imagen y los fps en un objeto label
        """
        self.host = host
        self.ob_imagen = ob_imagen
        self.ob_label_fps = ob_label_fps
        self.tcp.config(host, 50001, binario=True, callback=self.__call_conexion)
        self.fdetect.config(Callback_Imagen=self.__call_imagen)
        self.fdetect.config_callback(Func_Unica=self.__call_posdetect)

    def iniciar(self):
        print("iniciar????")
        self.tiempo.iniciar()
        self.tcp.iniciar()

    def stop(self):
        self.tcp.desconectar()
        self.th_detect.close()

    def __call_conexion(self, codigo, mensaje):
        """ recepcion de datos binarios del servidor tcp"""
        # Conectado
        if codigo == 2:
            self.conectado = True
            self.th_detect.start(self.__th_detector, '', 'DETECTOR', enviar_ejecucion=True)
        # Desconecado
        if codigo == 0:
            self.conectado = False
        # Recepcion de datos
        if codigo == 4:
            self.cola_imagen.put(mensaje)  # encolamos la imgen recibida

    def __call_imagen(self, cv_imagen):
        """ recepcion de imagen procesada por el detector para insertar en el objeto imagen"""
        self.ob_imagen.imagen_cv(cv_imagen)

    def __th_detector(self, run):
        """ envia a analizar las imagenes que entran en cola """
        while run.value:
            if self.cola_imagen.qsize() > 0:
                # print(tiempo.fps())
                self.ob_label_fps.set_text(str(self.tiempo.fps()))
                imag = self.cola_imagen.get()
                self.fdetect.imagen(imag)
            time.sleep(0.01)

    def __call_posdetect(self, x, y):
        print(x, y)
        modulo  = "FACE"
        comando = "CENTRAR"
        valor   = str(x) + "|" + str(y)
        self.tcp.enviar(modulo + "|" + comando + "|" + valor)
