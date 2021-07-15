from enum import Enum

class EstadoDeServicio(Enum):
     UNKNOWN=0
     STARTED=1
     LIVE=2
     READY=3
     KO=4


class Servicio:
    
    def __init__(self, nombre=None, servidor=None, pruebas_startup=[], pruebas_lifeness=[], pruebas_readyness=[], monitorizar=True, estado=EstadoDeServicio.UNKNOWN):
        self.nombre=nombre
        self.servidor=servidor
        self.pruebas_startup=pruebas_startup
        self.pruebas_lifeness=pruebas_lifeness
        self.pruebas_readyness=pruebas_readyness
        self.estado=estado
        self.monitorizar=monitorizar
        
    def imprimir_estado_servicio(self):
        print(self.nombre+"   "+str(self.estado))