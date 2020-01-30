# -*- coding: utf-8 -*-

###########################################################
### CLASE IMAGEN                                        ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 30/01/2020                                          ###
### Creacion                                            ###
###########################################################

import pygame
from winform.base.objeto_gral import Objeto_Gral

import cv2
import time

class Imagen(Objeto_Gral):
    def __init__(self, C_Form):
        super().__init__(C_Form)                # instanciamos la clase padre

    def config(self, x, y, ancho, alto):
        super().config(x, y, ancho, alto)
        

    def dibujar(self):
        pygame.draw.rect(self.superficie, self.color, self.rectangulo, 0)  # dibujamos
        
        captura = cv2.VideoCapture(0, cv2.CAP_DSHOW) # si es windows
        procesado, frame = captura.read()
        #captura.release()
        #time.sleep(1)
        self.superficie.blit(self.cvimage_to_pygame(frame), (self.x,self.y))

    
    def cvimage_to_pygame(self,image):
        """Convert cvimage into a pygame image"""
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],"RGB")
        
            
        # """Convert cvimage into a pygame image"""
        #image_rgb = cv.CreateMat(image.height, image.width, cv.CV_8UC3)
        #cv.CvtColor(image, image_rgb, cv.CV_BGR2RGB)
        #return pygame.image.frombuffer(image.tostring(), cv.GetSize(image_rgb),
        #                           "RGB")
