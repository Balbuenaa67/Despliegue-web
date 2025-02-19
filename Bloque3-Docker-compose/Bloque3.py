#!usr/bin/python3
from subprocess import call
import os


os.system('sudo apt update')
os.system('sudo apt upgrade -y')

os.system('sudo apt install docker.io -y')
os.system('sudo apt install docker-compose -y')

os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
os.chdir('practica_creativa2/bookinfo/src/reviews')
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')

os.system('sudo docker-compose up --build')
