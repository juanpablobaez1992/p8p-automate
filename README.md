# p8p-automate

Este repositorio contiene ejemplos y proyectos automatizados. Revisa la carpeta `n8n_desktop_python/` para una app de escritorio inspirada en n8n.

## Nodos de IA

En la raíz del proyecto se incluyen dos nodos para conectarse a modelos de lenguaje:

- `nodes/chatgpt_custom.py` utiliza la API de OpenAI.
- `nodes/gemini_pro.py` usa la API de Google Generative AI.

Cada nodo implementa la función `ejecutar(entrada: dict) -> dict` y puede ser importado dinámicamente por el motor de flujos.

### Instalación de dependencias

```bash
pip install openai google-generativeai
```

### Crear nuevos nodos

1. Crea un archivo dentro de la carpeta `nodes/`.
2. Define una función `ejecutar(entrada: dict) -> dict` que procese los parámetros y devuelva un diccionario.
3. El nombre del archivo debe coincidir con el campo `tipo` del flujo JSON.

### Integrar en el flujo P8P

Los flujos se definen como listas de pasos en la carpeta `flujos/`. Un ejemplo se encuentra en `flujos/flujo_ia.json`.
Al ejecutar el motor, la salida de cada nodo se pasa como entrada al siguiente.

Cada nodo es modular, por lo que es sencillo incorporar soporte para otros modelos (por ejemplo Ollama u opciones locales) creando nuevos archivos en `nodes/`.
