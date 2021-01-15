###########################################################
### EVENTOS v1.7                                        ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 15/01/2021                                          ###
### Uso del archivo de configuracion                    ###
### Guardado de archivo de configuracion                ###
### Borrado de envio de update para sensores iz y der   ###
### Cambio de Ip en conexion                            ###
### Incorporacion de sensores                           ###
### Control de conexion y Log                           ###
### Incluye objetos no graficos                         ###
### Cracion                                             ###
###########################################################

import config

from componentes.comunicacion import Comunicacion
from compuesto.face_comp import Face_Comp
# para visualizacion
from forms.form_principal import Form_Principal
from logs.logg import Logg


class Eventos(object):
    def __init__(self, c_objetos, c_log):
        # type: (Form_Principal, Logg)->None    # utilizado para visualizar ayuda
        self.objetos = c_objetos
        self.log = c_log
        # Configuracion de objetos sin graficos
        self.tcp_cli    = Comunicacion()
        self.face_comp  = Face_Comp()
        self.tcp_cli.config(config.SERVIDOR, config.PUERTO, callback=self.evento_conexion)
        self.face_comp.config(config.SERVIDOR, config.PUERTO_IMG, self.objetos.box_imagen, self.objetos.label_fps, self.fun_envio)
        # Metodos de los objetos graficos
        self.objetos.bot_conectar.accion(self.click_conectar)
        self.objetos.bot_conec_img.accion(self.click_conectar_img)
        self.objetos.bot_guardar.accion(self.click_guardar)
        self.objetos.chbox_sens_cent.accion(self.click_chbox_sensor_cent)
        self.objetos.chbox_sens_izq.accion(self.click_chbox_sensor_izq)
        self.objetos.chbox_sens_der.accion(self.click_chbox_sensor_der)
        self.objetos.chbox_sens_bru.accion(self.click_chbox_brujula)
        self.objetos.bot_update_cent.accion(self.up_sonic_cent_time)
        self.objetos.bot_update_bru.accion(self.up_brujula_time)
        # Callback a eventos
        self.face_comp.config_eventos(self.evento_im_conexion)

    ###########################################################
    ### METODOS (ACCIONES DE LOS BOTONES)                   ###
    ###########################################################
    def click_conectar(self):
        """evento cuando se presiona boton de conexion """
        if self.tcp_cli.conexion:
            self.objetos.bot_conectar.set_text("Desconectando...")
            self.tcp_cli.desconectar()
        else:
            self.objetos.bot_conectar.set_text("Conectando...")
            self.tcp_cli.iniciar()

    def click_conectar_img(self):
        """evento cuando se presiona boton de conexion de imagen"""
        if self.face_comp.conexion:
            self.objetos.bot_conec_img.set_text("Desconectando...")
            self.face_comp.desconectar()
        else:
            self.objetos.bot_conec_img.set_text("Conectando...")
            self.face_comp.iniciar()

    def click_guardar(self):
        """evento cuando se presiona boton de guardar"""
        config.CONFIGURACION.set('CONEXION', 'SERVIDOR', self.objetos.text_ip.text)
        config.CONFIGURACION.set('CONEXION', 'PUERTO', self.objetos.text_port.text)
        config.CONFIGURACION.set('CONEXION', 'PUERTO_IMG', self.objetos.text_port2.text)
        config.CONFIGURACION.set('SONICO', 'UPDATE', self.objetos.text_speed_cent.text)
        with open(config.ARCHIVO, 'w') as archivo:
            config.CONFIGURACION.write(archivo) # salvamos el archivo

    def click_chbox_sensor_cent(self, estado):
        """evento cuando se presiona checkbox de sensor central"""
        if estado:
            self.tcp_cli.enviar("SONICO|ENCENDIDO|1")
        else:
            self.tcp_cli.enviar("SONICO|ENCENDIDO|0")

    def click_chbox_sensor_izq(self, estado):
        """evento cuando se presiona checkbox de sensor izquierdo"""
        if estado:
            self.tcp_cli.enviar("[SONICO_IZQ-ON]")
        else:
            self.tcp_cli.enviar("[SONICO_IZQ-OFF]")

    def click_chbox_sensor_der(self, estado):
        """evento cuando se presiona checkbox de sensor derecho"""
        if estado:
            self.tcp_cli.enviar("[SONICO_DER-ON]")
        else:
            self.tcp_cli.enviar("[SONICO_DER-OFF]")

    def click_chbox_brujula(self, estado):
        """evento cuando se presiona checkbox de la brujula"""
        if estado:
            self.tcp_cli.enviar("[COMPAS-ON]")
        else:
            self.tcp_cli.enviar("[COMPAS-OFF]")

    def up_sonic_cent_time(self):
        """evento cuando se presiona el boton de actualizacion de tiempo"""
        tiempo = self.objetos.text_speed_cent.text
        self.tcp_cli.enviar("SONICO|SPEED|" + tiempo)

    def up_brujula_time(self):
        """evento cuando se presiona el boton de actualizacion de tiempo"""
        tiempo = self.objetos.text_speed_bru.text
        self.tcp_cli.enviar("[COMPAS-SPEED]:" + tiempo)

    ###########################################################
    ### EVENTOS (CALLBACK DE CONEXION)                      ###
    ###########################################################
    def evento_conexion(self, codigo, mensaje):
        if codigo == 2:     # Conectado
            self.objetos.bot_conectar.set_text("Desconectar")
        elif codigo == 0:   # Desconectado
            self.objetos.bot_conectar.set_text("Conectar")
        elif codigo == -1:  # Error
            self.objetos.bot_conectar.set_text("Conectar")
        elif codigo == 4:   # Recepcion de datos
            self.recepcion_datos(mensaje)
        else:
            self.log.log(str(codigo) + " " + mensaje, "EVENTOS")

    ###########################################################
    ### PROCESAMIENTO DE DATOS RECIBIDOS                    ###
    ###########################################################
    def recepcion_datos(self, datos):
        datos = datos.replace("[", "", 1)
        datos = datos.replace("]", "", 1)
        try:
            self.log.log("RECP: " + datos)
            mensaje_split = str(datos).split(":", 1)
            # recepcion de 2 valores (parametros)
            if len(mensaje_split) > 1:
                parametro = mensaje_split[0]    # Parametro
                valor     = mensaje_split[1]    # valor como string
                valor_f   = float(valor)        # valor como float
                valor_int = int(valor_f)        # valor como integer
                print(valor_int)
                if parametro == "COMPAS":
                    self.objetos.compbox.rotar(int(valor_int))
                if parametro == "SONICO-CENT":
                    self.objetos.prog_cent.set_text(str(valor_int))
                if parametro == "SONICO-IZQ":
                    self.objetos.prog_izq.set_text(str(valor_int))
                if parametro == "SONICO-DER":
                    self.objetos.prog_der.set_text(str(valor_int))

        except Exception as e:
            self.log.log("ERR: " + str(e))

    # EVENTOS
    def evento_im_conexion(self, Estado):
        if Estado:
            self.objetos.bot_conec_img.set_text("Desconectar")
        else:
            self.objetos.bot_conec_img.set_text("Conectar")



    # ENVIOS
    def fun_envio(self, modulo, comando, valor):
        mensaje = modulo + "|" + comando + "|" + valor
        self.tcp_cli.enviar(mensaje)



