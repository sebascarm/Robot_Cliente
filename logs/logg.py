from datetime import datetime

class Logg(object):
    def __init__(self):
        self.linea = 0
    def config(self, Objeto_Salida=""):
        #Objeto_Salida = Logbox (kivy)
        self.linea          = 0
        self.objeto_salida  = Objeto_Salida

    def log(self, texto, modulo =""):
        #tiempo = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        tiempo = datetime.now().strftime('%H:%M:%S.%f')[:-7]
        salida = ""
        if modulo != "":
            modulo = " [" + modulo + "]"
        #Si es primera linea
        if self.linea == 0:
            salida =  tiempo + ": INICIO DE LOG"
            if self.objeto_salida == "":
                print(salida, end = "")
            else:
                self.objeto_salida.insert(salida)
        # Log estandard
        self.linea += 1
        salida = tiempo + modulo + ": " + texto
        if self.objeto_salida == "":
            #si no se especifico un objeto de salida se envia a la pantalla
            print(salida, end = "")
        else:
            self.objeto_salida.insert(salida)
            


