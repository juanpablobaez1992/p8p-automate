import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import webview
from backend.flujo_engine import ejecutar_flujo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FLUJOS_DIR = os.path.join(BASE_DIR, 'flujos')
NODES_DIR = os.path.join(BASE_DIR, 'nodes')

app = Flask(__name__)

@app.route('/')
def index():
    flujos = {}
    for carpeta in os.listdir(FLUJOS_DIR):
        ruta = os.path.join(FLUJOS_DIR, carpeta)
        if os.path.isdir(ruta):
            flujos[carpeta] = [f for f in os.listdir(ruta) if f.endswith('.json')]
    nodes = [f for f in os.listdir(NODES_DIR) if f.endswith('.py')]
    return render_template('index.html', flujos=flujos, nodes=nodes)

@app.route('/run', methods=['POST'])
def run_flujo():
    data = request.get_json()
    flujo_path = os.path.join(FLUJOS_DIR, data['flujo'])
    desde = int(data.get('desde', 0))
    resultados = ejecutar_flujo(flujo_path, desde=desde)
    return jsonify(resultados)

@app.route('/download/<path:archivo>')
def download_flujo(archivo):
    return send_from_directory(FLUJOS_DIR, archivo, as_attachment=True)

@app.route('/upload', methods=['POST'])
def upload_flujo():
    archivo = request.files.get('file')
    carpeta = request.form.get('carpeta', '')
    ruta = os.path.join(FLUJOS_DIR, carpeta)
    os.makedirs(ruta, exist_ok=True)
    if archivo:
        archivo.save(os.path.join(ruta, archivo.filename))
        return 'subido'
    return 'no-file', 400

@app.route('/node/<nombre>', methods=['GET', 'POST'])
def editar_nodo(nombre):
    ruta = os.path.join(NODES_DIR, nombre)
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
