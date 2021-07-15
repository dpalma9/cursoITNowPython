
def mifuncion(argumento1):
    print("Estoy dentro de la función 1: "+argumento1)
    

mifuncion("HOLA !")

mivariable=mifuncion # Esta es la gracia de la programacion funcional
print(mivariable)

mivariable("ADIOS")


def saluda(nombre):
    return "Hola "+nombre
    
def despedida(nombre):
    return "Adios "+nombre
    
def imprime(funcion,nombre):
    print(funcion(nombre))
    
imprime(saluda,"Ivan")
imprime(despedida,"Gerard")

# Expresiones lambda: Funcion anonima
def doblar(numero):
    return numero*2
    

def imprimir(funcion,numero):
    print(funcion(numero))
    
imprimir(doblar,4)

imprimir( lambda numero: numero*3 ,4)

###############################

from threading import Thread

#class MIHILO(Thread):
#    __init__()
#    run()
    
    
def mifuncionRun():
    for i in range(1,5):
        print("Me ejecuta el hilo. Voy por el "+str(i))

hilo=Thread(target=mifuncionRun)
hilo.start()
print("Yo me sigo ejecutando desde el hilo MAIN")
hilo.join()
print("y sigo ejecutandome en el MAIN")