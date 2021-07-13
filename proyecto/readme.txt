ENUM: Estados posibles de Servicios

Clase: Prueba
    Subclases: Prueba HTTP
                    Protocolo
                    Puerto
                    Endpoint
                    Codigos de Respuesta HTTP admisibles
               Prueba Ping
               ...
    Nombre
    Intervalo
    Numero de fallos consecutivos admitidos
    Timeout
    <<< Codigo del programa que ejecuta la prueba en PYTHON

Clase: Servicio
    Nombre
    Estado
    Servidor
    ActivarMonitorizacion:: Boolean
    Pruebas:
        Startup   < lista (Pruebas)
        Lifeness  < lista (Pruebas)
        Readyness < lista (Pruebas)

    
Clase: Monitorizador... Tendre 1 monitorizacion por cada Servicio copn monitorizacion activada
    Ejecutar las pruebas... cuales? Dependiendo del estado del servicio
    Esas pruebas... como las ejecutamos? En serie o en paralelo?
        En paralelo.... y que vamos a necesitar aqui entonces? Threads >>> Cambiar el estado del Servicio
    = Contador    
    Servicio a monitorizar
    

Clase: SistemaMonitorizacion
            < Alta de Servicios
            < Baja de servicios
            < Estado de los servicios
            < Monitoriza
                Para cada servicio con monitorizacion activada
                    Iniciar una monitorizador
                
            < Para de monitorizar