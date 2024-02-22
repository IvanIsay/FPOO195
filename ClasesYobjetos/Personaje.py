class Personaje:
    
    #atibuto de personaje
    especie= "Humano"
    nombre="John"
    altura= 2.18
    
    #Metodos del personaje
    def correr(self,estado):
        if(estado):
            print("el personaje "+ self.nombre +" esta corriendo")
        else:
            print("el personaje "+ self.nombre +" esta muerto")   
            
            
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada") 
        
    def recargarArma(self, municion):
        cargador= 25
        cargador= cargador + municion
        print("Arma recargada al "+ str(cargador)+ "%")
      
      
 #creamos el objeto Spartan de la clase personaje       
Spartan = Personaje()

#Usamos los atributos Spartan
print(Spartan.nombre)
print(Spartan.especie)
print(Spartan.altura)

#Usamos los Metodos del Spartan
Spartan.correr(False)
Spartan.lanzarGranada()
Spartan.recargarArma(25)