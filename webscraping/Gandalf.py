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

def obtener_frases_Gandalf():
    
    url = 'https://www.lifeder.com/frases-de-gandalf/'

   
    response = requests.get(url)

  
    if response.status_code == 200:
        # Parsear el HTML usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las frases dentro de los elementos <span> con el estilo específico
        frases_elements = soup.find_all('span', style='color: #000000;')

        # Omitir las primeras dos frases
        frases_a_mostrar = frases_elements[2:]

       
        frases_gandalf = []

      
        contador = 0

        
        for frase_element in frases_a_mostrar:
            texto = frase_element.get_text(strip=True)  # Obtener el texto de la frase
            autor = 'Gandalf' 

            # Limpiar el texto 
            # Eliminar número, punto y espacios al inicio del texto
            texto_limpio = texto.lstrip('- ')
             # Verificar si el texto está vacío antes de crear el objeto Frase y agregarlo a la lista
            if texto_limpio:  # Si el texto no está vacío
                nueva_frase = Frase(texto_limpio, autor)
                frases_gandalf.append(nueva_frase)
                contador += 1 

        return frases_gandalf, contador
    else:
        print('No se pudo obtener el contenido de la página')


if __name__ == "__main__":
    frases, total = obtener_frases_Gandalf()
    for frase in frases:
        print(f'Frase: {frase.texto}\nAutor: {frase.autor}\n')
    print(f'Las frases de Gandalf son: {total}')
