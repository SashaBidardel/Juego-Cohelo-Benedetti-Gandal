import sys
import os

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar el directorio padre al sys.path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

import requests
from bs4 import BeautifulSoup
from clases.Frase import Frase  
def obtener_frases_Cohelo():

    url = 'https://psicologiaymente.com/reflexiones/frases-de-paulo-coelho'

   
    response = requests.get(url)

   
    if response.status_code == 200:
        # Parsear el HTML usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las frases dentro de los elementos h3
        frases_elements = soup.find_all('h3')

        # Lista para almacenar objetos Frase
        frases_Cohelo = []

        # Contador de frases
        contador = 0

        # Iterar sobre los elementos que contienen las frases
        for frase_element in frases_elements[:-4]:
            texto = frase_element.get_text(strip=True)  # Obtener el texto de la frase
            autor = 'Paulo Coelho'  # El autor es Paulo Coelho en este caso
            # Eliminar número, punto y espacios al inicio del texto
            texto_limpio = texto.lstrip('0123456789. ')
            # Crear un objeto Frase y agregarlo a la lista
            nueva_frase = Frase(texto_limpio, autor)
            frases_Cohelo.append(nueva_frase)
            contador += 1  # Incrementar el contador

        return frases_Cohelo, contador
    else:
        print('No se pudo obtener el contenido de la página')


if __name__ == "__main__":
    frases, total = obtener_frases_Cohelo()
    for frase in frases:
        print(f'Frase: {frase.texto}\nAutor: {frase.autor}\n')
    print(f'Las frases de Paulo Coelho son: {total}')


