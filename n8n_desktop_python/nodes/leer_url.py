import requests

def ejecutar(entrada):
    url = entrada.get('url') or entrada['params'].get('url')
    response = requests.get(url)
    return {'html': response.text}
