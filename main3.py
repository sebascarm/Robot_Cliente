# -*- coding: utf-8 -*-

############################################################
### MODULO PRINCIPAL 5.2                                 ###
############################################################
### ULTIMA MODIFICACION DOCUMENTADA                      ###
### 16/01/2021                                           ###
### Cambio de resolucion                                 ###
### Cracion                                              ###
############################################################

from componentes.logg     import Logg

from winform.screen       import Screen
from winform.form         import Form
from forms.form_principal import Form_Principal
from forms.eventos        import Eventos

RESOLUCION  = 1500, 768
COLOR_FORM  = 20, 20, 40
POS_VENTANA = 0, 0

log = Logg()
log.definir()

SCREEN    = Screen("Robot v5.0.1", RESOLUCION)  # enviamos el tamano al inicio
FORM      = Form(SCREEN, "control", RESOLUCION, POS_VENTANA, COLOR_FORM)
OBJETOS   = Form_Principal(FORM)
EVENTOS   = Eventos(OBJETOS, log)

SCREEN.loop()
