
# Quiero un tipo nuevo llamado Contador
# Un contador debe tener asociado un nombre
# También, hasta cuando contar, y cuanto tiempo espera entre numero y numero
# Quiero que esta clase tenga un metodo contar <<< Aqui empieza a contar
                                                                            # Quiero tener un metodo que sea detener Cuenta
import time
from threading import Thread

class Contador(Thread):
    
    forzar_parada_de_todos_los_contadores=False # Variable de clase
   
    @classmethod
    def parar_todos_los_contadores(cls):
        print("Paro todos los contadores ")
        cls.forzar_parada_de_todos_los_contadores=True
   
   
    # Todo esto a partir de aqui va asociado a las instancias (los objetos de este tipo que se crearán)
    def __init__(self,nombre,limite,espera):
        super().__init__()
        self.nombre=nombre
        self.limite=limite
        self.espera=espera
        self.tengo_que_parar=False

    def contar(self):
        self.start() # en Automatico start llama a la funcion RUN pero desde otro hilo
    # start  <<< Iniciar una ejecución en paralelo dentro de este proceso.
                 # Se ejecutará en paralelo, el código que se encuentre dentro de la función run()
    def parar_de_contar(self):
        print("Paro el contador "+self.nombre)
        self.tengo_que_parar=True

        #self.terminate()   # Crujir el hilo.... pero bien crujido

    def run(self):
        #for numero in range(1,self.limite+1):
        #    print("Soy el contador: "+self.nombre+".            Voy por el "+str(numero))
        #    time.sleep(self.espera)
        #    if self.tengo_que_parar:
        #        return
        numero=1
        while numero<=self.limite and not self.tengo_que_parar and not Contador.forzar_parada_de_todos_los_contadores:
            print("Soy el contador: "+self.nombre+".            Voy por el "+str(numero))
            numero+=1
            time.sleep(self.espera)
        
    
    
mi_contador=Contador("Contador A", 10, 2)
otro_contador=Contador("Contador B", 20, 1)
otro_contador_mas=Contador("Contador C", 7, 3)
Contador("Contador D", 6, 4).contar()

mi_contador.contar()
otro_contador.contar()
otro_contador_mas.contar()
# Este codigo de abajo lo ejecuta otro hilo... el hilo MAIN
print("Me ejecuto en paralelo con los contadores")
time.sleep(10)
otro_contador.parar_de_contar()
time.sleep(5)
# quiero que TODOS los contadores que esten vivos dejen de contar 
Contador.parar_todos_los_contadores()

mi_contador.join()
otro_contador.join()
otro_contador_mas.join()
print("Me ejecuto cuando acaben  los contadores")


# 1º Quiero que a los 10 segundos de iniciar la cuenta, se detenga el contador B
# 1º Quiero que a los 15 segundos de iniciar la cuenta, se detengan todos los contadores

# Qué es un hilo?
# Podriamos entenderlo como un proceso ligero

# Un proceso es una copia INDEPENDEIENTE de un programa que se está ejecutando
# Dentro de un proceso nosotros tenemos HILOS, que son los que de forma efectiva ejecutan el CODIGO DEL PROGRAMA

#      __________contador_______________
#     /                                  \
#----------------main---------------------O--
#                                         ^Punto de sincronizacion