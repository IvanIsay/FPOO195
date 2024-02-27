class Personaje:
    
    #atibuto de personaje
    # Declaramos el contructor para crear los objetos
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    #Metodos del personaje
    def correr(self,estado):
        if(estado):
            print("el personaje "+ self.nombre +" esta corriendo")
        else:
            print("el personaje "+ self.nombre +" esta muerto")   
            
            
    def lanzarGranada(self):
        print(self.nombre+" Pego una granada") 
        
