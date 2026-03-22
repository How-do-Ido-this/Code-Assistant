# 🤖 Senior Code Reviewer AI

Un asistente de revisión de código inteligente diseñado para proporcionar feedback de nivel senior, detectando bugs, malas prácticas, riesgos y sugiriendo mejoras.

## 🚀 Características
*   **Revisión experta**: Formato estructurado (Resumen, Problemas, Mejoras, Tests, Riesgos).
*   **CLI profesional**: Análisis robusto basado exclusivamente en archivos de código.
*   **API REST**: Endpoint integrado mediante FastAPI.
*   **Gestión de Logs**: Historial automático con rotación de archivos (+30 días).

## 💻 Uso (CLI)
Para analizar un archivo, pásalo como argumento:
```bash
python main.py ruta/a/tu_archivo.cpp
```

## 🌐 Uso (API)
Levanta el servidor:
```bash
uvicorn api:app --reload
```
Accede a la documentación interactiva en: `http://127.0.0.1:8000/docs`

---
*Configura tu API Key mediante `GEMINI_API_KEY` en tus variables de entorno.*
