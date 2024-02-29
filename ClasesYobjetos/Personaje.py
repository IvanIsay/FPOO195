class Personaje:
    
    #atibuto de personaje
    #Declaramos el contructor para crear los objetos
    #cambiamos a privados los atributos del personaje
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #Metodos del personaje
    def correr(self,estado):
        if(estado):
            print("el personaje "+ self.__nombre +" esta corriendo")
        else:
            print("el personaje "+ self.__nombre +" esta muerto")   
            
            
    def lanzarGranada(self):
        print(self.__nombre+" Pego una granada") 
        
    def __pensar(self):
        print(self.__nombre +" Esta pensando") 
        
    
	# Definimos Getters y Setters para acceder a los atributos
    def getEspecie(self):
        return self.__especie
      
    def setEspecie(self, ex):
        self.__especie = ex

    def getNombre(self):
        return self.__nombre
      
    def setNombre(self, nx):
        self.__nombre = nx
        
    def getAltura(self):
        return self.__altura
      
    def setAltura(self, ax):
        self.__altura = ax
        
