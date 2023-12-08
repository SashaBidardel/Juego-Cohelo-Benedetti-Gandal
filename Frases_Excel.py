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
import pandas as pd
from flask import Flask, render_template, request, session
autores = ['Paulo Coelho', 'Mario Benedetti', 'Gandalf']
app = Flask(__name__)
# Configurar la clave secreta para la sesión
app.secret_key = os.urandom(24)
def obtener_frases():
    
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

# Esta función toma una lista de frases y las guarda en un archivo Excel
def guardar_en_excel(lista_frases):
    # Crear un DataFrame de pandas con las frases y sus autores
    df = pd.DataFrame(lista_frases, columns=['Texto', 'Autor'])

    # Escribir el DataFrame en un archivo Excel
    df.to_excel('frases2.xlsx', index=False)

# Obtener las frases de los diferentes autores
frases = obtener_frases()

# Llamar a la función para guardar las frases en Excel
guardar_en_excel([(frase.texto, frase.autor) for frase in frases])
