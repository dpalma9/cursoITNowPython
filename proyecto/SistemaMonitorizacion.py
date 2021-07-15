from Monitorizador import Monitorizador
from threading import Thread
import time
import yaml
##########
from PruebaPing import PruebaPing
from Servicio import Servicio
from Servicio import EstadoDeServicio

class SistemaMonitorizacion:
    
    INTERVALO_COMPROBACION_SERVICIOS_A_MONITORIZAR = 2
    
    def __init__(self):
        self.servicios={}    #< Estado de los servicios
        self.__monitorizadores={}    
        self.__monitorizar=True
        self.__hilo_de_control=None
    
    def cargar_servicios(self, fichero):
        with open (fichero,"r") as fichero_yaml:
            contenido_del_fichero=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
        
        for definicion_servicio in contenido_del_fichero:

            for tipo_prueba, pruebas in definicion_servicio.pop("pruebas").items():
                lista_de_pruebas=[]
                for definicion_prueba in pruebas:
                    prueba=self.crear_prueba_desde_diccionario(definicion_prueba)
                    lista_de_pruebas.append(prueba)
                definicion_servicio["pruebas_"+tipo_prueba]=lista_de_pruebas
            
            servicio=Servicio()
            definicion_servicio["estado"]=EstadoDeServicio.UNKNOWN
            servicio.__dict__=definicion_servicio
            
            self.alta_servicio(servicio)
            
    
    def crear_prueba_desde_diccionario(self,diccionario):
        # Control sobre lo que vienen en diccionario.get("tipo")
        prueba=eval(diccionario.pop("tipo")+"()")      ######################## Generamos un objeto dinamicamente en funcion del contenido de una variable
        prueba.__dict__=diccionario
        return prueba
    
    def alta_servicio(self, servicio):
        self.servicios[servicio.nombre]=servicio
        #########################################################################################################
        #  nombre   #   SERVICIO                                                                                #
        #########################################################################################################
        #  google   #   Objeto de tipo Servicio, con TODOS los datos del servicio de GOOGLE, pruebas incluidas  #
        #########################################################################################################
        
    def baja_servicio(self, servicio):
        del self.servicios[servicio.nombre]
        #self.servicios.pop(servicio.nombre)
    
    def status(self):
        return self.__monitorizar

    def monitorizar(self):
        self.__monitorizar=True
        self.__hilo_de_control=Thread(target=self.crear_monitorizadores )
        self.__hilo_de_control.start()
    
    def crear_monitorizadores(self):
        # Crear Monitorizadores para cada Servicio con monitorizacion Activada
        # Meter un hilo que segun se activen / desactiven monitorizaciones sobre servicios, cree o borre Monitorizadores
        while self.__monitorizar:
            for nombre, servicio in self.servicios.items():
                
                # Si el servicio debe monitorizarse y no tengo AUN un monitorizador => lo creo
                if self.__monitorizadores.get(nombre) is None and servicio.monitorizar:
                    monitorizador=Monitorizador(servicio)
                    self.__monitorizadores[nombre]=monitorizador
                    monitorizador.start()
                # Si existe el monitorizador pero el servicio no debe monitorizarse, borro el monitorizador
                elif not servicio.monitorizar:
                    #self.__monitorizadores.get(nombre).parar_de_monitorizar()
                    #del self.__monitorizadores[nombre]
                    self.__borrar_monitorizador(nombre)
                        
            for nombre in self.__monitorizadores:
                if self.servicios.get(nombre) is None:
                    self.__borrar_monitorizador(nombre)
                    

            time.sleep(SistemaMonitorizacion.INTERVALO_COMPROBACION_SERVICIOS_A_MONITORIZAR)

    def __borrar_monitorizador(self, nombre_a_borrar):
        self.__monitorizadores.pop(nombre_a_borrar).parar_de_monitorizar()
    
    def parar_de_monitorizar(self):
        self.__monitorizar=False
        # Parar todas las monitorizaciones que se esten ejecutando
        Monitorizador.parar_todos_los_monitorizadores()
        self.__monitorizadores.clear()
        self.__hilo_de_control=None
