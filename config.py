# -*- coding: utf-8 -*-

############################################################
### MODULO GLOBAL (VARIABLES GLOBALES) 1.0               ###
############################################################
### ULTIMA MODIFICACION DOCUMENTADA                      ###
### 14/01/2021                                           ###
### Cracion                                              ###
############################################################

import configparser     # lector de archivos de configuracion

global SERVIDOR
global PUERTO
global PUERTO_IMG
global UPDATE_SONICO

ARCHIVO       = 'config.cfg'
CONFIGURACION = configparser.ConfigParser()
# CONFIGURACION.read('../config.cfg')  # pycharm requiere especificar bien la ruta
CONFIGURACION.read(ARCHIVO)
CONEXION    = CONFIGURACION['CONEXION']
SERVIDOR    = CONEXION['SERVIDOR']
PUERTO      = CONEXION['PUERTO']
PUERTO_IMG  = CONEXION['PUERTO_IMG']

SONICO        = CONFIGURACION['SONICO']
UPDATE_SONICO = SONICO['UPDATE']



