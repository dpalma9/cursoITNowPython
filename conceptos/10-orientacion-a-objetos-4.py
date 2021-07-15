class Servicio:
    
    def __init__(self,nombre,servidor):
        self.nombre=nombre
        self.servidor=servidor
        
    def __str__(self):
        return "Soy el servicio: "+self.nombre +", disponible en el servidor: "+self.servidor    
        
        
un_servicio=Servicio("Google","google.es")

print(un_servicio)