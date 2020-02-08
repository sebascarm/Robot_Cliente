# -*- coding: utf-8 -*-

###########################################################
### VENTANA PRINCIPAL 2.0                               ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 08/02/2020                                          ###
### Cracion                                             ###
###########################################################

from winform.label      import Label
from winform.textbox    import Textbox

import configparser     #lector de archivos de configuracion

CONFIGURACION = configparser.ConfigParser()
CONFIGURACION.read('./config.cfg')
CONEXION = CONFIGURACION['CONEXION']
SERVIDOR = CONEXION['SERVIDOR']
PUERTO   = CONEXION['PUERTO']

class Form_Principal(object):
    def __init__(self, C_Form):
        '''Se Requiere el objeto Formulario'''
        self.labl_titulo  = Label(C_Form)
        self.labl_ip      = Label(C_Form)
        self.text_ip      = Textbox(C_Form)
        self.labl_port    = Label(C_Form)
        self.text_port    = Textbox(C_Form)
        self.bot_conectar = Button(C_Form)
        # objetos sin graficos

        #
        self.eventos      = '' # se establece luego

        # Configuracion
        self.labl_titulo.config("Configuración", 10, 10, 140, 25, "centrada")
        self.labl_titulo.set_textSize(16)
        self.labl_ip.config("IP", 10, 40+4, 26, 12,"derecha")
        self.text_ip.config(SERVIDOR, 40, 40, 110, 18)
        self.labl_port.config("Port", 10, 60+4, 26, 12,"derecha")
        self.text_port.config(PUERTO, 40, 60, 110, 18)
        self.bot_conectar.config("Conectar", 10, 90, 140 , 20)
        
    def Establecer_Eventos(self, C_Eventos):
        self.eventos = C_Eventos

        # Configuracion de eventos
        #self.bot_conectar.accion(self.conectar)

