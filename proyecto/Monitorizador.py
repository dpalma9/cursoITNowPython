

from threading import Thread
import time
from Servicio import EstadoDeServicio

class Monitorizador(Thread):
    
    __monitorizar_todos=True
    
    @classmethod
    def parar_todos_los_monitorizadores(cls):
        cls.__monitorizar_todos=False
        
    def __init__(self,servicio):
        super().__init__()
        self.servicio=servicio
        self.__monitorizar=True
        
        self.__numero_fallos_consecutivos={}
        self.__ultima_ejecucion={}
    
    def parar_de_monitorizar(self):
        self.__monitorizar=False
        
    def run(self):
        while Monitorizador.__monitorizar_todos and self.__monitorizar:
            ## CODIGO DE LA MONITORIZACION
            pruebas=self.servicio.pruebas_startup
            if self.servicio.estado==EstadoDeServicio.STARTED:
                pruebas=self.servicio.pruebas_lifeness
            elif self.servicio.estado==EstadoDeServicio.LIVE or self.servicio.estado==EstadoDeServicio.READY:
                pruebas=self.servicio.pruebas_readyness
            
            for prueba in pruebas:
                self.__ejecutar_prueba(prueba)
            
            time.sleep(1)
                

    def __ejecutar_prueba(self, prueba):
        # Mirar si debo ejecutar esta prueba ahora
        ejecutar=True
        ultima_ejecucion_de_la_prueba=self.__ultima_ejecucion.get(prueba.nombre)
        #print("Miro si necesito hacer la prueba "+ prueba.nombre)
        # Si he hecho una ejecución
        if (not ultima_ejecucion_de_la_prueba is None) and time.time()-ultima_ejecucion_de_la_prueba < prueba.intervalo:    # Y ademas, no hace más del intervalo establecido para la prueba
                ejecutar=False                                                  # No la ejecuto
        
        if ejecutar:
            #print("  Ejecutando prueba ")
            # Ejecutar la prueba
            resultado=prueba.ejecutar(self.servicio.servidor)
            # Anotar la ultima ejecucion
            self.__ultima_ejecucion[prueba.nombre]=time.time() # Me devuelve la hora del reloj del sistema
            # Si no ha fallado => inicializar los fallos a 0
            
            if resultado:
                #print("  Prueba correcta ")
                self.__numero_fallos_consecutivos[prueba.nombre]=0 # Me devuelve la hora del reloj del sistema
                if self.servicio.estado == EstadoDeServicio.KO or self.servicio.estado == EstadoDeServicio.UNKNOWN:
                    self.servicio.estado = EstadoDeServicio.STARTED
                elif self.servicio.estado == EstadoDeServicio.STARTED:
                    self.servicio.estado = EstadoDeServicio.LIVE
                elif self.servicio.estado == EstadoDeServicio.LIVE:
                    self.servicio.estado = EstadoDeServicio.READY
                #elif self.servicio.estado == EstadoDeServicio.READY:
                #    self.servicio.estado = EstadoDeServicio.READY
                
            # Si ha fallado => anotar un fallo
            else:                                                                                                    # Valor por defecto si no existe 
                #print("  Prueba incorrecta ")
                self.__numero_fallos_consecutivos[prueba.nombre]=self.__numero_fallos_consecutivos.get(prueba.nombre,0)+1
                if self.__numero_fallos_consecutivos[prueba.nombre] >= prueba.numero_fallos_permitidos_consecutivos:
                    self.servicio.estado=EstadoDeServicio.KO
                
        #print("    Estado del servicio: "+str(self.servicio.estado))
