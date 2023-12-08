# COHELO, BENEDETTI O GANDALF

Proyecto en el que desarrollo un juego de preguntas en el que se le presenta al jugador una serie de frases (una a una) y ha de decir de quién es entre 3 opciones: Paolo Cohelo ,Mario Beneddeti o Gandalf

## Webscraping

Para sacar las frases creé la clase frase con los campos texto y autor y mediante web scraping las saqué de páginas en internet, las limpié y depuré para que tuviesen el mismo formato

## Templates

Creé tres templates de html como interfaz de usuario: Una de inicio (index.html) donde se da la bienvenida al jugador y con un botón se inicia el juego cuya interfaz está en el archivo juego.html. Al acabar el juego llegamos a la pantalla final (resultado.html) donde nos detallan los aciertos y las intentonas y nos ponen un botón para volver a jugar

## app.py

El juego se ejecuta en este archivo