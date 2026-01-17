# https://docs.python.org/es/3/library/tkinter.html

import tkinter as tk
#tk es basicamente el alias de tkinder
from tkinter import filedialog,messagebox
#Desde el módulo tkinter, quiero importar solo ciertas herramientas (filedialog,messagebox, es decir, dialogos de arvhicos y cajas de mensajes)
# También podemos ponele alias (minimizar un dato grande). Ejem: from tkinter import filedialog as fl,messagebox a mes
from proccessor import proccess_excel_safe

def seleccionar_excel():
    return filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivo Excel", "*.xlsx")]
    )
def on_clic_procesar():
    archivo = seleccionar_excel()
    exito,mensaje=proccess_excel_safe(archivo)
    #El mensaje llega desde proccessor desde donde se importa la función que se encarga de hacernos el proceso en la otra pagina (proccess_excel_safe)
    if exito:
        messagebox.showinfo("Proceso completado", mensaje)
    else:
        messagebox.showerror("Error",mensaje)
def iniciar_app():
    #Esta será nuestra ventana principal
    root = tk.Tk()
    root.title("Procesador de archivos Excel")
    root.geometry("400x400")
    root.resizable(False,False) #Para que no pueda mover ni el alto ni el anchivo

    boton = tk.Button(
        root,
        text="Seleccionar archivo Excel",
        command=on_clic_procesar,
        width=30,
        height=2
    )
    boton.pack(pady=60)

    root.mainloop()

iniciar_app()