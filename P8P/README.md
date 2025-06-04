# P8P

Plataforma local y visual para automatizar tareas mediante flujos de nodos Python.

## Ejecución

```bash
python app.py
```

Establece `FLASK_ONLY=1` si no deseas usar PyWebview.

## Uso visual

1. Selecciona un flujo en la página principal.
2. Haz clic en *Ejecutar flujo* para ver los resultados paso a paso.
3. Cambia al modo avanzado para editar el código de cualquier nodo.

## Crear nuevos flujos

Agrega archivos `.json` en la carpeta `flujos/` siguiendo el formato de ejemplo.

## Crear nuevos nodos

Crea un archivo `.py` en `nodes/` con la función `ejecutar(entrada: dict) -> dict`.

## Empaquetar con PyInstaller

```bash
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```
