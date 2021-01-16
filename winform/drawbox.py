# -*- coding: utf-8 -*-

###########################################################
### CLASE DRAWBOX (Para dibujar en pantalla)            ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 15/01/2021                                          ###
### Creacion                                            ###
###########################################################

import pygame
from winform.base.objeto_gral import Objeto_Gral
from winform.base.funciones import posLineRadio

class DrawBox(Objeto_Gral):
    def __init__(self, C_Form):
        super().__init__(C_Form)                # instanciamos la clase padre

    def config(self, x, y, ancho, alto):
        super().config(x, y, ancho, alto)

    def dibujar(self):
        pygame.draw.rect(self.superficie, self.color, self.rectangulo, 0)  # dibujamos

    ###################################
    ### METODOS                     ###
    ###################################
    def punto(self, x, y, tamano, color):
        pygame.draw.circle(self.superficie, color, (x, y), tamano)

    def linea_angular(self, x, y, angulo, longitud, color, ancho=1):
        x1, y1, x2, y2 = posLineRadio(x, y, angulo, longitud)
        pygame.draw.line(self.superficie, color, (x, y), (x2, y2), ancho)

    def arco(self, x, y, angulo, longitud, arco, color, ancho=1):
        pygame.draw.arc(self.superficie, color, rect,  )
