
class Persona:
    
    #Constuctor
    def __init__(self):
        self.listaBD = []
               
    # Metodos del CRUD
    
    def Insertar(self,id,nom,edad ):
        self.listaBD.append( { "Id":id,"Nombre":nom,"Edad":edad } )
           
    def consultarTodos(self):
        print(self.listaBD)
        
    def buscarUsuario(self,id):
        for usuario in self.listaBD:
            if usuario['Id'] == id:
                print( usuario)
            else:
                print("Usuario no encontrado")
        
    def eliminar(self,id):
        for usuario in self.listaBD:
            if usuario['Id'] == id:
                self.listaBD.remove(usuario)
                print(":: Usuario Eliminado ::")
                
            self.consultarTodos()
        
    def editar(self,id,nom,edad):
        for usuario in self.listaBD:
            if usuario['Id'] == id:
                usuario['Nombre'] = nom
                usuario['Edad'] = edad
                print(":: Usuario Editado ::")
                
            self.consultarTodos()
                
        
        