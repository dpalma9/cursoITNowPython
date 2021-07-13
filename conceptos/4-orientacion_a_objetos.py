# Orientación a objetos: Es un paradigma de programación
# Lo que hacemos es definir nuestros propios TIPOS de variables avanzados

# Variables
#url="http://google.es"
#nombre="Google"
#numero_fallos_consecutivos_permitidos=3
#timeout=5
#intervalo=10

# Funciones
#def monitorizar():
    #estado=...
#    return estado

#def parar_monitorizacion():
    # Se parará
    
    
# Me voy a definir mi propio tipo de datos: SERVICIO
class Servicio:
    
    # Constructor
    def __init__(self, la_url, nombre, numero_fallos_consecutivos_permitidos, timeout, intervalo):
        # Atributos
        self.url=la_url
        self.nombre=nombre
        self.numero_fallos_consecutivos_permitidos=numero_fallos_consecutivos_permitidos
        self.timeout=timeout
        self.intervalo=intervalo
    
    def monitorizar(self):
        print("Comienzo la monitorizacion " + self.nombre)

    def parar_monitorizacion(self):
        print("Detengo la monitorizacion " + self.nombre)

# Objetos
servicio_google=Servicio("http://google.es","Google",3,5,10)
servicio_facebook=Servicio("http://facebook.com","Facebook",3,5,10)
servicio_instagram=Servicio("http://instagram.com","Instagram",3,5,10)

# Recuperación de los atributos de un objeto
print(  servicio_google.url  )
print(  servicio_facebook.nombre  )
print(  servicio_instagram.numero_fallos_consecutivos_permitidos  )

# Llamar a las funciones de un objeto
servicio_google.monitorizar()
servicio_facebook.parar_monitorizacion()
