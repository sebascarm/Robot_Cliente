class Eventos(object):
    def __init__(self, C_Objetos):
        self.objetos = C_Objetos

    def conectar(self):
        ''' evento cuando se presiona boton de conexion '''
        if not self.objetos.face_comp.conectado:
            print("conectar")
            self.objetos.bot_conectar.set_text("Desconectar")
            self.objetos.face_comp.iniciar()
        else:
            print("desconectar")
            self.objetos.bot_conectar.set_text("Conectar")
            self.objetos.face_comp.stop()
        
    




