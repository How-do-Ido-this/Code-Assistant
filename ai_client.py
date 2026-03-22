# ai_client.py
import os
import google.generativeai as genai
from prompts import REVIEWER_PROMPT

# Configuración inicial al cargar el módulo
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def get_analysis(code: str) -> str:
    """Envía el código a la IA y retorna el análisis."""
    try:
        # Usamos el modelo gemini-2.5-flash
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Combinamos nuestra instrucción (prompt) con el código
        full_prompt = f"{REVIEWER_PROMPT}\n\nCÓDIGO A ANALIZAR:\n{code}"
        
        # Enviamos la petición
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error al conectar con la IA: {e}"
