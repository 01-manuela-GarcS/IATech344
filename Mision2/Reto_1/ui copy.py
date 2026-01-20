# UI.PY MODIFICADA POR EL INSTRUCTOR

# ui.py

#import tkinter as tk
#from tkinter import messagebox,filedialog
#from controller import procesar_instruccion

#def iniciar_app():
    #root = tk.Tk()
    #root.title("Procesador Excel con IA")
    #root.geometry("500x300")
    #tk.Label(root, text="Escriba una instrucción en lenguaje natural").pack(pady=10)
    
    #def seleccionar_excel():
        #path= filedialog.askopenfilename(
        #title="Seleccionar archivo Excel",
        #filetypes=[("Archivo Excel","*.xlsx")]
        #)
        #if path:
           #messagebox.showinfo("Resultado", path)
           #path_label.config(text=path)
    
    #boton=tk.Button(
        #root,
        #text="Seleccionar archivo Excel",
        #command=seleccionar_excel,
        #width=30,
        #height=2
    #)
    #path_label=tk.Label(root,
                         #text="sin archivo",
                         #width=30,
                         #height=2
                         #)
    #path_label.pack(pady=10)
    
    #boton.pack(pady=15)

    #entrada = tk.Entry(root, width=60)
    #entrada.pack(pady=5)

    #def ejecutar():
        #texto = entrada.get()
        #path=path_label.cget("text")
        #exito, mensaje = procesar_instruccion(texto,path)

        #if exito:
            #messagebox.showinfo("Resultado", mensaje)
        #else:
            #messagebox.showerror("Error", mensaje)

    #tk.Button(root, text="Ejecutar instrucción", command=ejecutar).pack(pady=20)

    #root.mainloop()
