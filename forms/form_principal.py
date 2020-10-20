# -*- coding: utf-8 -*-

###########################################################
### VENTANA PRINCIPAL 2.4                               ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 20/10/2020                                          ###
### Agregado de sensores
### Redibujado                                          ###
### Objetos no graficos fuera de esta clase             ###
### Eventos de fase conection                           ###
### Cracion                                             ###
###########################################################

from winform.label      import Label
from winform.textbox    import Textbox
from winform.button     import Button
from winform.imagen     import Imagen
from winform.checkbox   import Checkbox
from winform.compasbox  import Compasbox
from winform.progress   import Progress

# Objetos compuestos
# from componentes.comunicacion import Comunicacion
# from compuesto.face_comp import Face_Comp

import configparser     # lector de archivos de configuracion

import os
# print(os.path.join(os.getcwd(), '../config.cfg'))
CONFIGURACION = configparser.ConfigParser()
CONFIGURACION.read('config.cfg')
CONEXION = CONFIGURACION['CONEXION']
SERVIDOR = CONEXION['SERVIDOR']
PUERTO   = CONEXION['PUERTO']

PUERTO2  = str(50002)

class Form_Principal(object):
    def __init__(self, C_Form):
        """Se Requiere el objeto Formulario"""
        self.labl_titulo     = Label(C_Form)
        self.labl_ip         = Label(C_Form)
        self.text_ip         = Textbox(C_Form)
        self.labl_port       = Label(C_Form)
        self.text_port       = Textbox(C_Form)
        self.labl_port2      = Label(C_Form)
        self.text_port2      = Textbox(C_Form)
        self.bot_conectar    = Button(C_Form)
        self.bot_conec_img   = Button(C_Form)
        self.bot_guardar     = Button(C_Form)
        self.labl_sensores   = Label(C_Form)
        # sensores
        self.chbox_sens_cent = Checkbox(C_Form)
        self.text_speed_cent = Textbox(C_Form)
        self.bot_update_cent = Button(C_Form)
        self.chbox_sens_izq  = Checkbox(C_Form)
        self.text_speed_izq  = Textbox(C_Form)
        self.bot_update_izq  = Button(C_Form)
        self.chbox_sens_der  = Checkbox(C_Form)
        self.text_speed_der  = Textbox(C_Form)
        self.bot_update_der  = Button(C_Form)
        self.chbox_sens_bru  = Checkbox(C_Form)
        self.text_speed_bru  = Textbox(C_Form)
        self.bot_update_bru  = Button(C_Form)
        # Lado centrar
        self.label_fps       = Label(C_Form)
        self.box_imagen      = Imagen(C_Form)
        self.label_prog_cent = Label(C_Form)
        self.prog_cent       = Progress(C_Form)
        self.label_prog_izq  = Label(C_Form)
        self.prog_izq        = Progress(C_Form)
        self.label_prog_der  = Label(C_Form)
        self.prog_der        = Progress(C_Form)
        self.label_comp_der  = Label(C_Form)
        self.compbox         = Compasbox(C_Form)

        # objetos sin graficos
        # self.tpc_cli      = Comunicacion()
        # self.face_comp    = Face_Comp()

        # Configuracion
        self.labl_titulo.config("Configuración", 40, 10, 120, 25, "centrada")
        self.labl_titulo.set_textSize(16)
        self.labl_ip.config("IP", 10, 40+4, 26, 12,"derecha")
        self.text_ip.config(SERVIDOR, 40, 40, 120, 18)
        self.labl_port.config("Port", 10, 60+4, 26, 12,"derecha")
        self.text_port.config(PUERTO, 40, 60, 120, 18)
        self.labl_port2.config("Port", 10, 80 + 4, 26, 12, "derecha")
        self.text_port2.config(PUERTO2, 40, 80, 120, 18)
        self.bot_conectar.config("Conectar", 40, 120, 120, 20)
        self.bot_conec_img.config("Conectar Img", 40, 150, 120, 20)
        self.bot_guardar.config("Guardar", 40, 180, 120, 20)
        # sensores titulo
        self.labl_sensores.config("Sensores", 40, 220, 120, 25, "centrada")
        self.labl_sensores.set_textSize(12)
        # sensores
        self.chbox_sens_cent.config("Sonico Central", 40, 260, 120, 18)
        self.text_speed_cent.config("1", 40, 280, 120, 18)
        self.bot_update_cent.config("Update", 40, 300, 120, 18)
        self.chbox_sens_izq.config("Sonico Izquierdo", 40, 340, 120, 18)
        self.text_speed_izq.config("1", 40, 360, 120, 18)
        self.bot_update_izq.config("Update", 40, 380, 120, 18)
        self.chbox_sens_der.config("Sonico Derecho", 40, 420, 120, 18)
        self.text_speed_der.config("1", 40, 440, 120, 18)
        self.bot_update_der.config("Update", 40, 460, 120, 18)
        self.chbox_sens_bru.config("Brujula", 40, 500, 120, 18)
        self.text_speed_bru.config("1", 40, 520, 120, 18)
        self.bot_update_bru.config("Update", 40, 540, 120, 18)
        # lado central
        self.label_fps.config("FPS Procesado: ", 200, 20, 100, 18)
        self.box_imagen.config(200, 40, 320, 240)
        self.label_prog_cent.config("Distancia Sonico Central", 200, 300, 320, 18)
        self.prog_cent.config(0, 400, "0", 200, 320, 320, 18)
        self.label_prog_izq.config("Distancia Sonico Izquierdo", 200, 340, 320, 18)
        self.prog_izq.config(0, 400, "0", 200, 360, 320, 18)
        self.label_prog_der.config("Distancia Sonico Derecho", 200, 380, 320, 18)
        self.prog_der.config(0, 400, "0", 200, 400, 320, 18)
        self.label_comp_der.config("Brujula", 200, 420, 320, 18)
        self.compbox.config("180", 200, 440, 120, 120)
