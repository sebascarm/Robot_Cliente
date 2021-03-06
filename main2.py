# -*- coding: utf-8 -*-

############################################################
### MODULO PRINCIPAL 4.8.2                               ###
############################################################
### ULTIMA MODIFICACION DOCUMENTADA                      ###
### 08/02/2020                                           ###
### Cracion                                              ###
############################################################

from componentes.logg import Logg

from winform.screen       import Screen
from winform.form         import Form
from forms.form_principal import Form_Principal
from forms.eventos        import Eventos

RESOLUCION  = 900, 600
COLOR_FORM  = 40, 0, 50
POS_VENTANA = 0, 0

log = Logg()
log.definir()

SCREEN    = Screen("Robot v1.0.0", RESOLUCION)  # enviamos el tamano al inicio
FORM      = Form(SCREEN, "control", RESOLUCION, POS_VENTANA, COLOR_FORM)
OBJETOS   = Form_Principal(FORM)
EVENTOS   = Eventos(OBJETOS)

SCREEN.loop()
