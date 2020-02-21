class Eventos(object):
    def __init__(self, c_objetos):
        self.objetos = c_objetos
        # Establecer eventos de los objetos
        # Metodos de los objetos graficos
        self.objetos.bot_conectar.accion(self.conectar)
        # Callback a eventos
        self.objetos.face_comp.config_eventos(self.evento_face_conexion)

    # METODOS
    def conectar(self):
        """evento cuando se presiona boton de conexion """
        if not self.objetos.face_comp.conectado:
            print("conectar")
            self.objetos.bot_conectar.set_text("Conectando")
            self.objetos.face_comp.iniciar()
        else:
            print("desconectar")
            self.objetos.bot_conectar.set_text("Desconectando")
            self.objetos.face_comp.desconectar()

    # EVENTOS
    def evento_face_conexion(self, Estado):
        if Estado:
            self.objetos.bot_conectar.set_text("Desconectar")
        else:
            self.objetos.bot_conectar.set_text("Conectar")
    




