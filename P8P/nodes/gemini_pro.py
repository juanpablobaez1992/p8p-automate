import google.generativeai as genai


def ejecutar(entrada: dict) -> dict:
    """Utiliza Google Generative AI para obtener una respuesta."""
    params = entrada.get('params', {})
    api_key = entrada.get('api_key') or params.get('api_key')
    mensaje = entrada.get('mensaje') or params.get('mensaje')

    if not api_key:
        raise ValueError('Falta api_key para Gemini')
    if not mensaje:
        raise ValueError('Falta mensaje para enviar al modelo')

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    respuesta = model.generate_content(mensaje)
    texto = respuesta.text if hasattr(respuesta, 'text') else str(respuesta)

    return {'respuesta': texto}
