# -*- coding: utf-8 -*-

###########################################################
### VENTANA PRINCIPAL 1.0                               ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 29/09/2019                                          ###
###                                                     ###
###########################################################

import configparser     #lector de archivos de configuracion

from winform.label      import Label
from winform.textbox    import Textbox
from winform.logbox     import Logbox
from winform.button     import Button
from winform.checkbox   import Checkbox
from winform.compasbox  import Compasbox
from winform.progress   import Progress
#objetos personales
from logs.logg import Logg
#from conexion.cliente_tcp import Cliente_TCP
from conexion.control_tcp import Control_TCP

CONFIGURACION = configparser.ConfigParser()
CONFIGURACION.read('./config.cfg')
CONEXION = CONFIGURACION['CONEXION']
SERVIDOR = CONEXION['SERVIDOR']
PUERTO   = CONEXION['PUERTO']

class FormMain():
    def __init__(self, C_Form):
        self.labl_titulo  = Label(C_Form)
        self.labl_ip      = Label(C_Form)
        self.text_ip      = Textbox(C_Form)
        self.text_port    = Textbox(C_Form)
        self.labl_port    = Label(C_Form)
        self.bot_conectar = Button(C_Form)
        self.mult_log     = Logbox(C_Form)
        self.chbox_S1     = Checkbox(C_Form)
        self.chbox_S2     = Checkbox(C_Form)
        self.compbox      = Compasbox(C_Form)
        self.text_speed   = Textbox(C_Form)
        self.text_speed_sonic   = Textbox(C_Form)
        self.bot_update         = Button(C_Form)
        self.bot_up_sonic       = Button(C_Form)
        self.progress     = Progress(C_Form)
        
        #objetos personales
        self.log        = Logg()
        self.conex      = Control_TCP() 

        self.labl_titulo.config("Configuración", 10, 10, 140, 25, "centrada")
        #self.labl_titulo.set_background([10,0,10])
        self.labl_titulo.set_textSize(16)
        self.labl_ip.config("IP", 10, 40+4, 26, 12,"derecha")
        self.text_ip.config(SERVIDOR, 40, 40, 110, 18)
        self.labl_port.config("Port", 10, 60+4, 26, 12,"derecha")
        self.text_port.config(PUERTO, 40, 60, 110, 18)
        self.bot_conectar.config("Conectar", 10, 90, 140 , 20)
        self.mult_log.config("LOGS",10,120,300,450)  #REVISAR CUANDO SE ENVIA TEXTO VACIO
        self.mult_log.set_textSize(11) # problemas con algunos tamaÃ¯Â¿Â½os
        # lado derecho
        self.chbox_S1.config("Brujula", 320, 20, 108, 18)
        self.text_speed.config("1",430,20,38,18)
        self.bot_update.config("Update",470,20,70,18)
        #
        self.chbox_S2.config("Sensor sonico", 320, 40, 108, 18)
        self.text_speed_sonic.config("1",430,40,38,18)
        self.bot_up_sonic.config("Update",470,40,70,18)
        #
        self.compbox.config("180",320,120,220,120)
        #
        self.progress.config(0,300, 200,550,120,200,18)
        # objetos personales
        self.log.config(self.mult_log)
        self.conex.config("192.168.0.24", 50001, self.callback, 256)
        self.conex.config_packet("[","]", 100)
        
        # opciones adicionales (EVENTOS)
        self.bot_conectar.accion(self.conectar)
        self.chbox_S1.accion(self.sensor)
        self.chbox_S2.accion(self.sensor_sonico)
        self.bot_update.accion(self.update_time)
        self.bot_up_sonic.accion(self.up_sonic_time)
        

    def dibujar(self):
        self.labl_titulo.dibujar()
        self.labl_ip.dibujar()
        self.text_ip.dibujar()
        self.labl_port.dibujar()
        self.text_port.dibujar()
        self.bot_conectar.dibujar()
        self.mult_log.dibujar()
        self.chbox_S1.dibujar()
        self.compbox.dibujar()
        self.text_speed.dibujar()
        self.bot_update.dibujar()
        self.chbox_S2.dibujar()
        self.text_speed_sonic.dibujar()
        self.bot_up_sonic.dibujar()
        self.progress.dibujar()

        #self.log.log("Start")
        #threading.Thread(target=self.__hilo_test).start() # Python 3

    def callback(self, codigo, mensaje):
        print(str(codigo) + " " + mensaje)
        if codigo == 0:
            #Desconectado
            self.log.log("Deconectado")
            self.bot_conectar.accion(self.conectar)
            self.bot_conectar.set_text("Conectar")
        elif codigo == 2:
            #Conectado
            self.log.log("Conexión establecida")
            self.bot_conectar.accion(self.desconectar)
            self.bot_conectar.set_text("Desconectar")
        elif codigo == 3:
            self.log.log("SEND: " + mensaje)
        #recepcion de datos
        elif codigo == 4:
            try:
                self.log.log("RECP: " + mensaje)
                mensaje_split = str(mensaje).split(":",1) 
                #recepcion de 2 valores (parametros)
                if len(mensaje_split) > 1:  
                    valor     = mensaje_split[1]
                    valor_f   = float(valor)
                    valor_int = int(valor_f)
                    print(valor_int)
                    if mensaje_split[0] == "COMPAS":
                        self.compbox.rotar(int(valor_int))
                    if mensaje_split[0] == "SONICO":
                        self.progress.set_text(str(valor_int))

            except Exception as e:
                self.log.log("ERR: " + str(e))
        else:
            self.log.log(str(codigo) +" " + mensaje)
        


    def conectar(self):
        print("conectar")
        self.conex.conectar()
    
    def desconectar(self):
        print("desconectar")
        self.conex.desconectar()

    def sensor(self, estado):
        if estado:
            self.conex.enviar("[COMPAS-ON]")
        else:
            self.conex.enviar("[COMPAS-OFF]")

    def sensor_sonico(self, estado):
        if estado:
            self.conex.enviar("[SONICO-ON]")
        else:
            self.conex.enviar("[SONICO-OFF]")

    def update_time(self):
        tiempo = self.text_speed.text
        self.conex.enviar("[COMPAS-SPEED]:" + tiempo)

    def up_sonic_time(self):
        tiempo = self.text_speed_sonic.text
        self.conex.enviar("[SONICO-SPEED]:" + tiempo)
