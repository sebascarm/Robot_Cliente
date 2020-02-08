# -*- coding: utf-8 -*-

###########################################################
### CLASE BUTTON                                        ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 02/09/2019                                          ###
### Eliminado import innecesario                        ###
###########################################################

import pygame
from winform.base.objeto_gral import Objeto_Gral


class Button(Objeto_Gral):
    def __init__(self, C_Form):
        super().__init__(C_Form)                # instanciamos la clase padre
        self.funcion = ''                       # funcion que se activa con click

    def config(self, text, x, y, ancho, alto):
        super().config(x, y, ancho, alto, text, False)
        self.label_int.config(self.text, self.color_text, 
                              self.rectangulo,
                              "centrada", "centrada", 
                              self.text_size)

    def dibujar(self):
        pygame.draw.rect(self.superficie, self.color, self.rectangulo, 0)  # dibujamos
        self.label_int.dibujar()                                           # texto

    ###################################
    ### EVENTOS PARA USUARIO        ###
    ###################################
    # define la funcion a ejecutar al hacer click
    def accion(self, funcion):
        self.funcion = funcion

    ###################################
    ### EVENTOS                     ###
    ###################################

    def evento_mouse_over(self):
        # dibujamos
        pygame.draw.rect(self.superficie, self.color_b2, self.rectangulo, 0)
        self.label_int.dibujar()

    def evento_mouse_out(self):
        # dibujamos
        pygame.draw.rect(self.superficie, self.color, self.rectangulo, 0)
        self.label_int.dibujar()
        #self.foco = False
        
    def evento_mouse_click(self):
        # dibujamos
        pygame.draw.rect(self.superficie, self.color_b3, self.rectangulo, 0)
        self.label_int.dibujar()
        self.evento_foco()
        #Agregar accion del boton
        if self.funcion != '':
            self.funcion()
      
    ###################################
    ### EVENTOS DE TECLADO          ###
    ###################################

    def evento_key(self, cod_caracter, caracter):
        super().evento_key(cod_caracter, caracter)
        if cod_caracter == 32: # SPACE
            self.evento_mouse_click()

    def evento_keyup(self, cod_caracter):
        if cod_caracter == 32: # SPACE
            self.evento_mouse_out()
        
