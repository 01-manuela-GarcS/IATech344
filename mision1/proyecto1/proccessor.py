import re
# ====================
#  FUNCION clean_id
# Eliminar caracteres no númericos de un documento
# "cc75.888.56" = "7588856"
# ====================

def clean_id(value):
    # Elimina caracteres no númericos de un documento
    if value is None:
        return ""
    return re.sub(r'\D','',str(value))
    
# Cunaod llamemos a la función no tiene ningun vlaor va a devolver vacio. Toma todo lo que no e sun digito y que lo quite, el str string. con '\D' toma numeros.
#El archivo processor.py debe estar acompañado de el archivo test_pro (test unitarios), debe tenr el noimbre test y el nombre al cual le estamos aplicando las pruebas. Es importante entregarlo para ver las pruebas que se realizaron

# ====================
#  FUNCION marge_name
# Une nombre y apellido en un solo campo
# ====================

def merge_name(name, lastname):
    if name is None:
        name =""
    if lastname is None:
        lastname =""
    return f"{name} {lastname}".strip()

