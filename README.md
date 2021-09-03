# GRUPO-2-INFO2021-TRABAJO-FINAL
Repositorio para el trabajo Final del Curso de Programación Web y Bases de Datos del Informatorio 2021 - GRUPO 2

Template base: https://getbootstrap.com/docs/4.0/examples/album/

Comenzando 🚀


Pre-requisitos 📋
Con el gestor de BD que trabajen, crear una base de datos vacía en sus servidores

Instalar las dependendencias del proyecto (ir a la carpeta de requirements)

pip install -r base.txt

Crear settings local.py
modificar en settings/local.py los argumentos para que se conecten a la BD

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'NombreBaseDeDatos',
        'USER': 'UsuarioBaseDeDatos',
        'PASSWORD': 'ContraseñaBaseDeDatos',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

Construido con 🛠️
[Django]Framework web
[PostgreSQL]Base de datos


borrar todos las migraciones (000x...) de migrations

En la consola cmd
	ingresar al entorno virtual que hayan creado
	ejecutar el makemigrations
	ejecutar el migrate, con esto se generan las tablas necesarias
	crear un superusuario con createsuperuser



ATENCION: El superusuario se debe generar desde la consola CMD, solo con este usuario se puede acceder a las vistas:

Listado de Preguntas

Estadisticas Usuarios

Los usuarios finales pueden registrarse dentro de la app 

dentro de 127.0.0.1:8000


Cargar preguntas
agrega un registro nuevo por cada pregunta
consigna es el texto de la pregunta
puntaje, es un valor que pueden asignarle a la preguntas

	ingresar las respuestas alternativas para cada pregunta, se debe marcar con un tilde la correcta


hay un limite de 30 preguntas para pruebas, se puede modificar la constante CANT_PREG_TEST en la clase JuegoUsuario de models.py, se puede poner al máximo de preguntas registradas en la tabla preguntas (50)


si el usuario respondió las CANT_PREG_TEST, no puede seguir participando, para reintentar jugar la trivia, se debe registrar con otro usuario

en la tabla preguntas respondidas, se van registrando las preguntas ya mostradas en la aplicación, no se repiten para el mismo usuario.

 (al borrar todos los registros de la tabla preguntas respondidas la aplicación se reinicia sin modificar los usuarios registrados)



Autores ✒️

Alvarez Gabris Micaela
Silva Irma Laudelina
Kowalczuk Carlos Alberto
Blanco, Brenda
Cicirelli Maximo Miguel
Diego Godoy








