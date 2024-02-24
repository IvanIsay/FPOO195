from Personaje import *
from Armas import *

#creamos el objeto Spartan de la clase personaje       
Spartan = Personaje()
Arma= Armas()

#Usamos los atributos Spartan
print(Spartan.nombre)
print(Spartan.especie)
print(Spartan.altura)

#Usamos los Metodos del Spartan
Spartan.correr(False)
Spartan.lanzarGranada()

#Usamos los Metodos del Arma
Arma.seleccionarArma(Spartan.nombre)
Arma.recargarArma(65)



