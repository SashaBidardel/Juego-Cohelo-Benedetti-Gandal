import sys
import os

# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar el directorio padre al sys.path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)
import re
import requests
from bs4 import BeautifulSoup
from clases.Frase import Frase 

def obtener_frases_Benedetti():
    url = 'https://lamenteesmaravillosa.com/25-frases-del-maravilloso-mario-benedetti/'

    # Realizar la solicitud HTTP
    response = requests.get(url)

   
    if response.status_code == 200:
        # Parsear el HTML usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las frases dentro de los elementos <p> con la clase específica
        frases_elements = soup.find_all('p', class_='jsx-2049201783 c--grey-neutral-800')

        # Ignorar las primeras cinco y la última frase
        frases_a_mostrar = frases_elements[5:-1]

        
        frases_benedetti = []

      
        contador = 0

        
        for frase_element in frases_a_mostrar:
            texto = frase_element.get_text(strip=True)  # Obtener el texto de la frase
            autor = 'Mario Benedetti'  

            # Limpiar el texto 
            texto_limpio = re.sub(r'^\d+\.\s*', '', texto)  # Eliminar número y punto al principio
            texto_limpio = re.sub(r'[“”]', '', texto_limpio)   # Eliminar comillas dobles
            texto_limpio = texto_limpio.strip()  # Eliminar espacios al principio y al final

            # Crear un objeto Frase y agregarlo a la lista
            nueva_frase = Frase(texto_limpio, autor)
            frases_benedetti.append(nueva_frase)
            contador += 1 

        return frases_benedetti, contador
    else:
        print('No se pudo obtener el contenido de la página')


if __name__ == "__main__":
    frases, total = obtener_frases_Benedetti()
    for frase in frases:
        print(f'Frase: {frase.texto}\nAutor: {frase.autor}\n')
    print(f'Las frases de Mario Benedetti son: {total}')
