texto=str("Hola AmigoS!")

#print( max(1,2,3) )

# Calculo el valor absoluto de un número
#print( abs(-3) )

# CONTROL DEL CASE
# Le pido a un texto que se ponga en mayusculas
print(texto.upper())         # Mayusculas
print(texto.lower())         # Minusculas
print(texto.capitalize())    # Primera letra en mayusculas y el resto en minúsculas
print(texto.title())         # Primera letra de cada palabra en mayúscula. El resto en minúscukas.
print(texto.swapcase())      # Invierte el case (mayusculas por minusculas)

# CONTROL DE BLANCOS
texto="   Hola Amigos    "
print(texto.strip())         # Se come los blancos por delante y detrás
print(texto.rstrip())        # Se come los blancos por detrás
print(texto.lstrip())        # Se come los blancos por delante 


texto="En un lugar de la mancha, de cuyo nombre no quiero acordarme..."
print(texto.split())         # Genera una tupla con los distintos vocablos del texto tras dividir por blancos
print(texto.split(','))      # Genera una tupla con los distintos vocablos del texto tras dividir por comas

print(texto.index(','))      # Posicion en la que aparece un determinado caracter

# Formatos / Composición de textos

# Regex
