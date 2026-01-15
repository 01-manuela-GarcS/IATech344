# Clase IA
## 🤖 Comandos de Consola

```
# Es el titulo del README
```

###
![alt text](image.png)
```
python --version ó py --version
```

![alt text](image-1.png)
```
git --version
git init Iniciamos un repositorio
git add . Apuntar los archivos
git commit -m "nombre del commit"
```

![alt text](image-2.png)
```
git branch -M main
git remote add origin https://github.com/01-manuela-GarcS/IATech344.git
git push -u origin main
```

```
main rama principal para el despliegue
master donde se hacen las prueba, cuando la version ya este lista se sincroniza main y master

Navegar entre las carpetas
cd .\nombrecarpeta\ (si se van a ingresar a más carpetas cd .\nombrecarpeta\nombrecarpeta\)
Es como para ir entrando en las carpetas
cd ..
Es para salir de las carpetas
```

### Atajos de Teclado
```
Ctrl + u
alt + shift + ↓/↑ = Duplica la linea del código
alt + shift + a para crear un comentario
```

### Subir cambios
```
Para subir los cambios a github (1. git add .; 2. git commit -m "v1"; 3. git push)
el verde me indica que es un archivo nuevo que no existe en el repositorio.

commit la recopliacion de los nuevos archivos
Podemos seleccionar la rama main o master
push es el encargado de subir la información al git
```


### Entornos virtuales y Automatización
```
pip list
Lista de librerias

python -m venv myentorno
Crea un entorno virtual (ejem: python -m venv env3_13_3 (con el nombre se especifico la vesión de python)) (al crear el entorno se crean las carpetas Include, Lib, Script y los archivos .gitingnore y pyvenv.cfg)

dir
Directorio

env3_13_3\scripts\activate
Para activar el entorno y todas las librerias que instale se guardaran en este entorno

PowerShell como administrador
set-ExecutionPolicy Unrestricted   y luego S
Permite ejecutar scripts en el equipo (cuando al momento de activar el entorno no nos lo permite)

Para "actualizar" la carpeta de Profesores que es la que hemos clonado, lo mejor es hacelo por separado, es decir, en lugar de que lo hagos en la carpeta donde se encuentran las dos, seleccionar solo a una en este caso a Profesores y en la parte de abajo (inferior izquierda, le damos clic a el ciruclo con las flechas (sincronizar))
```

### Activar entrono virtual
```
Para volver a ACTIVAR el Entorno Virtual, debemos, perimero nos ubicamos en la carpeta donde esta el entorno virtual cd .\Personal\mision1\proyecto1\ y luego lo activamos env3_13_3\scripts\activate
```
### Desactivar entorno virtual
```
Para DESACTIVAR el Entorno Virtual, debemos, en la temrinar escribir el comando de deactivate
```


### Python (Entrenamiento)
```
#
Para comentar

import re
print("librería cargada correctamente")
Importaruna libreria, es la libreria (libreria estandar, la cual ya viene dentro del paquete de python), lo que colocamos dentro de las "" es lo que se muestra al ususario. Podemos usar """" para que las comillas internas las tomen como un caracter (el cual aparecera el texto con las comillas)

pip list
Para conocer la versión de la libreria pip
python entrenamiento.py  (el cual es el nombre de la pagina python que estamos trabajando)
Y luego cargamos la libreria en el archivo de python que vamos a utilizar
```

###
```

```