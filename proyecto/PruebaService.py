                   # Quiero la clase Prueba
from Prueba import Prueba
     # Del fichero Prueba.py
from subprocess import run, PIPE
from jinja2 import Template
from fabric import Connection
import os
import stat
import threading

class PruebaService(Prueba):
        
    numero=0
    semaforo=threading.Lock()
    
    def __init__(self, nombre=None, timeout=0, intervalo=0, numero_fallos_permitidos_consecutivos=0, servicios=() ):
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        self.servicios=servicios

        with open("services.jinja") as archivo_plantilla:
            texto_de_la_plantilla=archivo_plantilla.read()
        self.plantilla=Template( texto_de_la_plantilla )
        
    def ejecutar(self, servidor):
        
        codigo=self.plantilla.render( self.__dict__ )

        os.environ['use_ssh_config']="True"
        os.environ['key_filename']="~/.ssh/id_rsa"
        remoto=Connection(host= self.usuario+"@"+servidor)
        # Vamos a guardar la plantilla en un fichero temporal.. que vamos a copiar dentro del remoto
        try:
            # El resultado de la plantilla lo guardamos en un fichero temporal
            # SEMAFORO     
            with PruebaService.semaforo:
                PruebaService.numero+=1
                nombre_archivo="script"+str(PruebaService.numero)+".sh"
            
            ruta="./"+nombre_archivo
            with open(ruta,"w") as script:
                script.write(codigo)
            # Le pongo permisos de ejecucion
            permisos_originales=os.stat(ruta).st_mode
            os.chmod(ruta, permisos_originales | stat.S_IXUSR )
            # Ese fichero le copiamos al remoto
            remoto.put(ruta, remote="/tmp")
            os.remove(ruta)
            # Y lo ejecutamos alli
            respuesta=remoto.run( "/tmp/"+nombre_archivo )
            respuesta=remoto.run( "rm /tmp/"+nombre_archivo )
        except:
            return False
        #print("Resultado de la prueba "+str(respuesta.return_code))
        return respuesta.return_code == 0
        
        #if subproceso.resturncode == 0:
        #    return True
        #else
        #    return False