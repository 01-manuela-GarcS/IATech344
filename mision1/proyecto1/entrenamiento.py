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
# f es una propiedad, que nos permite combinar texto y variables en una sola linea. Y los espacios que pondemos los conserva
# el \d+" encuentra el numero y toma el resto de npumero que este luego de él pero si se encuentra un caracter los deja de tomar, como si los ignorara

texto="Mi número es 12345-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")
# Nos lo devuelve en una lista. En este caso, toma los primeros número del texto 12345 y luego los otros depués del caracter 985. ['12345', '985]
texto="Mi número es 123*45-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")
# El resultado es ['123', '45', '985]




documento="cc.75.055.60"

def clean_id(documento):
    return re.sub(r"\D","",documento)
print(clean_id(documento))
#Esta parte se llama la logica del negocio
# Funciones, las funciones en python se declaran con def, la sintaxis es def y el nombre con el que lo queramos llamar  def clean_id()  el nombre no puede tener espacios (si se ponen espacios es como si se pusiera una función y luego otra). 
# El nombre de la varibel documento no tiene nada que ver con , el documento es para todo lo que se tiene en ese "nivel" y el otro docmuento a lo de su "nivel"
#el documento cambia de color al estar haciendo uso de ella en la linea infeerios
#identifica solo texto y caracteres
#sub recibe, verifica el dato y le inficamos que lo remplace
#: parametro
# def es la palabra recervada, el nombre (no se inicia con mayuscula, a menos de que se vaya a declaras como clase, en este caso en una función), docuemnto es una funcion que recibe un parametro (alggo que se enviara), nos dara el resulado de sub. subb coge el conjunto de todo lo que nosotros no estamos necesitando, eliminara todos los caracteres por nada "" 
# para el resultado print, es mostrar en pantalla, kllamamos la funcipin clean
#elimina (no elimina, mas bien le indicamos que lo quite) todo lo que no es digito para ddenjar solo lo que es digito
# si ponemos " ", seria un cacater encmabio si ponemos "" no tiene ningun cacter
# El resultado es 7505560

documento1="75,055,60"

def clean_id(documento):
    return re.sub(r"\D",".",documento) #sub es como para reemplazar
print(clean_id(documento1))
#Todo lo que encuentre diferente, lo reemplaza por punto
#El resulado es 75.055.60  ya que toma los caracteres diferentes y los reemplaza por el punto, en esre caso reemplaza las , por los .

# py .\entrenamiento.py  Para el resultado