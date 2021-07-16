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
import re

#if re.match("regex","texto"):

if re.match(".*error","la busqueda ha provocado un error."):
    print("PUES SI 1")
if re.match("^.*error","la busqueda ha provocado un error."):
    print("PUES SI 2")
if re.match("^error","error."):
    print("PUES SI 3")
if re.match("^error$","error."):
    print("PUES SI 4")
if re.match("^error$","error"):
    print("PUES SI 5")
if re.match(".*error$","tengo error"):
    print("PUES SI 6")


texto="HOLA AMIGO 1276"
PATRON="[0-9]+"
resultado=re.search(PATRON,texto)
print(resultado.string)
print(resultado.group())
print(resultado.span())

texto="HOLA AMIGO 1276 IVAN"
PATRON="[A-Z]+"
resultado=re.findall(PATRON,texto)
for texto in resultado:
    print(texto)

texto="HOLA AMIGO COMO ESTAS"    
PATRON="[AEIOU]"
resultado=re.sub(PATRON,"O",texto)
print(resultado)



texto="+34 91  876-56/ 87"    
PATRON="[+ -/]+"
resultado=re.split(PATRON,texto)
for item in resultado:
    print(item)
