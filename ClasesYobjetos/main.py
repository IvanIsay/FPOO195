from Personaje import *
from Armas import *


#solicitar datos Spartan
print("===== Datos de Heroe ========")
nombreS= input("Escribe el nombre de tu Spartan: ")
especieS= input("Escribe la especie de tu Spartan: ")
alturaS= float(input("Escribe la alturatu Spartan: "))
print("")


#solicitar datos del Nemesis
print("===== Datos del Villano ========")
nombreN= input("Escribe el nombre del Nemesis: ")
especieN= input("Escribe la especie del Nemesis: ")
alturaN = float(input("Escribe la altura del Nemesis: "))
print("")

#creamos el objeto Spartan de la clase personaje       
Spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(especieN,nombreN,alturaN)
Arma= Armas()


#Usamos los atributos Spartan
print("===== El objeto Spartan contiene ========")
print(Spartan.getNombre())
print(Spartan.getEspecie())
print(Spartan.getAltura())
print("")

#Usamos los atributos Nemesis
print("===== El objeto Nemesis contiene ========")
print(Nemesis.getNombre())
print(Nemesis.getEspecie())
print(Nemesis.getAltura())
print("")


#Usamos los Metodos del Spartan

print("======  Acciones del Objeto Spartan ===")
Spartan.correr(False)
Spartan.lanzarGranada()
print("")

print("======  Acciones del Objeto Nemesis ===")
Nemesis.correr(True)
Nemesis.lanzarGranada()
print("")

#Usamos los Metodos del Arma

print("====== Selecciona arma del Spartan ======")
Arma.seleccionarArma(Spartan.getNombre())
Arma.recargarArma(65)
print("")

print("====== Selecciona arma del Villano ======")
Arma.seleccionarArma(Nemesis.getNombre())
Arma.recargarArma(10)
print("")

#cambiamos atributos del objeto Nemesis

print("====== Cambio de Villano ======")

cambioN= input("Escribe el nombre del nuevo villano: ")
Nemesis.setNombre(cambioN)
cambioE= input("Escribe la especie del nuevo villano: ")
Nemesis.setEspecie(cambioE)
print("")

print("====== Villano Nuevo ======")
print(Nemesis.getNombre())
print(Nemesis.getEspecie())
print("")


Spartan.__pensar()
 


