#open(RUTA ARCHIVO, MODO DE APERTURA)
import os

# REESCRIBIR TODO EL CONTENIDO DE UN FICHERO
apuntador_al_archivo = open("ejemplo.txt", "w")
apuntador_al_archivo.writelines( ("Esta es una linea1\n","Esta es una segunda linea\n") )
apuntador_al_archivo.write("Escribo más cosas en el fichero\n")
apuntador_al_archivo.close()

#input("PULSAR ENTER PARA AÑADIR MAS LINEAS")
# AÑADIR COSAS A UN FICHERO
with open("ejemplo.txt", "a") as apuntador_al_archivo:
    apuntador_al_archivo.writelines( ("Esta es una linea1\n","Esta es una segunda linea\n") )
    apuntador_al_archivo.write("Escribo más cosas en el fichero\n")

#input("PULSAR ENTER PARA LEER EL FICHERO")

with open("ejemplo.txt", "r") as apuntador_al_archivo:
    while True:
        linea=apuntador_al_archivo.readline()
        if len(linea) == 0: 
            break
        #linea=linea[:-1] # Esto me podría fallar en la última linea. 
                         # ME eliminaria el ultimo caracter que no tiene por que ser un salto de linea
        linea=linea.rstrip()
        print(">>>"+linea)
        

with open("ejemplo.txt", "r") as apuntador_al_archivo:
    for linea in apuntador_al_archivo:
        print("<<<"+linea)

#####################################



try: # IMPREVISTOS
    if os.path.exists("./ejemplo.txt"):
        with open("ejemplo.txt", "r") as apuntador_al_archivo:
            for linea in apuntador_al_archivo:
                print("+++"+linea)
        #print("Codigo que se ejecuta si todo ha ido bien")
    else: 
        print("El archivo no existe... hago lo que necesite en lugar de leerlo")
except FileNotFoundError:
    print("Se ha producido un problema al leer el archivo: EL ARCHIVO NO EXISTE")
except PermissionError:
    print("Se ha producido un problema al leer el archivo: PROBLEMA DE PERMISOS")
except:
    print("Se ha producido un problema al leer el archivo: OTRO TIPO DE PROBLEMAS")
else:
    print("Codigo que se ejecuta si todo ha ido bien")
finally:
    print("Codigo que se ejecuta siempre... si ha ido bien como si ha ido mal")
    
print("Sigue mi codigo ejecutandose")

################################

os.mkdir("./ejemplos")
input("Directorio creado. Pulse ENTER para borrarlo")
os.rmdir("./ejemplos")
os.remove("./fichero.txt")

print(os.path.exists("./ejemplos/ejemplo.txt"))

#################################

import stat
permisos_originales=os.stat("./ejemplo.txt").st_mode
os.chmod("./ejemplo.txt", permisos_originales | stat.S_IXUSR  | stat.S_IXGRP )

#USR GRO OTH
#100 000 100
#001 000 000 stat.S_IXUSR    OR    >     A | B   = 1? A o B es 1
#000 001 000 stat.S_IXUSR    OR    >     A | B   = 1? A o B es 1
#101 001 100 

#RWX
#100 > 4

#000 > 0
#001 > 1
#010 > 2
#011 > 3
#100 > 4
#101 > 5
#110 > 6
#111 > 7


