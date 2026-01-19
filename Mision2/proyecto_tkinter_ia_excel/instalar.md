### Primero miramos la versión de Python    python --version
### Ingresamos a la carpeta en la que vamos a crear una nueva carpeta   cd .\Mision2\ 
### Luego creamos la carpeta con la version de python   python -m venv venv3.13.3
python -m venv venv  
### Activamos el entorno virtual    venv3.13.3\scripts\activate
venv\scripts\activate 
### Con el siguiente comando actualizamos pip (Actualiza pip, que es el gestor de paquetes de Python (sirve para instalar librerías))
python.exe -m pip install --upgrade pip
### Nos vamos a la carpeta proyecto_tkinter_ia_excel    cd .\proyecto_tkinter_ia_excel\
### Y luego damos el comando    
pip install -r requirements.txt