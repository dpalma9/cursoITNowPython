class SistemaMonitorizacion:
    
    def __init__(self)
        self.servicios={}    #< Estado de los servicios
        self.monitorizadores={}    
            
            
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
        

    def monitorizar(self):
        # Crear Monitorizadores para cada Servicio con monitorizacion Activada
        # Meter un hilo que segun se activen / desactiven monitorizaciones sobre servicios, cree o borre Monitorizadores
        
    def parar_de_monitorizar(self):
        # Parar todas las monitorizaciones que se esten ejecutando
        