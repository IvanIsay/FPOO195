from tkinter import Tk,Frame

#1.Creamos la ventana
Ventana= Tk() # Uso de POO creando un Obj Ventana
Ventana.title("Ejemplo con 3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
seccion1= Frame(Ventana,bg="red")
seccion1.pack(expand= True,fill='both')

seccion2= Frame(Ventana ,bg="yellow")
seccion2.pack(expand= True,fill='both')

seccion3= Frame(Ventana, bg="blue")
seccion3.pack(expand= True,fill='both')


#Ejecuta la ventana
Ventana.mainloop()