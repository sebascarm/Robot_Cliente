# -*- coding: utf-8 -*-

###########################################################
### CONTROL TCP VERSION 2.0                             ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 04/09/2019                                          ###
### Correccion en funcion recursiva                     ###
### Encargado de controlar los paquetes TCP             ###
###########################################################

# LONG FIJA  | LONG VARIABLE
# 012 456 890 2.......             
# [iD|LON|CHK|MODULO|COMANDO|VALOR] 
# Para comprobar se utiliza el CHK = 000

from componentes.cliente_tcp import Cliente_TCP
from componentes.funciones import GetChkSum
from componentes.funciones import Val_to_text

class Control_TCP(Cliente_TCP):
    def __init__(self):
        super().__init__()
        self.inicio   = ''
        self.fin      = ''
        self.max_size = ''
        self.funcion  = '' # Funcion callback original
        self.paquete  = '' # paquete de datos completos
        self.paq_completo = '' # paquete completo 
        # tipos de busqueda interna
        self.buscar_ini = True
        self.buscar_fin = False
            
    def config(self, Host, Puerto, Callback, Buffer = 1024):
        ''' Callaback(Codigo, Mensaje)
            La funcion callback retorna un codigo y el mensaje de detalle o recepcion'''
        self.funcion = Callback
        super().config(Host, Puerto, self.__callback_int, Buffer)

    def config_packet(self, inicio="[", fin="]", max_size=100):
        '''inicio   = caracter que define el inicio del paquete
           fin      = caracter que define el final del paquete
           max_size = tamaño maximo para buscar el fin del paquete
        '''
        self.inicio   = inicio
        self.fin      = fin
        self.max_size = max_size

    #Agregamos el codigo: -2 en caso de errores corregibles
    def __callback_int(self, codigo, mensaje):
        if codigo != 4:
            self.funcion(codigo, mensaje) # devolvemos el mensaje sin cambios
        else:
            self.paquete += mensaje       # analizamos el mensaje
            
            if self.buscar_ini:
                # Revisamos el inicio del paquete
                if self.paquete[:1] != self.inicio:
                    #buscamos el inicio del paquete
                    pos_ini = self.paquete.find(self.inicio)
                    if pos_ini == -1:
                        # no se encontro el inicio, descartamos los datos actuales
                        # el inicio se puede encontrar en el resto del paquete
                        self.funcion(-2, "Inicio no encontrado - Perdida de datos")
                        self.paquete = ''
                    else:
                        # inicio encontrado, pero desfazado, eliminar parte inicial del paquete
                        self.funcion(-2, "Inicio desplazado - Perdida de datos")
                        self.paquete = self.paquete[pos_ini:]
                        self.buscar_ini = False
                        self.buscar_fin = True
                else:
                    #el inicio es correcto
                    self.buscar_ini = False
                    self.buscar_fin = True
            
            if self.buscar_fin:
                # busqueda de fin de paquete
                pos_fin = self.paquete.find(self.fin)
                if pos_fin == -1:
                    # no se encontro el fin
                    self.funcion(-2, "Final no econtrado en paquete actual")
                    if pos_fin > self.max_size:
                        self.funcion(-2, "Final no encontrado en longitud maxima - Perdida de datos")
                        # se supero el final sin encontrarlo
                        # se elimina el inicio del paquete para posteriormente buscar otro inicio
                        self.paquete = self.paquete[pos_ini+1:]
                        self.buscar_ini = True
                        self.buscar_fin = False
                    # el final puede estar en el resto del paquete, se espera el proximo paquete
                else:
                    # paquete completo
                    if pos_fin > self.max_size:
                        self.funcion(-2, "Final encontrado pasada longitud maxima - Perdida de datos")
                        # se elimina el inicio del paquete para posteriormente buscar otro inicio
                        self.paquete = self.paquete[pos_ini+1:]
                        self.buscar_ini = True
                        self.buscar_fin = False
                    else:    
                        # enviar paquete
                        self.paq_completo = self.paquete[1:pos_fin]
                        self.funcion(4, self.paq_completo)
                        self.buscar_ini = True
                        self.buscar_fin = False
                        # revisasr si queda paquete pendiente
                        if (len(self.paq_completo) + 2) == len(self.paquete): # 2 por Inicio y Fin
                            self.paquete = ''   # no hay mas nada
                        else:
                            # enviar el paquete y rellamarse a si mismo
                            self.paquete = self.paquete[pos_fin+1:]
                            self.__callback_int(4, '') # se envia vacio, los datos ya estan en self.paquete

                 
