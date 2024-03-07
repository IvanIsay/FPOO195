from tkinter import Tk,Frame, Button,messagebox

#metodo para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.showerror('showerror','Error'))
    print(messagebox.showwarning('showwarning','Warninig'))
    print(messagebox.askokcancel(message="¿Desea continuar?",title="Soy el titulo"))

# Metodo para crear Botones
def addbtn():
    botonVerde.config(text="+")
    botonrosa= Button(seccion3,text="Nuevo",bg="#f7089c")
    botonrosa.configure(height=3,width=5)
    botonrosa.pack()

    

#1.Creamos la ventana
Ventana= Tk() # Uso de POO creando un Obj Ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
seccion1= Frame(Ventana,bg="#525050")
seccion1.pack(expand= True,fill='both')

seccion2= Frame(Ventana ,bg="#8f8c8c")
seccion2.pack(expand= True,fill='both')

seccion3= Frame(Ventana, bg="#b9b6b6")
seccion3.pack(expand= True,fill='both')

#3. posicionar Botones

#place
botonAzul= Button(seccion1,text="Azul", fg="#0733f7")
botonAzul.place(x=60,y=60, width=100, height=30)

#grid
botonNegro= Button(seccion2,text="Negro", fg="#FFFFFF",bg="#090909")
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0,column=1)

botonAmarillo= Button(seccion2,text="Amarillo",bg="#fbff00",command=mostrarMensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=1)

#pack
botonVerde= Button(seccion3,text="Verde",bg="#06e813",command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()


#Ejecuta la ventana
Ventana.mainloop()