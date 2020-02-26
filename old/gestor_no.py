# -*- coding: utf-8 -*-

###########################################################
### Clase GESTOR CLI DE COMUNICACION ENTRE COMP  V1.0   ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 25/02/2020                                          ###
### Creacion de clase                                   ###
###########################################################

from componentes.comunicacion import Comunicacion
from compuesto.face_comp import Face_Comp
# Para visualizar
from forms.form_principal import Form_Principal


class Gestor_cli(object):
    def __init__(self, c_objetos):
        # type: (Form_Principal)->None  # ejemplo ty_ (int, int)
        self.conexion      = False        # Estado de la conexion
        self.objeto        = c_objetos
        self.tcp_gestor    = Comunicacion()
        self.host          = "127.0.0.1"
        self.log           = self.__log_default  # Para configurar log
        # Elementos de gestion
        self.face_analis   = Face_Comp()
        self.fun_conexion  = ''         # devulve ele estado de la conexion

    def config(self, host, evento_conexion):
        """ host: IP del servidor
            evento_conexion devuelve el estado de la conexion
        """
        self.host = host
        self.tcp_gestor.config(host, callback=self.__call_conexion)
        # Modulos de gestion
        self.face_analis.config(host, 50002, self.objeto.box_imagen, self.objeto.label_fps, self.enviar)
        self.face_analis.config_eventos(self.__evento_face)
        self.fun_conexion = evento_conexion

    def config_log(self, Log):
        """posibilidad de configurar clase Log(Texto, Modulo)"""
        self.log = Log.log

    def conectar(self):
        self.log("INICIANDO GESTOR CLIENTE", "GESTOR-CLI")
        # Gestor
        self.tcp_gestor.iniciar()

    def desconectar(self):
        self.log("DESCONECTAR GESTOR CLIENTE", "GESTOR-CLI")
        # Gestor
        self.tcp_gestor.desconectar()

    def conectar_face(self):
        #self.log("INICIANDO GESTOR CLIENTE", "GESTOR-CLI")
        self.face_analis.iniciar()

    def desconectar_face(self):
        #self.log("DESCONECTAR GESTOR CLIENTE", "GESTOR-CLI")
        self.face_analis.desconectar()

    ############################
    ### ENVIO DE DATOS       ###
    ############################
    def enviar(self, modulo, comando, valor):
        mensaje = modulo + "|" + comando + "|" + valor
        self.tcp_gestor.enviar(mensaje)

    ############################
    ### RECEPCION DE DATOS   ###
    ############################
    def __call_conexion(self, codigo, mensaje):
        if codigo == 2:     # Conectado
            self.log("CONECTADO A GESTOR SERVIDOR", "GESTOR-CLI")
            self.conexion = True
            self.fun_conexion(True)
        if codigo == 0:     # Desconectado
            self.conexion = False
            self.fun_conexion(False)

    def __evento_face(self, estado):


    # Log por defecto
    def __log_default(self, Texto, Modulo):
        print(Texto)


