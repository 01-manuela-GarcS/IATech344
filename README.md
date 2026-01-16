# Clase IA
## 🤖 Comandos de Consola

```
# Es el titulo en README, el ## es como un subtitulo, etc. (es como el # es h1, ## h2, etc.)
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

Para activar una libreria en nuestro entorno virtual
pip install pytest

python.exe -m pip install --upgrade pip
Es para actualizar la libreria a la versión más reciente

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
Podemos poner el comando dir para ver la dirección del entorno virtual y el nombre que le colocamos al entorno
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

### Obtener resultado Python
```
Debimos activar el entorno para poder obtener el resultado
Para obtener el RESULTADO de las operaciones en la terminal escribimos py .\entrenamiento.py  Para el resultado
```

### Configuración de Python (Personalización)
```
Configuración (parte inferior izquierda), luego Command Palet (Cntrl + shift + p), >configure user snippets (Snippets:Configure Snippets), luego Python

En este entorno podemos crear nuestra propia versión que se adecue a lo que necesitamos

{
	"Separador de seccion Python":{
		"prefix": "sep",
		"body": [
			"# ====================",
			"# ${1: PUNTO DE ENTRADA}",
			"# ===================="
		],
		"description": "Crea un separador de secciones en python"
	}
}

Esto es una configuración de snippet (fragmento de código) para un editor. Es un snippet personalizado que te permite insertar rápidamente un bloque de comentarios en archivos Python.

sep + Tab

# ====================
#  PUNTO DE ENTRADA
# ====================
```