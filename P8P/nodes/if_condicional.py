"""Evalúa una condición simple y redirige el flujo."""


def ejecutar(entrada):
    valor = entrada['params'].get('valor')
    comparador = entrada['params'].get('comparador', '==')
    contra = entrada['params'].get('contra')
    resultado = False
    if comparador == '==':
        resultado = valor == contra
    elif comparador == '!=':
        resultado = valor != contra
    return {'condicion': resultado}
