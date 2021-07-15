                   # Quiero la clase Prueba
from Prueba import Prueba
     # Del fichero Prueba.py
from subprocess import run, PIPE


class PruebaPing(Prueba):
        
    def __init__(self, nombre=None, timeout=0, intervalo=0, numero_fallos_permitidos_consecutivos=0 ):
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        
    def ejecutar(self, servidor):
        subproceso=run( ("ping","-c","1","-W",str(self.timeout),servidor) , stdout=PIPE, stderr=PIPE)
        return subproceso.returncode == 0
        
        #if subproceso.resturncode == 0:
        #    return True
        #else
        #    return False