lista=[1,2,3,4,5,6,7,8,9]

pares= [item for item in lista if item % 2 == 0]
print(pares)

diccionario={"clave1":"valor1", "clave2":"valor2", "clave3":"valor3"}

lista2=[valor for clave, valor in diccionario.items() if clave == "clave1" or clave == "clave2"]
print(lista2)

otro_diccionario={clave:valor for clave, valor in diccionario.items() if clave == "clave1" or clave == "clave2"}
print(otro_diccionario)

#otra_lista=filter(funcion_de_filtro,coleccion)
otra_lista=list(filter(lambda numero: numero % 2 == 1,lista))
print(otra_lista)

#otra_coleccion=map(funcion,coleccion)
# De forma que en la nueva coleccion estarán los resultados de aplicar 
# la funcion de mapeo sobre los elementos originales

otra_lista=list(map(lambda numero: numero*2,lista))
print(otra_lista)
