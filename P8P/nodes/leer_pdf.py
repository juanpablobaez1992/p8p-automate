import fitz  # PyMuPDF


def ejecutar(entrada):
    archivo = entrada.get('archivo') or entrada['params'].get('archivo')
    if not archivo:
        raise ValueError('Se requiere ruta de PDF')
    doc = fitz.open(archivo)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return {'texto_pdf': texto}
