def factorialFor(numero_inicial):
    resultado = 1
    for numero in range(numero_inicial,1,-1):
        resultado *= numero
    return resultado
    
def factorialWhile(numero):

# 6! = 6 x 5 x 4 x 3 x 2 x 1
    resultado = 1
    while numero > 1:
        #resultado = resultado * numero
        resultado *= numero
        numero -= 1
    return resultado


# 6! = 6 x 5!
# 5! = 5 x 4!
# 0! = 1
def factorialRecursividad(numero):
    resultado=1
    if numero != 0:
        resultado= numero * factorialRecursividad (numero - 1)   # RECURSIVIDAD
    return resultado
        
print(factorialWhile(6))
print(factorialFor(6))
print(factorialRecursividad(6))

