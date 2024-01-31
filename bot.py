import requests
from requests.auth import HTTPBasicAuth
import base64

def subir_a_github(archivo_local, archivo_remoto, token):
    url = f'https://api.github.com/repos/RubenMA12/passwords/contents/{archivo_remoto}'

    # Leer el contenido del archivo local
    with open(archivo_local, 'rb') as file:
        contenido_base64 = base64.b64encode(file.read()).decode('utf-8')

    # Crear un diccionario con los datos para enviar
    datos = {
        "message": "Subir archivo desde script Python",
        "content": contenido_base64
    }

    # Configurar la autenticación usando el token de acceso
    auth = HTTPBasicAuth('SyntaxMA12', token)

    # Realizar una solicitud PUT para subir el archivo
    respuesta = requests.put(url, auth=auth, json=datos)

    if respuesta.status_code == 201:
        print(f"El archivo {archivo_local} se ha subido correctamente a GitHub.")
    else:
        print(f"Error al subir el archivo a GitHub. Código de estado: {respuesta.status_code}")
        print(respuesta.text)

def run():
    archivo_local = 'passwd'
    archivo_remoto = 'contras/passwd.txt'  # Especifica la ruta en tu repositorio
    github_token = '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'  # Necesitarás generar un token de acceso en tu cuenta de GitHub

    subir_a_github(archivo_local, archivo_remoto, github_token)

if __name__ == "__main__":
    run()
