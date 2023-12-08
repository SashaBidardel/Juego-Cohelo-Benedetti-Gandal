import sys
import os

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar el directorio padre al sys.path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from webscraping.Cohelo import obtener_frases_Cohelo
from webscraping.Benedetti import obtener_frases_Benedetti
from webscraping.Gandalf import obtener_frases_Gandalf
import random
from flask import Flask, render_template, request, session
autores = ['Coelho', 'Benedetti', 'Gandalf']
app = Flask(__name__)
# Configurar la clave secreta para la sesión
app.secret_key = os.urandom(24)
def obtener_frases(): # Meter en una lista de objetos frase todas las frases de los 3 autores 
    
    frases = []

    frases_Cohelo, _ = obtener_frases_Cohelo()
    for frase in frases_Cohelo:
        frases.append(frase)

    frases_Benedetti, _ = obtener_frases_Benedetti()
    for frase in frases_Benedetti:
        frases.append(frase)

    frases_Gandalf, _ = obtener_frases_Gandalf()
    for frase in frases_Gandalf:
        frases.append(frase)
    return frases


def obtener_autor_para_frase(frase_buscada): # Obtener el autor de una frase concreta
    frases = obtener_frases()  # Obtener la lista de frases

    for frase in frases:
        if frase.texto == frase_buscada:
            return frase.autor
    
    return "Autor Desconocido"  


def obtener_frase_aleatoria():
    frases = []

    
    frases_Cohelo, _ = obtener_frases_Cohelo()
    frases.extend(frases_Cohelo)

    frases_Benedetti, _ = obtener_frases_Benedetti()
    frases.extend(frases_Benedetti)

    frases_Gandalf, _ = obtener_frases_Gandalf()
    frases.extend(frases_Gandalf)

   
    frase_aleatoria = random.choice(frases)
    
    return frase_aleatoria


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/juego', methods=['GET', 'POST'])
def juego_adivinar_autor():
    intentos = 4
    aciertos = session.get('aciertos', 0)

    if request.method == 'GET':
        session['intentos_restantes'] = intentos
        session['aciertos'] = 0  # Reiniciar el valor de aciertos al empezar un nuevo juego
        frase = obtener_frase_aleatoria()
        session['frase_actual'] = frase.texto  # Almacena solo el texto de la frase
        return render_template('juego.html', frase=frase.texto)

    if request.method == 'POST':
        frase_actual = session.get('frase_actual')
        autor_correcto = obtener_autor_para_frase(frase_actual)  # Función para obtener el autor de la frase actual
        primera_respuesta = request.form.get('respuesta')

        if primera_respuesta == autor_correcto:
            aciertos += 1
            mensaje = "¡Correcto!"
            session['aciertos'] = aciertos  # Actualizar la sesión con el nuevo valor de aciertos
        else:
            mensaje = f"Fallaste, era de {autor_correcto}"

        session['intentos_restantes'] -= 1

        if session['intentos_restantes'] > 0:
            frase_siguiente = obtener_frase_aleatoria()
            session['frase_actual'] = frase_siguiente.texto  # Almacenar el texto de la siguiente frase
            return render_template('juego.html', frase=frase_siguiente.texto, mensaje=mensaje, aciertos=aciertos)
        else:
            return render_template('resultado.html', mensaje=mensaje, aciertos=aciertos, intentos=intentos)

if __name__ == '__main__':
    app.run(debug=True, port=5002)