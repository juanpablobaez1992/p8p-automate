# P8P Automate

**P8P** es una plataforma de automatización visual inspirada en n8n y potenciada con Python. Está pensada para docentes, equipos pastorales, periodistas y cualquier persona que quiera simplificar tareas repetitivas sin depender de la nube.

- 🟢 Diseño 100% local: crea y ejecuta flujos sin enviar datos a terceros.
- 🖥️ Interfaz intuitiva con modo básico y avanzado.
- ⚡ Ejecuta nodos Python listos para usar o modifica el código en vivo.

El proyecto incluye una versión de escritorio (carpeta `n8n_desktop_python/`) y una implementación simplificada en `P8P/`.

## Beneficios clave
- **Automatiza procesos** como lectura de RSS, manejo de PDFs o envío a Telegram.
- **Expandible** mediante nodos personalizados que siguen la función `ejecutar(entrada: dict) -> dict`.
- **Sin límites**: comparte tus flujos en archivos JSON y ejecútalos en cualquier equipo con Python.

Consulta el [manual de usuario](P8P/docs/MANUAL_USUARIO.md) para instrucciones paso a paso.

## Primeros pasos rápidos
```bash
pip install -r P8P/requirements.txt
python P8P/app.py
```

Descubre cómo la automatización puede agilizar tu día y libera tiempo para lo que realmente importa.
