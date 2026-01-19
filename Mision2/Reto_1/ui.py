# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import messagebox, filedialog
from controller import procesar_instruccion

# Variable para almacenar la ruta del Excel seleccionado
archivo_excel = None

# Seleccionar un archivo Excel y guarda en la variable global archivo_excel.
def seleccionar_excel():
    global archivo_excel
    archivo_excel = filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivo Excel", "*.xlsx")]
    )
    if archivo_excel:
        messagebox.showinfo("Archivo seleccionado.")
    else:
        messagebox.showerror("Archivo no seleccionado.")

def ejecutar_instruccion():
    global archivo_excel
    if not archivo_excel:
        messagebox.showerror("Primero seleccione un archivo Excel")
        return
    texto = entrada.get()
    if not texto.strip():
        messagebox.showwarning("Ingrese una instrucción")
        return

    # Llama al controller para procesar la instrucción sobre el archivo seleccionado
    exito, mensaje = procesar_instruccion(texto, archivo_excel)
    if exito:
        messagebox.showinfo("Resultado", mensaje)
    else:
        messagebox.showerror("Error", mensaje)

def iniciar_app():
    global entrada
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x400")
    # Botón para seleccionar archivo Excel
    tk.Button(root, text="Seleccionar archivo Excel", command=seleccionar_excel).pack(pady=50)
    # Etiqueta e input para instrucción
    tk.Label(root, text="EPor favor, escriba una instrucción.").pack(pady=10)
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)
    # Botón para ejecutar la instrucción
    tk.Button(root, text="Ejecutar instrucción", command=ejecutar_instruccion).pack(pady=50)

    root.mainloop()
