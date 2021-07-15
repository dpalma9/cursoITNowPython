from SistemaMonitorizacion import SistemaMonitorizacion
from Servicio import Servicio
from PruebaPing import PruebaPing
from Servicio import EstadoDeServicio


def imprimir_servicios(servicios):
    for nombre,service in servicios.items():
            service.imprimir_estado_servicio()
# 1º Crear un sistema de Monitorizacion
sistema_de_monitorizacion=SistemaMonitorizacion()


## NO QUIERO HACER ESTO:
#################################################################################################
# 2º Definir una serie de servicios con sus correspondientes pruebas
#pruebas_startup=( PruebaPing("Ping Startup", 5, 5, 3) ,)
#pruebas_lifeness=( PruebaPing("Ping Lifeness", 5, 2, 3) ,)
#pruebas_readyness=( PruebaPing("Ping Readyness", 5, 1, 3) ,)

#servicio_de_google=Servicio("Google", "google.es", pruebas_startup, pruebas_lifeness, pruebas_readyness, True)
#servicio_de_google_malo=Servicio("GoogleMalo", "googlemalo.es", pruebas_startup, pruebas_lifeness, pruebas_readyness, True)

#sistema_de_monitorizacion.alta_servicio(servicio_de_google)
#sistema_de_monitorizacion.alta_servicio(servicio_de_google_malo)
#################################################################################################
sistema_de_monitorizacion.cargar_servicios("servicios.yaml");


# 3º Iniciar la monitorizacion
sistema_de_monitorizacion.monitorizar()
# 4º Desactivar la monitorizacion para un servicio
# 5º Alta de un nuevo servicio
# 6º Baja de un servicio

# Esto se ejecuta en el hilo MAIN
print("Monitorizando... ")
while True:    
    comando=input("> ") # Hace un sleep del hilo MAIN hasta que se pulsa ENTER en la consola

    if comando == "quit":
        print("Deteniendo el sistema de monitorización... y saliendo")
        sistema_de_monitorizacion.parar_de_monitorizar()
        break   
    
    elif comando == "stop":
        print("Deteniendo la monitorización...")
        sistema_de_monitorizacion.parar_de_monitorizar()
    
    elif comando == "start":
        print("Iniciando la monitorización...")
        sistema_de_monitorizacion.monitorizar()
    
    elif comando == "status":
        print(sistema_de_monitorizacion.status())
        
    elif comando == "service status":
        imprimir_servicios(sistema_de_monitorizacion.servicios)

    elif comando == "ko services":
        imprimir_servicios(dict(filter( lambda servicio: servicio[1].estado == EstadoDeServicio.KO or  servicio[1].estado == EstadoDeServicio.UNKNOWN
                            , sistema_de_monitorizacion.servicios.items())))

    else:
        print("Comando no reconocido.")

print("Sistema de monitorización detenido. Gracias por usar nuestro sistema de MonitorizacionACME.")
