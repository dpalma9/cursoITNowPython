# Funcion que dados 2 numeros devuelva el maximo de ellos
def maximo(a,b):
    #if a>b:
    #    return a
    #else:
    #    return b

    #if a>b:        # En este escenario no seria recomendable
    #    return a
    #return b
    
    return a if a>b else b
    # VALOR A DEVOLVER SI TRU if CONDICION else VALOR A DEVOLVER SI FALSE
    

def maximoDeTres(a,b,c):
    #if a>b:
    #    if a>c:
    #        return a
    #    else:
    #        return c
    #else:
    #    if b>c:
    #        return b
    #    else:
    #        return c
    return maximo(maximo(a,b),c)


def identificarMaximo(numero1,numero2):
        # Quiero que esta funcion devuelva: El maximo, pero tambien cual de los 1 es el maximo: (1,2,0)
    if numero1>numero2:
        return (1,numero1)
    elif numero1<numero2:
        return (2,numero2)
    else:
        return (0,numero1)

print(maximo(7,9))    
print(maximo(9,9))

print(maximoDeTres(9,81,18))

quien,maximo=identificarMaximo(25,25)

print("El mayor es el numero: "+ str(   quien    ))
print("Su valor es: "+ str(   maximo   ))