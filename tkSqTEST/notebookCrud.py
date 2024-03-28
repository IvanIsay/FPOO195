from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from GenPDF import *
import os

objControlador= Controlador()
Objpdf = GenPDF()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())
    
def busUsuario():
    usuarioBD= objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Nada","Id no existe en BD")
    else:
        print(usuarioBD)
        
def generaPdf():
    if varTipdf.get() == "":
        messagebox.showwarning("Nombre obligatorio","Escribe un nombre para el PDF")
    else:
        pdf_path ="C:/laragon/www/FPOO195/"+str(varTipdf.get())+".pdf"
        Objpdf.add_page()
        Objpdf.chapter_body()
        Objpdf.output(str(varTipdf.get())+".pdf")
        messagebox.showinfo("Archivo Creado","PDF disponible en la carpeta de tu proyecto")
        os.system(f"start {pdf_path}")


# 1 crear la ventana
Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

#2. preparar el notebook para pestañas
panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

#3.definir las pesatañas del notebook
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)
pestana6= ttk.Frame(panel)

#4. agregamos las pestañas
panel.add(pestana1,text="Crear Usuario")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Editar Usuario")
panel.add(pestana5,text="Borrar Usuario")
panel.add(pestana6,text="Reportes en PDF")



#5. Pestaña 1:Formulario de Insert
Label(pestana1, text="Registro de Usuarios",fg="blue" ,font=("Modern",18)).pack()

var1= tk.StringVar()
Label(pestana1,text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1,text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1,text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1,text="Guardar usuario",command=ejecutaInsert).pack()


#6. Pestaña 2:Buscar Usuario

Label(pestana2, text="Buscar Usuario",fg="red" ,font=("Mono",18)).pack()

varBus= tk.StringVar()
Label(pestana2,text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2,text="Buscar usuario",command=busUsuario).pack()

Label(pestana2, text="Registrado:",fg="blue" ,font=("Mono",14)).pack()
tk.Text(pestana2,height=5, width=52).pack()


# Pestaña6:Reportes PDF

Label(pestana6, text="Reportes PDF",fg="green" ,font=("Mono",18)).pack()

varTipdf= tk.StringVar()
Label(pestana6,text="Titulo del PDF: ").pack()
Entry(pestana6, textvariable=varTipdf).pack()

Button(pestana6,text="Crear Reporte Usuarios",command=generaPdf ).pack()




Ventana.mainloop()