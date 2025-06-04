import os
from flask import Flask, render_template, request, jsonify
import webview
from backend.flujo_engine import ejecutar_flujo

app = Flask(__name__)

@app.route('/')
def index():
    flujos = {}
    for carpeta in os.listdir('flujos'):
        ruta = os.path.join('flujos', carpeta)
        if os.path.isdir(ruta):
            flujos[carpeta] = [f for f in os.listdir(ruta) if f.endswith('.json')]
    nodes = [f for f in os.listdir('nodes') if f.endswith('.py')]
    return render_template('index.html', flujos=flujos, nodes=nodes)

@app.route('/run', methods=['POST'])
def run_flujo():
    data = request.get_json()
    flujo_path = os.path.join('flujos', data['flujo'])
    resultados = ejecutar_flujo(flujo_path)
    return jsonify(resultados)

@app.route('/node/<nombre>', methods=['GET', 'POST'])
def editar_nodo(nombre):
    ruta = os.path.join('nodes', nombre)
    if request.method == 'POST':
        codigo = request.form['code']
        with open(ruta, 'w') as f:
            f.write(codigo)
        return 'guardado'
    with open(ruta) as f:
        return f.read()

def start():
    if os.environ.get('FLASK_ONLY'):
        app.run(debug=True)
    else:
        webview.create_window('P8P', app)
        webview.start()

if __name__ == '__main__':
    start()
