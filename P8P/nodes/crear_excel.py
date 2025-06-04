import openpyxl
from openpyxl import Workbook


def ejecutar(entrada):
    datos = entrada.get('datos') or entrada['params'].get('datos', [])
    archivo = entrada['params'].get('archivo', 'salida.xlsx')
    wb = Workbook()
    ws = wb.active
    for fila in datos:
        ws.append(fila)
    wb.save(archivo)
    return {'archivo_excel': archivo}
