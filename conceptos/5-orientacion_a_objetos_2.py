      
class Prueba:
        
    def __init__(self, nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos ):
        self.nombre=nombre
        self.timeout=timeout
        self.intervalo=intervalo
        self.numero_fallos_permitidos_consecutivos=numero_fallos_permitidos_consecutivos

    def ejecutar(self, servidor):
        pass
    

class PruebaHttp(Prueba): # La clase PruebaHttp extiende a la clase Prueba, 
                          #  y por tanto hereda todas sus caracteristicas
        
    def __init__(self, nombre, protocolo , puertos, 
                        endpoint, timeout, codigos_estado_validos, intervalo, numero_fallos_permitidos_consecutivos ):
        # Inicializo la PruebaHttp como Prueba que es
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        # Inicializo especifica de PruebaHttp
        self.protocolo=protocolo
        self.puertos=puertos
        self.endpoint=endpoint
        self.codigos_estado_validos=codigos_estado_validos

    def ejecutar(self, servidor):
        print("Hago un curl")
        
class PruebaPing(Prueba):
        
    def __init__(self, nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos ):
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        
    def ejecutar(self, servidor):
        print("Hago un ping")

prueba_web_segura = PruebaHttp("Web", "https", (443,), "/", 5 , (200,), 5, 3)
print( prueba_web_segura.nombre )
print( prueba_web_segura.puertos )
prueba_web_segura.ejecutar("servidor1")

prueba_conectividad = PruebaPing("Ping", 5 , 5, 3)
print( prueba_conectividad.nombre )
prueba_conectividad.ejecutar("servidor1")
