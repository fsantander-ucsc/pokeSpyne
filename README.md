
# Ejemplo de RPC en Spyne



## Descripción


Este proyecto es un ejemplo de cómo generar servicios rpc con spyne.
El proyecto cuenta un un ejemplo de servidor en spyne y un ejemplo cliente en flask.
El cliente puede ser implementado en cualquier otro framework que soporte los protocolos manejados por spyne. Solo se utilizó flask para hacer una demostración.


Cualquier interesado en mejorar este archivo base es bienvenido a participar.


## Pre-requisitos


Este proyecto necesita lo siguiente:

  - python version 3
  - virtualenv (Para generar un enterono virtual y cargar los requerimientos)
  - Conexión a internet para instalar requerimientos

## Instalar pre-requisitos

Los requisitos del entorno virtual se encuentran en en archivo requirements.txt. Si solo desea ejecutar el ejemplo pase a la siguiente sección.

Para instalar los pre-requisitos siga los siguientes pasos.


Asegurese de tener python 3 instalado, para esto escriba en la terminal

    python3 --version

Si python 3 no se ecuentra instalado utilice (en distribuciones basadas en debian)

    sudo apt-get install python3

Instale virtualenv para esto utilice

    sudo apt-get install python-virtualenv

Si se ecuentra en un entorno windows utilice pip

    pip install virtualenv






## Como construir el proyecto

Para cargar y probar el proyecto abra una terminal para ejecutar el cliente y una terminal para ejecutar el servidor en un directorio de trabajo


### Instalar requerimientos

Clone el proyecto desde gitlab escribiendo en la terminal

    git clone https://gitlab.com/braulioqh/ejemplorpcspyne.git

Cree un entorno virutal con virtualenv

    virtualenv env_proyectospyne --python=python3

Active el entorno virtual

    source env_proyectospyne/bin/activate

Cambie al directorio del proyecto utilizando

    cd ejemplorpcspyne    

Instale los requerimientos  

    pip install -r requirements.txt

#### Instalar requerimientos manualmente

Si usted desea instalar los requerimientos manualmente debe instalar los siguientes paquetes con el entorno virtal activado

Por el lado del servidor se necesita instalar:


    pip install spyne
    pip install lxml

Por el lado del cliente necesita instalar:

    pip install Flask
    pip install flask-wtf
    pip install zeep

### Ejecutar el cliente y el servidor

Ejecute el servidor (con el entorno virtual activado)

    python serverEjemplo/main.py

Abra otra terminal en el mismo directorio de trabajo (con el entorno virtual activado) para ejecutar el cliente con

    python clientEjemplo/main.py

Si todo sale bien hasta este punto ingrese a:

  - http://127.0.0.1:5000

## Probar el servidor con zeep

Si solo desea probar el servidor puede hacerlo directamente con zeep, para esto abra python desde la terminal

    python

Escriba lo siguiente:

```python
from zeep.client import Client
myclient = Client('http://localhost:8000/?wsdl')

myclient.service.say_hello('Braulio')
myclient.service.sum(3,4)
myclient.service.list_hello('braulio',5)
```
## Cerrar entorno virutal
Para desactivar el entorno virtual cierre la terminal o escriba

    deactivate
