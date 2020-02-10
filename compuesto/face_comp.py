
# -*- coding: utf-8 -*-

###########################################################
### FACE COMPUESTO V1.2                                 ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 10/02/2020                                          ###
### Envio de angulo a retornar                          ###
### Cracion nuevamente                                  ###
###########################################################

from componentes.cliente_tcp  import Cliente_TCP
from componentes.thread_admin import ThreadAdmin
from componentes.timer        import Timer
from ia.face_detect2          import Face_Detect2

import time
import queue # cola o pila

class Face_Comp(object):
    def __init__(self):
        self.tcp         = Cliente_TCP()
        self.fdetect     = Face_Detect2()
        self.th_detect   = ThreadAdmin()
        self.host        = ''
        self.ob_imagen   = ''
        self.ob_label_fps = ''
        self.cola_imagen = queue.LifoQueue()
        self.conectado   = False # Estado de la conexion
        self.tiempo      = Timer()

    def config(self, Host, Ob_Imagen, Ob_label_fps):
        ''' Se requiere IP del Servidor y Objeto Imagen'''
        self.host =Host
        self.ob_imagen = Ob_Imagen
        self.ob_label_fps = Ob_label_fps
        self.tcp.config(Host, 50001, self.__call_conexion, Binario=True)
        self.fdetect.config(Callback_Imagen=self.__call_imagen)
        self.fdetect.config_callback(Func_Unica=self.__call_posdetect)
            
    def iniciar(self):
        print("iniciar")
        self.tiempo.iniciar()
        self.tcp.conectar()

    def stop(self):
        self.tcp.desconectar()
        self.th_detect.close()
        
    def __call_conexion(self, Codigo, Mensaje):
        ''' recepcion de datos binarios tpc'''
        # Conectado
        if Codigo == 2:
            self.conectado = True
            self.th_detect.start(self.__th_detector, '', 'DETECTOR', enviar_ejecucion=True)
        # Desconecado
        if Codigo == 0:
            self.conectado = False
        # Recepcion de datos
        if Codigo == 4:
            self.cola_imagen.put(Mensaje) # encolamos la imgen recibida

    def __call_imagen(self, cv_imagen):
        ''' recepcion de imagen procesada por el detector para insertar en el objeto imagen'''
        self.ob_imagen.imagen_cv(cv_imagen)

    def __call_posdetect(self,X , Y):
        print(X, Y)

    def __th_detector(self, run):
        ''' envia a analizar las imagenes que entran en cola '''
        while run.value:
            if self.cola_imagen.qsize() > 0:
               #print(tiempo.fps())
               self.ob_label_fps.set_text(str(self.tiempo.fps()))
               imag = self.cola_imagen.get()
               self.fdetect.imagen(imag)
            time.sleep(0.01)

