# test_logger.py
import os
import time
import logger

# Creamos un archivo ficticio y le cambiamos su fecha de modificación a hace 31 días
def test_log_rotation():
    filename = "old_history.log"
    with open(filename, "w") as f:
        f.write("test content")
    
    # Simulamos que el archivo tiene 31 días de antigüedad
    # (31 días * 24 horas * 60 minutos * 60 segundos)
    past_time = time.time() - (31 * 24 * 60 * 60)
    os.utime(filename, (past_time, past_time))
    
    # Ejecutamos la lógica de limpieza
    logger.rotate_logs(filename)
    
    # El archivo debería haber sido borrado
    assert not os.path.exists(filename)
    print("Test de rotación de logs pasado con éxito.")

if __name__ == "__main__":
    try:
        test_log_rotation()
    except AssertionError:
        print("Test falló: El archivo no fue borrado.")
        exit(1)
