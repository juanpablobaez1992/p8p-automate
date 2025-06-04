# n8n Desktop Python

Esta aplicación emula la lógica de n8n en un entorno de escritorio usando Python. Utiliza Flask como backend web y PyWebview para ejecutarse como app nativa.

## Instalación

```bash
pip install -r requirements.txt
```

## Cómo correr

```bash
python app.py
```

Si deseas correr el servidor Flask sin PyWebview, puedes establecer la variable de entorno `FLASK_ONLY=1`.

## Crear nuevo nodo

1. Crea un archivo `.py` dentro de la carpeta `nodes/`.
2. Implementa una función `ejecutar(entrada: dict) -> dict`.
3. El resultado retornado se pasará al siguiente nodo del flujo.

## Crear nuevo flujo

1. Genera un archivo `.json` en la carpeta `flujos/`.
2. Define una lista de pasos donde cada paso indica el `id`, el `tipo` (nombre del nodo) y sus `params`.

Ejemplo:

```json
[
  {"id": "1", "tipo": "leer_url", "params": {"url": "https://example.com"}},
  {"id": "2", "tipo": "extraer_titulo", "params": {}},
  {"id": "3", "tipo": "guardar_txt", "params": {"archivo": "titulo.txt"}}
]
```

## Empaquetar como ejecutable

Para crear un ejecutable puedes usar PyInstaller:

```bash
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```

Esto generará un archivo `dist/app.exe` (en sistemas Windows). Cambia la extensión a `.txt` si no deseas generar binarios directamente.

## Estructura del proyecto

```
app.py
backend/
  flujo_engine.py
nodes/
  leer_url.py
  extraer_titulo.py
  guardar_txt.py
flujos/
  flujo_demo.json
templates/
  index.html
static/
  style.css
requirements.txt
```

## Funcionalidades clave

- Carga flujos desde archivos JSON.
- Ejecución dinámica de nodos Python.
- Flujo encadenado: la salida de un nodo es la entrada del siguiente.
- Manejo simple de errores: si un nodo falla, se detiene la ejecución y se registra el error.
- Interfaz web con resultados de cada paso y editor básico de nodos.
