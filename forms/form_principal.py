# -*- coding: utf-8 -*-

###########################################################
### VENTANA PRINCIPAL 2.6                               ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 16/01/2021                                          ###
### DrawBox y sensores                                  ###
### uso del archivo de configuracion                    ###
### Agregado de sensores                                ###
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
from winform.drawbox    import DrawBox

# Objetos compuestos
# from componentes.comunicacion import Comunicacion
# from compuesto.face_comp import Face_Comp

import config

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
        self.chbox_sens_izq = Checkbox(C_Form)
        self.chbox_sens_der = Checkbox(C_Form)

        self.text_speed_cent = Textbox(C_Form)
        self.bot_update_cent = Button(C_Form)

        self.chbox_sens_bru  = Checkbox(C_Form)
        self.text_speed_bru  = Textbox(C_Form)
        self.bot_update_bru  = Button(C_Form)

        self.label_calibrar = Label(C_Form)
        self.chbox_cal_0    = Checkbox(C_Form)
        self.chbox_cal_90   = Checkbox(C_Form)
        self.chbox_cal_180  = Checkbox(C_Form)
        self.chbox_cal_270  = Checkbox(C_Form)
        self.text_cal_0     = Textbox(C_Form)
        self.text_cal_90    = Textbox(C_Form)
        self.text_cal_180   = Textbox(C_Form)
        self.text_cal_270   = Textbox(C_Form)

        self.chbox_sens_dis = Checkbox(C_Form)
        self.text_speed_dis = Textbox(C_Form)
        self.bot_update_dis = Button(C_Form)

        self.chbox_sens_cam = Checkbox(C_Form)
        self.text_speed_cam = Textbox(C_Form)
        self.bot_update_cam = Button(C_Form)

        self.chbox_ruedas        = Checkbox(C_Form)
        self.label_rued_iz_freno = Label(C_Form)
        self.label_rued_iz_max   = Label(C_Form)
        self.label_rued_iz_min   = Label(C_Form)
        self.label_rued_de_freno = Label(C_Form)
        self.label_rued_de_max   = Label(C_Form)
        self.label_rued_de_min   = Label(C_Form)

        self.text_rued_iz_freno = Textbox(C_Form)
        self.text_rued_iz_max = Textbox(C_Form)
        self.text_rued_iz_min = Textbox(C_Form)
        self.text_rued_de_freno = Textbox(C_Form)
        self.text_rued_de_max = Textbox(C_Form)
        self.text_rued_de_min = Textbox(C_Form)

        self.bot_update_rued  = Button(C_Form)

        self.chbox_motor_cam = Checkbox(C_Form)
        self.text_speed_mot_cam = Textbox(C_Form)
        self.bot_update_mot_cam = Button(C_Form)

        self.chbox_sens_laser = Checkbox(C_Form)
        self.text_speed_laser = Textbox(C_Form)
        self.bot_update_laser = Button(C_Form)

        # Lado centrar
        self.label_fps       = Label(C_Form)
        self.box_imagen      = Imagen(C_Form)

        self.label_prog_dist = Label(C_Form)
        self.prog_dist       = Progress(C_Form)
        self.label_prog_laser= Label(C_Form)
        self.prog_laser      = Progress(C_Form)

        self.label_prog_cent = Label(C_Form)
        self.prog_cent       = Progress(C_Form)
        self.label_prog_izq  = Label(C_Form)
        self.prog_izq        = Progress(C_Form)
        self.label_prog_der  = Label(C_Form)
        self.prog_der        = Progress(C_Form)
        self.label_comp_der  = Label(C_Form)
        self.compbox         = Compasbox(C_Form)

        # Lado Derecho
        self.box_draw        = DrawBox(C_Form)
        # objetos sin graficos
        # self.tpc_cli      = Comunicacion()
        # self.face_comp    = Face_Comp()

        # Configuracion
        self.labl_titulo.config("Configuración", 40, 10, 120, 25, "centrada")
        self.labl_titulo.set_textSize(16)
        self.labl_ip.config("IP", 10, 40+4, 26, 12,"derecha")
        self.text_ip.config(config.SERVIDOR, 40, 40, 120, 18)
        self.labl_port.config("Port", 10, 60+4, 26, 12,"derecha")
        self.text_port.config(config.PUERTO, 40, 60, 120, 18)
        self.labl_port2.config("Port", 10, 80 + 4, 26, 12, "derecha")
        self.text_port2.config(config.PUERTO_IMG, 40, 80, 120, 18)
        self.bot_conectar.config("Conectar", 40, 120, 120, 20)
        self.bot_conec_img.config("Conectar Img", 40, 150, 120, 20)
        self.bot_guardar.config("Guardar", 40, 180, 120, 20)
        # sensores titulo
        self.labl_sensores.config("Sensores", 40, 220, 120, 25, "centrada")
        self.labl_sensores.set_textSize(12)
        # sensores
        self.chbox_sens_cent.config("Sonico Central", 40, 260, 120, 18)
        self.chbox_sens_izq.config("Sonico Izquierdo", 40, 280, 120, 18)
        self.chbox_sens_der.config("Sonico Derecho", 40, 300, 120, 18)
        self.text_speed_cent.config(config.UPDATE_SONICO, 40, 330, 120, 18)
        self.bot_update_cent.config("Update", 40, 350, 120, 18)
        # brujula
        self.chbox_sens_bru.config("Brujula", 40, 390, 120, 18)
        self.text_speed_bru.config("1", 40, 410, 120, 18)
        self.bot_update_bru.config("Update", 40, 430, 120, 18)
        self.label_calibrar.config("Calibrar", 40, 460, 120,18)
        self.chbox_cal_0.config("  0", 40, 480, 50, 18)
        self.chbox_cal_90.config(" 90", 40, 500, 50, 18)
        self.chbox_cal_180.config("180", 40, 520, 50, 18)
        self.chbox_cal_270.config("270", 40, 540, 50, 18)
        self.text_cal_0.config("", 110, 480, 50, 18)
        self.text_cal_90.config("", 110, 500, 50, 18)
        self.text_cal_180.config("", 110, 520, 50, 18)
        self.text_cal_270.config("", 110, 540, 50, 18)

        # distancia
        self.chbox_sens_dis.config("Distancia", 40, 580, 120, 18)
        self.text_speed_dis.config("1", 40, 600, 120, 18)
        self.bot_update_dis.config("mm x paso", 40, 620, 120, 18)

        # Camara
        self.chbox_sens_cam.config("Camara", 40, 660, 120, 18)
        self.text_speed_cam.config("1", 40, 680, 120, 18)
        self.bot_update_cam.config("FPS", 40, 700, 120, 18)

        # lado central
        self.chbox_ruedas.config("Ruedas",200, 40, 120, 18)
        self.label_rued_iz_freno.config("Izq Freno", 200, 60, 60, 18, "derecha")
        self.label_rued_iz_max.config("Izq Max", 200, 80, 60, 18, "derecha")
        self.label_rued_iz_min.config("Izq Min", 200, 100, 60, 18, "derecha")
        self.label_rued_de_freno.config("Der Freno", 200, 120, 60, 18, "derecha")
        self.label_rued_de_max.config("Der Max", 200, 140, 60, 18, "derecha")
        self.label_rued_de_min.config("Der Min", 200, 160, 60, 18, "derecha")

        self.text_rued_iz_freno.config("",270, 60, 50, 18)
        self.text_rued_iz_max.config("", 270, 80, 50, 18)
        self.text_rued_iz_min.config("", 270, 100, 50, 18)
        self.text_rued_de_freno.config("", 270, 120, 50, 18)
        self.text_rued_de_max.config("", 270, 140, 50, 18)
        self.text_rued_de_min.config("", 270, 160, 50, 18)

        self.bot_update_rued.config("Update", 200, 180, 120, 18)

        self.chbox_motor_cam.config("Motor Cam", 200, 230, 120, 18)
        self.text_speed_mot_cam.config("1", 200, 250, 120, 18)
        self.bot_update_mot_cam.config("Update", 200, 270, 120, 18)

        self.chbox_sens_laser.config("Sensor Laser", 200, 310, 120, 18)
        self.text_speed_laser.config("1", 200, 330, 120, 18)
        self.bot_update_laser.config("Update", 200, 350, 120, 18)


        self.label_prog_dist.config("Distancia Recorrida en cm", 200, 380, 220, 18)
        self.prog_dist.config(0,100, "0", 200, 400, 220, 18)
        self.label_prog_laser.config("Distancia Laser", 200, 420, 220, 18)
        self.prog_laser.config(0, 200, "0", 200, 440, 220, 18)
        self.label_prog_cent.config("Distancia Sonico Central", 200, 460, 220, 18)
        self.prog_cent.config(0, 400, "0", 200, 480, 220, 18)
        self.label_prog_izq.config("Distancia Sonico Izquierdo", 200, 500, 220, 18)
        self.prog_izq.config(0, 400, "0", 200, 520, 220, 18)
        self.label_prog_der.config("Distancia Sonico Derecho", 200, 540, 220, 18)
        self.prog_der.config(0, 400, "0", 200, 560, 220, 18)
        self.label_comp_der.config("Brujula", 200, 580, 320, 18)
        self.compbox.config("180", 200, 600, 120, 120)

        # lado derecho 1
        self.label_fps.config("FPS Procesado: ", 440, 20, 100, 18)
        self.box_imagen.config(440, 40, 320, 240)

        # lado derecho
        self.box_draw.config(770, 40, 700, 700)
