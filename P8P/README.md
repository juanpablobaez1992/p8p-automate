# P8P

Plataforma local y visual para automatizar tareas mediante flujos de nodos Python.
Incluye un logotipo inspirado en n8n con la "P" de Python.

Viene con más de 50 flujos listos para usar y la misma cantidad de nodos
disponibles para personalizar tus automatizaciones.

## Ejecución

```bash
python app.py
```

Establece `FLASK_ONLY=1` si no deseas usar PyWebview.

## Uso visual

1. Selecciona un flujo en la página principal.
2. Indica desde qué paso deseas iniciar la ejecución.
3. Haz clic en *Ejecutar flujo* para ver los resultados paso a paso.
4. Descarga o carga archivos JSON para compartir tus flujos.
5. Cambia al modo avanzado para editar el código de cualquier nodo.
6. Activa el **Modo Oscuro** si lo prefieres.

## Crear nuevos flujos

Agrega archivos `.json` en la carpeta `flujos/` siguiendo el formato de ejemplo.

## Crear nuevos nodos

Crea un archivo `.py` en `nodes/` con la función `ejecutar(entrada: dict) -> dict`.

## Empaquetar con PyInstaller

```bash
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```
