# logger.py
import os
import datetime

def rotate_logs(filename="history.log"):
    # 1. Comprobamos si el archivo existe
    if os.path.exists(filename):
        # Obtenemos la fecha de última modificación del archivo
        mtime = os.path.getmtime(filename)
        last_modified = datetime.datetime.fromtimestamp(mtime)
        
        # 2. Si tiene más de 30 días, lo borramos
        if (datetime.datetime.now() - last_modified).days > 30:
            os.remove(filename)

def log_analysis(filename: str, analysis_text: str):
    # 1. Ejecutamos la rotación antes de intentar escribir
    rotate_logs()
    
    # 2. Guardamos la entrada en el archivo
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n--- [{timestamp}] Revisión de: {filename} ---\n{analysis_text}\n"
    
    # Abrimos en modo 'a' (append) para añadir al final del archivo
    with open("history.log", "a", encoding="utf-8") as f:
        f.write(log_entry)

def get_history():
    # Si el archivo no existe, no hay historial todavía
    if not os.path.exists("history.log"):
        return "No hay historial disponible aún."
    
    # Leemos todo el contenido del log
    with open("history.log", "r", encoding="utf-8") as f:
        return f.read()
