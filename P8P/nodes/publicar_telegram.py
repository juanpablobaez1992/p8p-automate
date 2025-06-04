import requests


def ejecutar(entrada):
    params = entrada.get('params', {})
    token = params.get('token')
    chat_id = params.get('chat_id')
    mensaje = params.get('mensaje', '')
    if not token or not chat_id:
        raise ValueError('Faltan token o chat_id')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': mensaje})
    return {'telegram': 'enviado'}
