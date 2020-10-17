###########################################################
### EVENTOS v1.2                                        ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 17/10/2020                                          ###
### Control de conexion y Log
### Incluye objetos no graficos                         ###
### Cracion                                             ###
###########################################################


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
        self.tcp_cli.config("192.168.0.24", 50001, callback=self.evento_conexion)
        self.face_comp.config("192.168.0.24", 50002, self.objetos.box_imagen, self.objetos.label_fps,self.fun_envio)
        # Metodos de los objetos graficos
        self.objetos.bot_conectar.accion(self.click_conectar)
        self.objetos.bot_conec_img.accion(self.click_conectar_img)
        # Callback a eventos
        self.face_comp.config_eventos(self.evento_im_conexion)

    # METODOS DE OBJETOS (CLICK DE LOS BOTONES)
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


    # EVENTOS (CALLBACKS)
    def evento_conexion(self, codigo, mensaje):
        if codigo == 2:     # Conectado
            self.objetos.bot_conectar.set_text("Desconectar")
        elif codigo == 0:   # Desconectado
            self.objetos.bot_conectar.set_text("Conectar")
        elif codigo == -1:  # Error
            self.objetos.bot_conectar.set_text("Conectar")
        else:
            self.log.log(str(codigo) + " " + mensaje, "EVENTOS")

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



