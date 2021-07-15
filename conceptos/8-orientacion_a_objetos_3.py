class Prueba:
    
    def __init__ (self, argumento1):
        self.__argumento1=argumento1  
        self.__argumento2=argumento1  
        self.__argumento3=argumento1  
        self.__argumento4=argumento1  
        self.__argumento5=argumento1  
        
    #################################################
        
    def get_argumento1(self):
        return self.__argumento1.upper()
        
    def set_argumento1(self,nuevo_valor):
        if len(nuevo_valor)>4:
            self.__argumento1=nuevo_valor
        else:
            print("El valor es demasiado chico... No vale !")
    
    argumento1 = property (get_argumento1, set_argumento1)


#################################################################
prueba=Prueba("HOLA")       # Inicialiar un objeto prueba, con un argumento
print(prueba.argumento1)    #Recuperar el valor de un argumento
prueba.argumento1="Adios"   # Modificar un argumento (atributo) de un objeto
print(prueba.argumento1)
print(prueba.__dict__)
