
# -*- coding: utf-8 -*-

###########################################################
### FACE COMPUESTO V1.1                                 ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 08/02/2020                                          ###
### Cracion nuevamente                                  ###
###########################################################

from componentes.cliente_tcp  import Cliente_TCP
from componentes.thread_admin import ThreadAdmin
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
        self.cola_imagen = queue.LifoQueue()

    def config(self, Host, Ob_Imagen):
        ''' Se requiere IP del Servidor y Objeto Imagen'''
        self.host =Host
        self.ob_imagen = Ob_Imagen
        self.tcp.config(Host, 50001, self.__call_conexion, Binario=True)
        self.fdetect.config(Callback_Imagen=self.__call_imagen)
        fdetec.config_callback(Func_Cuadro=self.__call_cuadro)
            
    def iniciar(self):
        self.tcp.conectar()
        
    def __call_conexion(self, Codigo, Mensaje):
        ''' recepcion de datos binarios tpc'''
        # Conectado
        if Codigo == 2:
            self.th_detect.start(self.__th_detector, '', 'DETECTOR', enviar_ejecucion=True)
        # Recepcion de datos
        if Codigo == 4:
            self.cola_imagen.put(Mensaje) # encolamos la imgen recibida

    def __call_imagen(self, cv_imagen):
        ''' recepcion de imagen procesada por el detector para insertar en el objeto imagen'''
        self.ob_imagen.imagen_cv(cv_imagen)

    def __call_cuadro(self,X , Y, Ancho, Alto):
        pass

    def __th_detector(self, run):
        ''' envia a analizar las imagenes que entran en cola '''
        while run.value:
            if self.cola_imagen.qsize() > 0:
               #print(tiempo.fps())
               imag = self.cola_imagen.get()
               self.fdetect.imagen(imag)
            time.sleep(0.01)
