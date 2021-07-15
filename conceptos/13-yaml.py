import yaml # pyyaml.org
# Fabrik, Selenium, Pandas, Numpy, YAML


with open ("ejemplo.yaml","r") as fichero_yaml:
    contenido_del_fichero=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    print(contenido_del_fichero)
    
    for elemento in contenido_del_fichero:
        print("- " + str(elemento))
        

diccionario={}
diccionario["Nombre"] ="Google"
diccionario["Puertos"] = [80,443]
print(diccionario)

with open ("ejemplo.yaml","w") as fichero_yaml:
    yaml.dump(diccionario,fichero_yaml)
    
###################################################

import json

# Leo el fichero YAML
with open ("ejemplo_generado.json","r") as fichero_json:
    contenido_del_fichero=json.load(fichero_json)
    print(">>>"+ str(contenido_del_fichero))
        
# Lo guardo como JSON
with open ("ejemplo_generado.json","w") as fichero_json:
    json.dump(contenido_del_fichero,fichero_json)
    
    
###
with open ("ejemplo_generado.yaml","r") as fichero_yaml:
    contenido_del_fichero=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    print(contenido_del_fichero)
