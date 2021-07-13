# Orientación a objetos: Es un paradigma de programación

Lo que hacemos es definir nuestros propios TIPOS de variables avanzados.

Tipos sencillos:
Numeros: Integer, Float, Boolean

Tipos avanzados:
    Clase: TIPO de variable que puedo usar y definirme los mios
        Strings
        
        Colecciones: 
            Tupla, Lista, Diccionario
            
    Características:
        1º Pueden albergar varios valores, no uno solo
        2º Pueden definir sus propias FUNCIONES
        
----
Montar un sistema de monitorizacion para servicios web.
Que información necesito del servicio:
    ----------------------------------------- V DATOS
    - URL
    - Nombre
    - Cuando falla? Cuando no devuelve un determinado codigo o codigos
        Si no lo devuelve ya lo considero en estado FALLIDO? Quizas deberiamos probar N veces... 
        Si las N veces falla, marco el servicio como FALLIDO
    - Timeout
    - Intervalo
    ----------------------------------------- V FUNCION
    - A Monitorizar
    - Para la monitorización
    
    
---------------------------------------------------------------------------------------------------------

Servicios
    
    Momento en el que la prueba debe realizarse / Que estoy probando conceptualmente
        Si el sistema esta vivo o no
        El que un sistema esté vivo... implica que sea utilizable?
            BBDD <<<< Backup
                Esta viva?                         SI
                Esta todo correcto con ella?       SI
                Es utilizable por los usuarios?    
        
        Arrancando un WEBLOGIC <<<< 5 minutos       ... Debo de marcar el WEBLOGIC como invalido?
        
        1º Saber si un servicio ha arrancado correctamente              <<< PRUEBAS
                                                                Configuración de tiempos
            StartupProbe
                TCP
                HTTP 
        2º Saber si un servicio está en funcionamiento                  <<< PRUEBAS
                                                                Configuración de tiempos
            LifenessProbe
                HTTP 
                TCP
        3º Saber si un servicio está listo para atender peticiones      <<< PRUEBAS
                                                                Configuración de tiempos
            ReadynessProbe
                HTTP 
                TCP
        
        Que sistema lleva este tipo de monitorización: Kubernetes / Openshift 
        
        Un servicio tiene 3 estados:
            Started OK,KO
            Live    OK,KO
            Ready   OK,KO
            
            Started > Live <> Ready
              ^^            V
            UNKNOWN      > KO
    
    Pruebas
        Distinto tipo (Naturaleza de la prueba: http, tcp, ping, ....)
        Intervalo
        Numero de fallos Consecutivos permitidos
        Timeout
    
    


