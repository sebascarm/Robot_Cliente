Robot CLIENTE version 5.0
=====================
### Control de cambios

* Winform (objeto image)


-----------
## Versiones
-----------
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