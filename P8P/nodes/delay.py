import time


def ejecutar(entrada):
    segundos = float(entrada['params'].get('segundos', 1))
    time.sleep(segundos)
    return {'delay': segundos}
