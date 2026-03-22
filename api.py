# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv # Carga variables desde .env
from ai_client import get_analysis
import logger

# Carga variables de entorno
load_dotenv()

# Iniciamos la aplicación
app = FastAPI(title="Code Assistant API")

# Definimos el esquema de datos esperado (Validación automática)
class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/analyze")
async def analyze(request: CodeRequest):
    # Validación simple: que el código no esté vacío
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="El campo 'code' no puede estar vacío.")

    # 1. Llamamos al cliente de IA
    resultado = get_analysis(request.code)
    
    # 2. Guardamos el historial (reutilizamos la lógica anterior)
    logger.log_analysis(f"API - {request.language}", resultado)
    
    # 3. Retornamos la respuesta estructurada
    return {"analysis": resultado}

@app.get("/history")
async def get_history():
    # Llamamos a nuestro logger para recuperar el historial
    historial = logger.get_history()
    return {"history": historial}
