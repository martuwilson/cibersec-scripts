"""

pip install requests
pip install colorama
pip install argparse

"""

import requests
import argparse
from colorama import Fore, Style

def check_directory(target_url, directory):
    url = target_url + directory

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Directorio encontrado: {url}")
    except requests.ConnectionError:
        pass

def main():
    parser = argparse.ArgumentParser(description='Script para buscar directorios privados en un sitio web')
    parser.add_argument('-t', '--target', help='URL del sitio web objetivo', required=True)
    args = parser.parse_args()

    target_url = args.target

    common_directories = [
        '',
        'admin/',
        'admin/login/',
        'admin/dashboard/',
        'private/',
        'secret/',
        'hidden/',
    ]

    print(f"Iniciando búsqueda de directorios privados en: {target_url}\n")

    for directory in common_directories:
        check_directory(target_url, directory)

if __name__ == '__main__':
    main()
