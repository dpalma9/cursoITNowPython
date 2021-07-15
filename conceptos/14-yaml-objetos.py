import yaml

class MiClaseBase:
    def __init__(self):
        self.atributo_base=True

class MiClase(MiClaseBase):
    
    @classmethod
    def init(cls,argumento1,argumento2):
        aux=MiClase()
        aux.argumento1=argumento1
        aux.argumento2=argumento2
        return aux
    
    @classmethod
    def load_from_file(cls,fichero):
        with open (fichero, "r") as fichero_variable1:
            diccionario=yaml.load(fichero_variable1, Loader=yaml.FullLoader)
        return MiClase.load_from_dict(diccionario)
    
    @classmethod
    def load_from_dict(cls,diccionario):
        aux=MiClase()
        aux.__dict__=diccionario
        return aux
    
    def __init__(self):
        super().__init__()
        self.argumento1=None
        self.argumento2=None
        
    def __str__(self):
        return "Soy un objeto de tipo MICLASE: "+self.argumento1+" "+self.argumento2
        
    def dump_to_file(self,fichero):
        with open (fichero, "w") as fichero:
            yaml.dump(self.__dict__, fichero)    


########################################

un_objeto=MiClase.init("Hola","Amigo")
un_objeto.dump_to_file("fichero.yaml")

objeto_leido=MiClase.load_from_file("fichero.yaml")
print(objeto_leido)