
# Como construir un API para Data Science con Docker

En este proyecto nos enfocaremos en construir un API para un servicio que permita consumir un modelo de machine learning.
Para provisionar los recursos y configurar el ambiente de desarrollo vamos a esta utilizando Docker.
El objetivo final sera desplegar nuestro servicio en una instancia de EC2 de AWS


## Herramientas necesarias

- Github: https://git-scm.com/downloads
- Docker: https://www.docker.com/products/docker-desktop/
- Visual Studio Code: https://code.visualstudio.com/


## Descargar repositorio

```bash
git clone https://github.com/juan-carvajal/dc-docker.git
```

## Desarrollo local
### Herramientas de desarrollo
Una vez clonado el proyecto de Github, podemos comenzar a desarrollar:
```bash
cd dc-docker
```
Abra Visual Studio Code dentro de la carpeta actual:
```bash
code .
```
Ya aqui, el IDE deberia esta abierto y listo para desarrollar, se le van a sugerir algunas extensiones segun el tipo de archivos que tenga abiertos, en este caso, Python. Instalelas (no es necesario, pero es recomendado)

Ahora activaremos el ambiente virtual:
```bash
python -m venv .venv
```
Visual estudio code reconocera que se creo un nuevo ambiente virtual de Python, y le preguntara que si quiere utilizarlo, acepte.
Aqui, se recomienda cerrar la terminal actual y volver a abrir un nueva.
### Instalacion de requerimientos
```bash
pip install -r requirements.txt
```
Esto instalara todos los paquetes que vamos a necesitar.
### Correr local con Docker
Asegurese que la aplicacion de Docker esta corriendo, despues utilice los siguientes comandos:
```bash
docker build -t dc-docker .
docker run -d -p 80:80 -v %cd%:/app dc-docker /start-reload.sh
```
Listo!
Navegue a localhost en su navegar preferido. Ya podemos comenzar a desarrollar.