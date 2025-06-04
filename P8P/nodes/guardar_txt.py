
def ejecutar(entrada):
    texto = entrada.get('titulo') or entrada.get('texto')
    nombre = entrada['params'].get('archivo', 'salida.txt')
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(texto)
    return {'archivo': nombre}
