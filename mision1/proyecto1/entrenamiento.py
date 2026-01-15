# Este es un comentario

import re
print("librería cargada correctamente")
# Primero la libreria (import re) y luego el código print("librería cargada correctamente")

#Multi-linea
"""
Expresiones regulares en Python
"""

# Ejemplo Número 1
texto="Mi número es 12345"
resultado=re.search(r"\d+",texto)
print(resultado.group())
# El código que colocamos para el ejemplo nos indica Revisar en la variable texto todos los números
# r es revisar, "\d+" es la expresión regular y texto es variable

# texto y resultado son varibles, esto nos lo indica el = el cual hace refencia a una variable. Las variables son como una bolsita donde vamos colocando, sacando o reemplazando
# Una expresión regular es como algo que busca que se cumpla con ciertos criterios, por ejemplo, en un log de un correo la expresión regular seria un @ y un ., es decir, el log de un correo electronico mira que se cumplan con estos "criterios"
# La expresión regular en este caso es \d+ el cual detectara todos los número (cuando encuentre algún número lo ira tomando ("suamndolos" como al grupo donde estan todos los número que se encontraron en la variable), busca los número del 0 al 9)
# {Indica un diccionario} {"1", "uno"}  [indica una lista] [1,2,3,4,5]  Ambas son mutables,es decir, que sus valores se puede cambiar. (uno, dos) es una dupla la cual es un conjunto no mutable, es decir, que sus valosres no se pueden cambiar


texto="Mi número es 12345"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")
texto="Mi número es 12345-985"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")
# f es una propiedad, que permite combinar texto y variables en una sola linea
# el \d+" encuentra el numero y toma el resto de npumero que este luego de él pero si se encuentra un caracter los deja de tomar, como si los ignorara
# 