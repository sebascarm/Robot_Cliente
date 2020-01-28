# -*- coding: utf-8 -*-

############################################################
### CLIENTE TCP VERSION 2.2                              ###
############################################################
### ULTIMA MODIFICACION DOCUMENTADA                      ###
### 24/09/2019                                           ###
### Espera de 0.1 para escuchar mensajes entrantes       ###
### timeout en socket para no bloquear proceso al cerrar ###
### Uso de ThreadAdmin                                   ###
### Captura de error al leer datos del puerto            ###
### Evitar intento de conexion conectado                 ###
############################################################

import socket
import time
from thread_admin import ThreadAdmin


class Cliente_TCP(object):
    def __init__(self):
        self.soc = ""
        self.conexion     = False
        self.th_conexion  = ''
        self.th_recepcion = ''      #hilo de recepcion
        
    def config(self, Host, Puerto, Callback, Buffer = 1024):
        self.HOST       = Host
        self.PUERTO     = int(Puerto)
        #self.recepcion  = Cola_Recepcion
        self.buffer     = Buffer
        self.callback   = Callback      #Funcion de rellamada de estados
        #Mensajes de callback: -1 Error 0 Desconectado 1 Conectando 2 Conectado
        #                       3 Envio de Datos 4 Recepcion de Datos
        #Calback funcion ej: calback(codigo, mensaje): / calback(self, codigo, mensaje): /

    def conectar(self):
        #abrimos hilo de recepcion
        if not self.conexion:
            #abrimos un hilo nuevo
            self.th_conexion = ThreadAdmin(self.__interno_conectar,'','CONEXION-TCP', 10)
        else:
            self.callback(-1, "Conexion actualmente establecida")

    def __interno_conectar(self):
        try:
            self.conexion = True
            self.callback(1, "Estableciendo conexion")
            self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.soc.settimeout(3)
            conectar = self.soc.connect((self.HOST, self.PUERTO)) #si tiene que usarse
            self.callback(2, "Conexion establecida")
            self.__interno_recibir()
        except Exception:
            self.conexion = False
            self.callback(-1, "Error en conexion")

    def enviar(self, mensaje):
        if self.conexion:
            try:
                self.soc.sendall(mensaje.encode('utf-8'))
                self.callback(3, "Enviado: " + mensaje)
            except:
                self.desconectar()
                self.callback(-1, "Problemas al enviar datos \n  Conexion Cerrada")
        else:
            try:
                self.callback(-1, "Sin Conexion: " + mensaje)
            except:
                print("Sin Conexion: " + mensaje)

    def __interno_recibir(self):
        while self.conexion:
            try:
                #leer del puerto
                recibido = self.soc.recv(self.buffer)    #leer del puerto - posible bloqueo hasta recepcion (con timeout no hay)
                if recibido == b'':
                    self.callback(-1, "Servidor Desconectado")
                    self.desconectar()
                else:
                    #Recepcion de datos
                    self.callback(4, recibido.decode())
            except socket.timeout as err:
                pass    # time out continua con el loop
            except Exception as err:
                self.callback(-1, "Error SOC: " + str(err))
                self.desconectar()
            # Espera antes de leer nuevamente el puerto
            time.sleep(0.1)
            
        
    def desconectar(self):
        try:
            self.conexion = False
            self.th_conexion.close()
            self.soc.close()
            self.callback(0, "Conexion Cerrada")
        except Exception:
            self.callback(-1, "Error al cerrar conexion")

