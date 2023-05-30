"""
pip install requests

"""

import requests

def check_wordpress(url):
    response = requests.get(url)

    if 'wp-content' in response.text:
        print("El sitio web utiliza WordPress.")

        # Extraer información de la plantilla
        theme_start = response.text.find('wp-content/themes/') + len('wp-content/themes/')
        theme_end = response.text.find('/', theme_start)
        theme_name = response.text[theme_start:theme_end]

        print(f"La plantilla utilizada es: {theme_name}")
    else:
        print("El sitio web no parece utilizar WordPress.")

# Ejemplo de uso
check_wordpress('https://www.ejemplo.com')  # Reemplaza 'https://www.ejemplo.com' con la URL del sitio web que deseas analizar
