# -*- coding: utf-8 -*-

###########################################################
### FACE COMPUESTO V1.6                                 ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 21/02/2020                                          ###
### Evento estado de conexion                           ###
### Revision de reconexion                              ###
### Desconexion                                         ###
### Mejora en envio de los FPS                          ###
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
        self.conectado = False      # Estado de la conexion
        self.tiempo = Timer()
        self.evento_conexion = ''   # Evento que devuelve el estado de la conexion

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

    def config_eventos(self, evento_conexion=''):
        """evento_conexion: Funcion que devuelve True o False cuando conecta o desconecta
           Ej: def evento(Estado)
        """
        self.evento_conexion = evento_conexion

    def iniciar(self):
        self.tiempo.iniciar()
        self.tcp.iniciar()

    def desconectar(self):
        self.tcp.desconectar()
        self.th_detect.close()

    def __call_conexion(self, codigo, mensaje):
        """ recepcion de datos binarios del servidor tcp"""
        # Conectado
        if codigo == 2:
            self.conectado = True
            self.th_detect.start(self.__th_detector, '', 'DETECTOR', enviar_ejecucion=True)
            self.evento_conexion(True) # Devolvemos conectado
        # Desconecado
        elif codigo == 0:
            self.conectado = False
            self.evento_conexion(False)    # Devolvemos desconectado
        # Recepcion de datos
        elif codigo == 4:
            self.cola_imagen.put(mensaje)  # encolamos la imgen recibida
        # Errores
        elif codigo == -1:
            self.conectado = False
            self.evento_conexion(False)  # Devolvemos desconectado
        # Otros mensajes
        else:
            if codigo != 3: # 3 es envio de mensajes
                print("MEN: " + str(codigo) + " " + str(mensaje))

    def __call_imagen(self, cv_imagen):
        """ recepcion de imagen procesada por el detector para insertar en el objeto imagen"""
        self.ob_imagen.imagen_cv(cv_imagen)

    def __th_detector(self, run):
        """ envia a analizar las imagenes que entran en cola """
        while run.value:
            if self.cola_imagen.qsize() > 0:
                # print(tiempo.fps())
                self.ob_label_fps.set_text("FPS: " + str(round(self.tiempo.fps(), 2)))
                imag = self.cola_imagen.get()
                self.fdetect.imagen(imag)
            time.sleep(0.01)

    def __call_posdetect(self, x, y):
        # print(x, y)
        modulo  = "FACE"
        comando = "CENTRAR"
        valor   = str(x) + "|" + str(y)
        self.tcp.enviar(modulo + "|" + comando + "|" + valor)
