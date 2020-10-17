# -*- coding: utf-8 -*-

###########################################################
### VENTANA PRINCIPAL 2.2                               ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 26/02/2020                                          ###
### Objetos no graficos fuera de esta clase             ###
### Eventos de fase conection                           ###
### Cracion                                             ###
###########################################################

from winform.label      import Label
from winform.textbox    import Textbox
from winform.button     import Button
from winform.imagen     import Imagen
# Objetos compuestos
# from componentes.comunicacion import Comunicacion
# from compuesto.face_comp import Face_Comp

import configparser     # lector de archivos de configuracion

import os
# print(os.path.join(os.getcwd(), '../config.cfg'))
CONFIGURACION = configparser.ConfigParser()
# CONFIGURACION.read('./config.cfg')
CONFIGURACION.read('../config.cfg')  # pycharm requiere especificar bien la ruta
CONFIGURACION.read('config.cfg')
CONEXION = CONFIGURACION['CONEXION']
SERVIDOR = CONEXION['SERVIDOR']
PUERTO   = CONEXION['PUERTO']

PUERTO2  = str(50002)


class Form_Principal(object):
    def __init__(self, C_Form):
        """Se Requiere el objeto Formulario"""
        self.labl_titulo  = Label(C_Form)
        self.labl_ip      = Label(C_Form)
        self.text_ip      = Textbox(C_Form)
        self.labl_port    = Label(C_Form)
        self.text_port    = Textbox(C_Form)
        self.labl_port2   = Label(C_Form)
        self.text_port2   = Textbox(C_Form)
        self.bot_conectar = Button(C_Form)
        self.bot_conec_img = Button(C_Form)
        self.box_imagen   = Imagen(C_Form)
        self.label_fps    = Label(C_Form)
        # objetos sin graficos
        # self.tpc_cli      = Comunicacion()
        # self.face_comp    = Face_Comp()

        # Configuracion
        self.labl_titulo.config("Configuración", 40, 10, 110, 25, "centrada")
        self.labl_titulo.set_textSize(16)
        self.labl_ip.config("IP", 10, 40+4, 26, 12,"derecha")
        self.text_ip.config(SERVIDOR, 40, 40, 110, 18)
        self.labl_port.config("Port", 10, 60+4, 26, 12,"derecha")
        self.text_port.config(PUERTO, 40, 60, 110, 18)
        self.labl_port2.config("Port", 10, 80 + 4, 26, 12, "derecha")
        self.text_port2.config(PUERTO2, 40, 80, 110, 18)
        self.bot_conectar.config("Conectar", 40, 120, 110 , 20)
        self.bot_conec_img.config("Conectar Img", 40, 150, 110, 20)
        self.label_fps.config("FPS Procesado: ", 200, 80, 100, 18)
        self.box_imagen.config(200,100,320,240)


