
from winform.base.objeto_gral import Objeto_Gral #Clase Padre

class Label(Objeto_Gral):
    def __init__(self, C_Form):
        super().__init__(C_Form)                #instanciamos la clase padre
        
    def config(self, text, x, y, ancho, alto, alineacion="izquierda"):
        """Configuración del objeto Requerido previo a toda acccion
           alinacion = izquierda , derecha, centrada
        """
        super().config(x, y, ancho, alto, text, True, False)
        self.label_int.config(self.text, self.color, self.rectangulo, alineacion, "centrada", self.text_size)

    #def set_textSize(self, size):
    #    self.label_int.set_textSize(size)
        
    def set_background(self, color):
        self.label_int.set_background(color)
    
    def dibujar(self):
        self.label_int.dibujar()   
        #agregamos el cuadro al total
        self.cuadros_total.append(self.rectangulo)


