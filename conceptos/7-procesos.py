#import  subprocess
#codigo_salida=subprocess.call( ("ping","-c","1","goooogle.es") )

#print(codigo_salida)

from subprocess import run, PIPE

subproceso=run( ("ping","-c","1","goooogle.es") , stdout=PIPE, stderr=PIPE)
print(subproceso.returncode)
#print(subproceso.stdout)
#print(subproceso.stderr)
