Robot CLIENTE version 5.1.3 (PC)
=====================
### Control de cambios
* 16/01/2021
    * clase form         v2.6 (nuevos elementos)
    * clase Drawbox      v1.0 (creacion)
    * clase eventos      v1.8 (envio de brujula)
* 15/01/2021
    * clase form         v2.5 (uso de archivo de configuracion)
    * clase eventos      v1.7 (uso de archivo de config)
    * config.py          v1.0 (archivo de variables globales)   
* 14/01/2021
    * clase eventos      v1.6 (Cambio de IP y sensores) 
* 20/10/2020
    * clase eventos      v1.4 (Agregado de sensores)
    * clase form_princip v2.4 (Agregado de sensores)
* 17/10/2020
    * clase eventos      v1.3 (Cambio de IP)
    * clase eventos      v1.2 (Control de conexion y Log)
    * clase form_princip v2.3 (Redibujado)
    * clase main3        v5.1 (Nuevo main)
* 16/10/2020
    * Uso de pycharm
* 26/02/2020
    * clase face_comp    v1.9 (puerto, funcion envio, estado)
    * clase form_princip v2.2 (sin obj no graficos)
    * clase eventos      v1.1 (objetos no graficos)
* 21/02/2020
    * clase Thread_Admin v2.4 (re ejecucion)
    * clase servidor_TCP v3.8 (desconexion)
    * clase logg         v1.2 (incorporada)
    * clase face_comp    v1.6 (evento de conexion, desconexion)
    * clase comunicacion v3.9 (desconexion, log)
    * clase eventos           (definicion inside) 
    * clase form_princip v2.1 (eventos aparte)
* 20/02/2020
    * clase thread_admin v2.3 (diccionario)
    * clase Servidor_TCP v3.7 (log de th en callback)
    * clase comunicacion v3.7 (log)
* Previo
    * (Correr sobre version de 64 bits)
    * Correccion en comunicacion
    * Nuevo objeto comunicacion
    * Mejoras en readme
    * Correcion objeto label v1.1
    * Winform (objeto image)


-----------
## Versiones
-----------
Versiones PC

* Entorno virtual en: ent-virtual-cliente_5.1
* Python 3.8.6 (PC - Pycharm)

* pip                   20.2.3
* setuptools            50.3.1
* pygame                1.9.6 
* opencv-contrib-python 4.4.0.44
* imutils               0.5.3       (manipulacion de imagen)


Versiones LAPTOP (Actualizado)

* Entorno virtual en: ent-virtual-cliente_5.1
* Python 3.8.6 (PC - Pycharm)

* imutils               0.5.3       (manipulacion de imagen)
* numpy                 1.19.5
* opencv-contrib-python 4.5.1.48
* pip                   20.3.3
* pygame                2.0.1
* setuptools            51.1.2
 


```
Package               Version
--------------------- ----------
numpy                 1.18.1
opencv-contrib-python 4.1.2.30
pip                   20.0.2
pygame                1.9.6
gTTS                  2.1.0
gTTS-token            1.1.3
imutils               0.5.3
otros... (limpiar)
```

Versiones:

* Python 3.6.9 (Linux PC)
* Requerido:
    * pyGame
    * Opencv
```
numpy                 1.18.1
opencv-contrib-python 4.1.2.30
pip                   20.0.2
pygame                1.9.6
setuptools            41.2.0
```

Versiones YOGABOOK
* Python 3.8.1
* Requerido:
    * pygame (pip install pygame)
    * opencv (pip install opencv-contrib-python)
    * imutils (pip install imutils) # no necesario


-----------
## Carpetas
-----------


* Componentes
    * Clases y objetos de uso comun
* Tmp
    * archivos temporales
* Actividad
* Comunicacion
* ia

## Entorno Virtual

## Instalar entorno virtual (solo linux - metodo facil)
```
sudo ap-get install python3-venv
```
## Crear entorno virtual en directorio
```
python3 -m venv carpeta-env  # Crea la carpeta carpeta-env)
cd carpeta-env
```
#### Activar en Windows
```
Scripts\activate.bat        # Activamos el entorno
Scripts\deactivate.bat      # Desctiva el entorno
```
#### Activar en Linux
```
source carpeta-env/bin/activate
deactivate                  # comando solo sin ruta