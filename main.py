""" MODULO PRINCIPAL MAIN()
"""

from winform.screen    import Screen
from winform.form      import Form
from formularios.ventana_principal import FormMain

RESOLUCION  = 900, 600
COLOR_FORM  = 40, 0, 50
POS_VENTANA = 0, 0

# Crear pantalla, objeto unico y principal
SCREEN = Screen("Robot v0.4.5", RESOLUCION, 1,1.0)  # enviamos el tamano al inicio
SCREEN.dibujar()

FORM1 = Form(SCREEN, "control", RESOLUCION, POS_VENTANA, COLOR_FORM)
OBJETOS = FormMain(FORM1)

# creamos la ventana desde la pantalla
FORM1.dibujar()
OBJETOS.dibujar()

SCREEN.loop()
