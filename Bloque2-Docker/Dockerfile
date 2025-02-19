# Distribucion de python del contenedor
FROM python:3.7.7-slim
# Configuracion incial e instalacion de de la aplicacion
RUN apt-get update
#RUN apt-get install git -y
RUN apt-get install -y git 
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt

# Creamos un argumento y lo capturamos como variable de entorno 
ARG GROUP_NUM
ENV GROUP_NUM="grupo_predet"

#WORKDIR /app/bookinfo/src/productpage
WORKDIR /practica_creativa2/bookinfo/src/productpage

# Exponemos el puerto 5080 para que sea accesible
EXPOSE 5080

# Una vez creado el contenedor se ejecutan los siguientes comandos sobre el
CMD ["sh", "-c", "sed -i \"s/Simple Bookstore App/ Group${GROUP_NUM}/\" templates/productpage.html && python3 productpage_monolith.py 5080"]
