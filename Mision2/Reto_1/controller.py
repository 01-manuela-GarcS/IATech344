# controller.py
# Coordina la interfaz, la IA y la lógica de Excel

from ia_interpreter import interpretar_texto
from processor import ejecutar_accion, proccess_excel_safe


def procesar_instruccion(texto):
    try:
        instruccion = interpretar_texto(texto)
        ejecutar_accion(instruccion)
        return True, "Instrucción ejecutada correctamente"
    except Exception as e:
        return False, str(e)

def procesar_excel_archivo(path):
    return proccess_excel_safe(path) 