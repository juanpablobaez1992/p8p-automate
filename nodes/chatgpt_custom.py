import openai


def ejecutar(entrada: dict) -> dict:
    """Envía un mensaje a la API de OpenAI y retorna la respuesta."""
    params = entrada.get('params', {})
    api_key = entrada.get('api_key') or params.get('api_key')
    mensaje = entrada.get('mensaje') or params.get('mensaje')
    modelo = entrada.get('modelo') or params.get('modelo', 'gpt-4')
    instruccion = entrada.get('instruccion') or params.get('instruccion')

    if not api_key:
        raise ValueError('Falta api_key para OpenAI')
    if not mensaje:
        raise ValueError('Falta mensaje para enviar al modelo')

    openai.api_key = api_key

    messages = []
    if instruccion:
        messages.append({"role": "system", "content": instruccion})
    messages.append({"role": "user", "content": mensaje})

    respuesta = openai.ChatCompletion.create(
        model=modelo,
        messages=messages
    )

    contenido = respuesta.choices[0].message.content.strip()
    return {'respuesta': contenido}
