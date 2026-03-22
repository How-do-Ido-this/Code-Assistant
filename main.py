# main.py
import sys
import os
from dotenv import load_dotenv # Carga variables desde .env
from ai_client import get_analysis
import logger

# Cargamos variables antes de cualquier uso
load_dotenv()

def get_code_from_source():

    # 1. Verificamos que se haya pasado un archivo
    if len(sys.argv) < 2:
        print("Uso: python main.py <ruta_del_archivo>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    # 2. Validación: ¿existe el archivo?
    if not os.path.exists(file_path):
        print(f"Error: El archivo '{file_path}' no existe.")
        sys.exit(1)
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read(), file_path
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)

def main():
    # 3. Validación PROACTIVA: API Key configurada
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: La variable de entorno 'GEMINI_API_KEY' no está configurada.")
        sys.exit(1)

    # Obtenemos el código y la ruta del archivo
    code, file_path = get_code_from_source()

    # Validación: ¿el código está vacío?
    if not code.strip():
        print("Error: El archivo está vacío.")
        return

    print(f"\nAnalizando archivo: {file_path}...")
    resultado = get_analysis(code)
    print(resultado)
    
    # 4. Guardamos el historial del análisis
    logger.log_analysis(file_path, resultado)

if __name__ == "__main__":
    main()

