from jinja2 import Template


valores={"SERVICIOS": ("MYSQL","SSH") }

with open("plantilla.jinja") as archivo_plantilla:
    texto_de_la_plantilla=archivo_plantilla.read()
    
mi_plantilla_jinja=Template( texto_de_la_plantilla )

resultado=mi_plantilla_jinja.render( valores )

print(resultado)