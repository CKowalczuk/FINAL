# GRUPO-2-INFO2021-TRABAJO-FINAL
Repositorio para el trabajo Final del Curso de Programación Web y Bases de Datos del Informatorio 2021 - GRUPO 2


falta requirements

con el gestor de BD que trabajen, crear una base de datos vacía en sus servidores

modificar en settings/local.py los argumentos para que se conecten a la BD

borrar todos las migraciones (000x...) de migrations

en la consola cmd
	ingresar al entorno virtual que hayan creado
	ejecutar el makemigrations
	ejecutar el migrate,  con esto se generan las tablas necesarias
	crear un superusuario con createsuperuser

dentro de 127.0.0.1:8000

	ingresar a /admin
	en la tabla "preguntas", agregar un registro nuevo por cada pregunta
		consigna es el texto de la pregunta
		puntaje, es un valor que pueden asignarle a la preguntas

		por fk, el inline del admin pide ingresar las respuestas alternativas para cada pregunta, se debe marcar con un tilde la correcta

	todas estas ultimas respuestas, quedan registradas en la tabla "respuestas"

	en la tabla juego usuario, están los usuarios que se hayan registrado en la aplicacion

	en la tabla preguntas respondidas, se van registrando las preguntas ya mostradas en la aplicación, no se repiten para el mismo usuario.

		hay un limite de 10 preguntas para pruebas, se puede modificar la constante CANT_PREG_TEST en la clase JuegoUsuario de models.py, se puede poner al máximo de preguntas registradas en la tabla preguntas (50)

		si el usuario respondió las CANT_PREG_TEST, no puede seguir participando, para reintentar jugar la trivia, se deben borrar todos los registros de la tabla preguntas respondidas para ese usuario (solo lo puede hacer un superusuario)



	ACTIVIDADES PENDIENTES:

	LOGIN DE USUARIO Y REGISTRO DE USUARIO SE DEBEN INCORPORAR COMO BLOQUES DENTRO DE BASE.HTML

	FALTA BOTON DE COMPARTIR

	CORREGIR ALGUNOS verbose_name para que se vean bien en el admin

	detalles de fuentes de los mensajes, mejorarlos


