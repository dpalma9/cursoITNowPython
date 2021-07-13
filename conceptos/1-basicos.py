# Comentarios
# Todo lo que tengamos detrás de este simbolo se ignora por el interprete

# En python no existe el comentario en bloque
# En python hay una chapuzilla que hacemos que es usar el operador triple comilla
"""
Lo que pongo aqui se ignora
Y lo que pongo aqui también
"""

# Es importante escribir comentarios en el código, cuando haya que escribirlos... no a lo loco
# Para que sirve un comentario
# Comentar vs Documentar
# Documentar : Explicar QUE HACE UN PROGRAMA
# Comentar   : Explicar COMO HACE UN PROGRAMA LO QUE HACE
# En general el código debe ser AUTOEXPLICATIVO

###########################################################################################
# Tipos de datos
###########################################################################################

# TIPOS SIMPLES

# Numeros enteros
17
23
-76
# Numeros decimales
-34.87
# Valores logicos
True
False
# Textos
"Hola"
'Amigo'
""" Como estas?
Yo estoy bien !!!!"""

# COLECCIONES DE DATOS

# Tupla: Secuencia ordenadas e inalterables de datos: ARRAY  <<< CONSTANTE
(1,2,3,4)
(1, True, "Hola")

# Listas: Secuencia ordenada y modificables de datos: ARRAY
[1,2,3,4]
[1, True, "Hola"]

# Diccionario (mapa): Coleccion no ordenada de datos y modificables, accesibles a través de un identificador
{ "Nombre": "Ivan", "Edad": 42 }
# Datos: Ivan y 42
# Identificadores: Nombre , Edad

# VARIABLES
VARIABLE_NUMERICA  = 17          # Esto no seria un nombre adecuado en python para una variable
texto              = "Hola"
mi_variable_logica = True

# En python las variables se escriben en snake-case: Minusculas y cada palabra va separada de la siguiente por un guion bajo.

# OPERADORES
# Operadores aritmeticos:
2+3-4/4*7
7//4         # Division entera -> 1
7%4          # Resto de la division entera -> 3
# Operadores relacionales
3>2 # > < >= <=  == !=
3==4 # > FALSE
# Operadores lógicos
True and False  # False
True or  False  # True
not False       # True 
# Operadores sobre textos
"Hola" + """ """ + 'Amigo' # "Hola amigo"
"HOLA" * 3                 # HOLAHOLAHOLA

# Funciones básicas integradas en python
print( "HOLA " )    # Imprimir un texto por consola
edad = input("Dame tu edad: ")       # Lee algo de la consola
print( edad )
edad = 42
print("Tu edad es: " + str(edad) ) 

# Funciones de conversión de tipos de datos

str(32)  # -> "32"
int("32")
float("32.23")
bool("TRUE")

# Programación imperativa

## Expresiones de control de flujo

### Condicionales
# if CONDICION :
# Dentro del if irá el codigo que debe ejecutarse si se cumple la condición
# La condición tiene que ser un valor LOGICO
edad=12
if edad > 115:
    print("Eres un superviviente !!!!!") # Al estar este código sangrado hacia la derecha (MAS QUE EL IF) 
    print("Que guay !!!!, pero ya deberias conducir")
elif edad > 18:
    print("Eres mayor de edad") # Al estar este código sangrado hacia la derecha (MAS QUE EL IF) 
    print("Que guay !!!!, ya puedes conducir")
else:
    print("Eres un pitufin")
print("Adios!") # Este se ejecuta siempre


### BUCLES

#while CONDICION:
    # CODIGO se ejecuta MIENTRAS se cumple la condición

numero=10
while numero > 0:
    print(numero)
    numero = numero - 1
    numero -= 1 # -= += /= *=

# Bucle que permite ejecutar un determinado codigo 
#   PARA CADA UNO DE LOS VALORES QUE TENGA EN UNA COLECCION
lista=("a","b","c")
for valor in lista:
    print("  >  "+ str(valor))
    
    
# Quiero un bucle que itere sobre los numeros del 1 al 100    
lista=range(1,100)
for numero in lista:
     print(numero)
     
    
for numero in range(10,1,-2):
     print(numero)



# Programacion procedural

## Definir una FUNCION o PROCEDIMIENTO
def saluda (nombre="amigo", efusividad=False):
    if not efusividad:
        return "HOLA "+nombre
    else:
        return "HOLA "+nombre+" !!!!!!!!"
    
saluda("Ivan")
saluda("Jero", True)
saluda("Leo", True)
saluda("Miguel", True)
saluda()
saluda(efusividad=True)
saluda(efusividad=True, nombre="Cristian")

saludo = saluda(efusividad=True, nombre="Gau")
print(saludo)


