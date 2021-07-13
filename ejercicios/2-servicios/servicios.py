# Tipo de datos servicio
# Un servicio va a tener asociadas PRUEBAS, que es otro tipo de datos que voy a definir
    # servidor
# Prueba HTTP: 
    # protocolo , puertos, endpoint, timeout, codigos_estado, intervalo, numero_fallos_permitidos consecutivos

# De un servicio quiero poder pedir que se inicie la monitorizacion... o que se detenga
    # Estado en que se encuentra: 
    # OK            0
    # KO            1
    # DESCONOCIDO   2

# Un servicio puede tener varias pruebas asociadas

# De la libreria de enumeraciones (enum) quiero el tipo Enum para poder usarlo en este programa
from enum import Enum

class EstadoDeServicio(Enum):
     OK=0
     KO=1
     DESCONOCIDO=2

class Prueba: # DE UNA PRUEBA GENERICA QUE PUEDO HACER EN N SERVIDORES
    
    def __init__(self, nombre, protocolo , puertos, 
                        endpoint, timeout, codigos_estado_validos, intervalo, numero_fallos_permitidos_consecutivos ):
        self.nombre=nombre
        self.protocolo=protocolo
        self.puertos=puertos
        self.endpoint=endpoint
        self.timeout=timeout
        self.codigos_estado_validos=codigos_estado_validos
        self.intervalo=intervalo
        self.numero_fallos_permitidos_consecutivos=numero_fallos_permitidos_consecutivos
    
    def ejecutar(self, servidor):
        # Hacer un curl que devuelva el codigo http PARA CADA PUERTO
        print("Llamamos por curl al protocolo"+self.protocolo+" del servidor: "+servidor)
        return True

class Servicio:
    
    def __init__(self, nombre, servidor, pruebas):
        self.nombre=nombre
        self.servidor=servidor
        self.pruebas=pruebas
        self.estado=EstadoDeServicio.DESCONOCIDO
        
    def iniciar_monitorizacion(self):
        # Lanzar un hilo en paralelo que se encargue de ejecutar las pruebas
        #for prueba in pruebas:
        #    prueba.ejecutar(self.servidor) # Esta prueba debe ejecutarse cada prueba.intervalo
        pass
    
    def detener_monitorizacion(self):
        pass
        
prueba_web_segura = Prueba("Web", "https", (443,), "/", 5 , (200,), 5, 3)
servicio_google =  Servicio("Google", "google.es", (prueba_web_segura,) )
servicio_facebook =  Servicio("Facebook", "facebook.es", (prueba_web_segura,) )

print(servicio_google.estado)

servicio_google.iniciar_monitorizacion()
servicio_facebook.iniciar_monitorizacion()
# Dentro de 2 años
servicio_google.detener_monitorizacion()
servicio_facebook.detener_monitorizacion()