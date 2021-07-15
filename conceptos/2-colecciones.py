tupla=(1,3,5,7,9,7,5,3,1)
texto="murcielago" # Es una tupla de caracteres

print("Numero de cosas en la tupla: " + str (    len(tupla)  ) )

print("Elemento primero: " + str (          tupla[0]                    ) )
print("Elemento tercero: " + str (          tupla[2]                    ) )

print("Elemento último: " + str (           tupla[len(tupla)-1]         ) )
print("Elemento último: " + str (           tupla[-1]                   ) )
print("Elemento penúltimo: " + str (        tupla[-2]                   ) )


print("Los elementos 2, 3 y 4: " + str (    tupla[1:4]                  ) )
                                                    # De la posicion 1 a la 4 no incluida

print("Los 2 primeros valores: " + str (    tupla[:2]                   ) )
print("Los 3 ultimos valores: " + str (     tupla[-3:]                  ) )

print( tupla * 3 ) 



lista=[]
lista=[1,2,3,4,5,6]
lista[1]=10
print(lista[-1])
print(lista[2:4])

#lista=list(tupla) # Convierte la tupla en una lista
#tupla=tuple(lista) # Convierte la tupla en una lista

lista = list(  (1,2,3) )
print(lista)
lista.append( 4 )
lista +=   [ 5,6,7,8,9,10 ]

print(lista)

#texto[1]="U"

for caracter in texto:
    print(caracter)


lista=["LISTA CON UN ELEMENTO"]
print(lista)

#### OJO !!!!! En python los parentesis sirven para muchas cosas:
# Definir tuplas
# Pedir la ejecución de una función
# Sirven para establecer prioridades a la hora de ejecutar un codigo
print(  (3 + 2) * 5 )


tupla=("TUPLA CON UN ELEMENTO", )
print(len(tupla))

texto=("TUPLA CON UN ELEMENTO")
print(texto)

tupla=(12,20,67,87,90,87)
#partidas_ganadas=tupla[0]
#partidas_jugadas=tupla[-1]

# Desestructuración )
(partidas_ganadas,_,partidas_jugadas,*otros)=tupla

print(partidas_ganadas)
print(partidas_jugadas)


diccionario={} # He definido un diccionario vacio

diccionario={"numero": 5, "texto": "Hola", "logico": True}

print (diccionario["numero"])
diccionario["texto"]="Adios"
print (diccionario["texto"])
print ( len(diccionario))


diccionario["fecha"]="10-10-2020"
print (diccionario.get("fecha"))  # Aqui no se genera error

print (diccionario.get("indefinido"))  # Aqui no se genera error. Devuelve None
#print (diccionario["indefinido"])      # Genera un error en tiempo de ejecución


for clave in diccionario:
    print("----"+clave)
    print(diccionario.get(clave))
    print(diccionario[clave])

for clave,valor in diccionario.items():
    print("++++"+clave)
    print(valor)

print(diccionario)
print(diccionario.items())