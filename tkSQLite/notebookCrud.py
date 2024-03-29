from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador= Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())
    
def busUsuario():
    usuarioBD= objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Nada","Id no existe en BD")
    else:
        print(usuarioBD)


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

#4. agregamos las pestañas
panel.add(pestana1,text="Crear Usuario")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Editar Usuario")
panel.add(pestana5,text="Borrar Usuario")



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




Ventana.mainloop()