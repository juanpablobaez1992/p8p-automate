# Manual de Usuario de P8P

Bienvenido a **P8P**, la plataforma de automatización visual en Python.
Este manual explica cómo instalar la aplicación, cargar flujos y crear tus propios nodos.

## Instalación
1. Asegúrate de tener Python 3.10 o superior.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución
Ejecuta la aplicación con:
```bash
python app.py
```
Si deseas iniciar solo el servidor web sin la ventana de escritorio, define la variable de entorno `FLASK_ONLY=1`.

## Cargar y ejecutar flujos
1. Desde la página principal selecciona uno de los archivos JSON listados en la carpeta `flujos/`.
2. Presiona **Ejecutar flujo** para procesar cada paso. La salida de un nodo se pasa como entrada al siguiente.
3. Puedes descargar tus flujos o subir nuevos para compartirlos.

## Modo avanzado
Activa el modo desarrollador para editar el código de los nodos directamente desde la interfaz. Esto permite personalizar cada acción según tus necesidades.

## Crear nuevos nodos
1. Dentro de la carpeta `nodes/` crea un archivo `.py`.
2. Define en él la función:
   ```python
   def ejecutar(entrada: dict) -> dict:
       # tu código aquí
       return {}
   ```
3. Utiliza cualquier biblioteca de Python. El nombre del archivo debe coincidir con el campo `tipo` en tus flujos JSON.

## Compartir y extender
- Genera flujos propios y guárdalos en `flujos/`.
- Empaqueta la app como `.exe` usando PyInstaller:
  ```bash
  pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
  ```
- Integra P8P con otras aplicaciones mediante llamadas HTTP o lectura de archivos según el nodo que utilices.

## Soporte
Para preguntas o sugerencias abre un issue en el repositorio o envía un correo al mantenedor.

