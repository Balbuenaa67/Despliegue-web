#!usr/bin/python3
from subprocess import call
import os,sys

# Configuración

call(['sudo', 'apt', 'update'])
call(['sudo', 'apt', 'upgrade'])
call(['sudo', 'apt', 'install', 'docker.io'])

# Construir la imagen Docker
def crear():
        call(['sudo', 'docker', 'build', '-t', 'product-page/19', '.'])
        os.system('sudo docker run -it --name productpage-19 -p 5080:5080 --env GROUP_NUM=$GROUP_NUM')

# Ejecutar el contenedor
def arrancar():
	os.system('sudo docker run -it -p 5080:5080 --env GROUP_NUM=19 product-page/19')


param = sys.argv

if param[1] == "arrancar":
        arrancar()
if param[1] == "crear":
        crear()


