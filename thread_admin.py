# -*- coding: utf-8 -*-

###########################################################
### CLASE THREAD ADMIN V1.6                             ###
###########################################################
### ULTIMA MODIFICACION DOCUMENTADA                     ###
### 20/09/2019                                          ###
### Mas velocidad en control de thread (0.1)            ###
### Call back (no es obligatorio)                       ###
### Agregado de Totalthread para nuevos casos           ###
### Parametro time_to_kill                              ###
### Correcciones en close                               ###
### Incorporacion de parametro name                     ###
###########################################################

import threading
import ctypes
import signal
import sys
import time
import queue

#######################################################
### FUNCION PARA CAPTURAR INTERRUPCION DE TECLADO   ###
#######################################################

def keyboard_interrupt(signal, frame):
    print(' SERVICE BREAK: Ctrl + C')
    ThreadAdmin.close_all()
    print('FINISH THREADING CLOSE')
    print('EXIT PROGRAM')
    sys.exit(0)
    

signal.signal(signal.SIGINT, keyboard_interrupt)
 
##########################################
### CONTROL DE ESTADO DE LOS THREADS   ###
##########################################
def threads_control():
    th_control = threading.Thread(target=__threads_status, name = 'CONTROL')
    th_control.daemon = True
    th_control.start()

def __threads_status():
    time.sleep(0.1)
    while 1:
        for thread in ThreadAdmin.threads:
            if thread.state: 
                if not thread.thread.is_alive():
                    mensaje = ("THREAD ID: " + str(thread.ident) + " " + str(thread.name) + " FINISHED - TOTAL THREADS: " + str(thread.total_threads()))
                    thread.funcion_call(5, mensaje)
                    thread.state = False
        time.sleep(0.1)

##########################################
### CLASE ADMINISTRADORA DE THREADS    ###
##########################################

class ThreadAdmin(object):
    threads_control()
    threads = []                            # lista de self threads
    thread_ini = threading.active_count()   # Numero de procesos actuales 
    def close_all():                        # cerrar todos los hilos 
        print("CLOSING THREADS")
        for thread in ThreadAdmin.threads:
            if thread.state:
                ThreadAdmin.close(thread)
            
    def __init__(self, process='', argument='', name = '', time_to_kill=3, callback=''):    
        # Se puede pasar el proceso al instanciar o pasar como start luego
        # Callback devuelve un codigo y un string
        # Codigos callback -1: Error, 5: Informacion
        self.state        = False           # estado de ejecucion
        self.process      = process
        self.argument     = argument
        self.name         = name
        self.time_to_kill = time_to_kill    # valor en segundos        
        self.thread       = ''
        self.ident        = 0
        self.funcion_call = ''
        #arranca el star si se paso el proceso como parametro, caso contrario se espera iniciar con start
        if process != '':
            self.start(self.process, self.argument, self.name, self.time_to_kill, callback)

    def callback(self, funcion_callback):
        # Callback, retorno de mensajes para log
        # se devuelven 2 parametros 
        # Si no se especifica se utiliza print
        if funcion_callback != '':
            self.funcion_call = funcion_callback
        else:
            self.funcion_call = self.callback_vacio

    def start(self, process, argument='', name = '', time_to_kill=3, callback=''):
        if not self.state: 
            self.callback(callback)
            self.process      = process
            self.argument     = argument
            self.name         = name
            self.time_to_kill = time_to_kill    
            if argument == '':
                if name == '':
                    self.thread = threading.Thread(target=self.process)
                else:
                    self.thread = threading.Thread(target=self.process, name=self.name)
            else:
                if name == '':
                    self.thread = threading.Thread(target=self.process, args=(argument,))
                else:
                    self.thread = threading.Thread(target=self.process, name=self.name, args=(argument,))
            ThreadAdmin.threads.append(self)
            self.thread.daemon = True 
            self.thread.start() # Python 3
            #requiere iniciar para tener el id
            self.ident= self.thread.ident
            self.name = self.thread.name
            mensaje = ("START THREAD ID: " + str(self.ident) + " " + str(self.name) + " - TOTAL THREADS: " + str(self.total_threads()))  
            self.funcion_call(5, mensaje)
            self.state = True
        else:
            mensaje = ("THREAD ID: " + str(self.ident) + " ALREADY RUNNING")
            self.funcion_call(-1, mensaje)
            
    def total_threads(self):
        return threading.active_count() - ThreadAdmin.thread_ini
    
    def close(self):
        if self.state:
            if self.__close_thread():
                self.state = False
                mensaje = ("TOTAL THREADS: " + str(self.total_threads())) 
                self.funcion_call(5, mensaje)
        else:
            mensaje = ("THREAD ID: " + str(self.ident) + " NOT RUNNING")
            self.funcion_call(-1, mensaje)
            
    ##########################################
    ### FUNCION PARA CERRAR THREADS        ###
    ##########################################        
    def __close_thread(self): 
        result = ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, ctypes.py_object(SystemExit)) 
        if result > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, 0) 
            mensaje = ("THREAD ID: " + str(self.ident) + " " + str(self.name) + " CLOSE ERROR")
            self.funcion_call(-1, mensaje)
            return False
        else:
            mensaje = ("THREAD ID: " + str(self.ident) + " " + str(self.name) + " CLOSING") 
            self.funcion_call(5, mensaje)
            if self.__join_thread():
                return True
            else:
                return False

    def __join_thread(self):
        cola_espera = queue.Queue()
        th_control = threading.Thread(target=self.__thread_join, name = 'JOINER', args=(cola_espera,))
        th_control.daemon = True
        th_control.start()
        tiempo = 0
        while tiempo < self.time_to_kill:
            if cola_espera.qsize() > 0:
                mensaje = ("THREAD ID: " + str(self.ident) + " " + str(self.name) + " CLOSE OK") 
                self.funcion_call(5, mensaje)
                return True
            time.sleep(0.1)
            tiempo += 0.1
        
        ctypes.pythonapi.PyThreadState_SetAsyncExc(
            th_control.ident, ctypes.py_object(SystemExit)) 
        mensaje = ("THREAD ID: " + str(self.ident) + " " + str(self.name) + " CLOSE FAIL (Kill)") 
        self.funcion_call(-1, mensaje)
        return True
        # return False // Es probable que tengamos que devolver realmente False 
        # pero el join queda blqueado en casos 

    def __thread_join(self, cola_espra):
        self.thread.join()
        cola_espra.put(True)

    #callback por defecto
    def callback_vacio(self, codigo, mensaje):
        #print(str(codigo) + " " + mensaje)
        print(mensaje)
