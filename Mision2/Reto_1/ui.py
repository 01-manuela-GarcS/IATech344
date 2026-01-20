# UI.PY MODIFICADA PARA LA REALIZACIÓN DEL RETO_1

# ui.py
# Capa de interfaz gráfica (Tkinter). Este archivo se encarga únicamente de la interacción con el usuario.

import tkinter as tk
# tkinter es la librería estándar de Python
#tk se utiliza para crear ventana, botones, etc.
from tkinter import messagebox, filedialog
from controller import procesar_instruccion

# Variable para almacenar la ruta del Excel seleccionado. Guarda la rutna completa del archivo Excel seleccionado, empieza con None ya que al inicio no hay ningun archivo cargado
archivo_excel = None

# Seleccionar un archivo Excel y guarda en la variable global archivo_excel.
def seleccionar_excel():
    global archivo_excel
    #Abre una ventana para elegir el archivo y solo permitira archivo tipo "*.xlsx"
    archivo_excel = filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivo Excel", "*.xlsx")]
    )
    # Mensaje al usuario si selecciona el archivo o no
    if archivo_excel:
        messagebox.showinfo("Éxito", "Archivo seleccionado.")
    else:
        messagebox.showerror("Error", "Archivo no seleccionado.")

#Esta función se ejecutara cuando se presione el botón
def ejecutar_instruccion():
    global archivo_excel
    #Mostrara un error si se intenta ejecutar una instrucción si seleccionar un archivo
    if not archivo_excel:
        messagebox.showerror("Error", "Primero seleccione un archivo Excel")
        return
    #Este es el campo de texto y en get() devuelve lo que escribió el usuario
    texto = entrada.get()
    #Muestra error si se intenta ejecutar sin ingresar ninguna instrucción
    if not texto.strip():
        messagebox.showwarning("Error", "Ingrese una instrucción")
        return

    # Llama al controller para procesar la instrucción sobre el archivo seleccionado
    exito, mensaje = procesar_instruccion(texto, archivo_excel)
    #Muestra el resultado al finalizar
    if exito:
        messagebox.showinfo("Resultado", mensaje)
    else:
        messagebox.showerror("Error", mensaje)

# Crea la ventana principal
def iniciar_app():
    global entrada
    # Ventana principal y se define el titulo y su tamaño
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x400")
    # Botón para seleccionar archivo Excel
    tk.Button(root, text="Seleccionar archivo Excel", command=seleccionar_excel).pack(pady=50)
    # Etiqueta e input para instrucción (campo de texto)
    tk.Label(root, text="Por favor, escriba una instrucción.").pack(pady=10)
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)
    # Botón para ejecutar la instrucción sobre el excel seleccionado
    tk.Button(root, text="Ejecutar instrucción", command=ejecutar_instruccion).pack(pady=50)

    #Bucle principal. Mantiene la ventana abierta, ejecuta las funciones
    root.mainloop()
