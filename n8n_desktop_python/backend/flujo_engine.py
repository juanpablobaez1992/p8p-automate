import json
import importlib.util
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NODES_DIR = BASE_DIR / 'nodes'


def cargar_modulo(nombre):
    ruta = NODES_DIR / f'{nombre}.py'
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def ejecutar_flujo(ruta_flujo):
    with open(ruta_flujo) as f:
        pasos = json.load(f)

    datos = {}
    logs = []
    for paso in pasos:
        tipo = paso['tipo']
        params = paso.get('params', {})
        modulo = cargar_modulo(tipo)
        entrada = {'params': params}
        entrada.update(datos)
        try:
            salida = modulo.ejecutar(entrada)
            datos.update(salida)
            logs.append({'id': paso['id'], 'nodo': tipo, 'salida': salida})
        except Exception as e:
            logs.append({'id': paso['id'], 'nodo': tipo, 'error': str(e)})
            break
    return logs
