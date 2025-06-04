"""Nodo para traducir texto. Implementación simplificada sin API externa."""

def ejecutar(entrada):
    texto = entrada.get('texto') or entrada['params'].get('texto', '')
    destino = entrada['params'].get('destino', 'en')
    # Implementación mínima: no traduce realmente, solo indica idioma de destino
    return {'texto_traducido': f"[{destino}] {texto}"}
