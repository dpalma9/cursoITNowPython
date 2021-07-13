# Python

Lenguaje de programación
Lenguaje:
    - Sintaxis      <<<< Forma de escribirlo. Funciones que realizan los vocablos dentro de una expresión.
    - Gramatica     <<<< Tipos de vocablos que podemos usar
------------------
    - Semantica     <<<< El significado cada uno de esos vocablos
    
Características de python:
- INTERPRETADO vs Compilados:
    Quien ejecuta las instrucciones es el SO. EL SO entiende su propio lenguaje.
- No precisa definir variables
- Es de tipado dinámico vs lenguajes de tipado estático
    - En un lenguaje de tipado estático, una variable no puede apuntar más que a un determinado tipo de dato, 
       predefinido a la hora de definir la variable 
    - En un lenguaje de tipado dinámico, una variable puede apuntar a cualquier tipo de dato, 
       sin necesidad de definirlo previamente y además variable en el tiempo

Traducción estática: Compilación 
    - Antes de mandar el programa, antes se le hace un analisis exhaustuivo donde se identifican errores
    - Mejor rendimiento
Traducción en tiempo de ejecución: Interpretación
    - Más facilidad a la hora de distribuir el software

Qué interprete o intepretes usamos en python?
>> python/python3: CYTHON: Es un interprete de Python escrito en lenguaje C
        Solo permite usar una única CPU de la máquina <<<
>> jython
>> pypy

## Para qué usamos python. Casos de uso comunes.
- Data analytics <<< numpy pandas skylearn tensorflow theras. Esas librerias están escritas en C
- Automatización
    - Tareas de administración de sistemas
    - Testing
- Monitorización
- Inteligencia artificial

PYTHON Es un lenguaje muy sencillo de aprender. Con una sintaxis muy simple (al compararla con otros lenguajes)

## VARIABLE
- Un espacio de memoria donde almacenamos un valor.... RUINA !!!! GIGANTESCA !!!!
- Referencia a un espacio de memoria donde almacenamos un valor

Ejemplo:
    TEXTO = "17"
    TEXTO = 17
    TEXTO = True
    
    NUMERO > VARIABLE
    =      > OPERADOR     (SEMANTICA := >>>> ASIGNACION)
    17     > VALOR
Qué cosas hace esta linea de código?
    [17]       1º    Reserva un espacio de memoria para guardar el 17 y guarda el 17 en ese espacio de memoria
    [NUMERO]   2º    Crear una variable llamada NUMERO
    [=]        3º    Referenciar desde la variable al espacio de memoria donde está el número 17
    
Ejemplo2:
    NUMERO = 22
Qué cosas hace esta linea de código?
    [22]       1º    Reserva un espacio de memoria para guardar el 22 y guarda el 22 en ese espacio de memoria
        PREGUNTA: El 22 se guarda sobreescribiendo el 17?    El 22 se guarda en otro sitio de la RAM
        ¿Cuantas cosas hay en la RAM? 17 y 22
    [NUMERO]   2º    Reuso la variable NUMERO que ya existe
    [=]        3º    La variable NUMERO CAMBIA (VARIA) a donde referencia... 
                     Ahora referencia a la zona de memoria donde está guardado el 22
    

## TIPOS:
    Vamos a estar guardando cosas en la RAM... Cosas de diferente naturaleza:
        Números
            Enteros
                Rango completo
                Positivos
                En el rango del 0-255
        Textos
        Fechas
        Fecha y Hora
    Los datos de un determinado tipo, el que sea, se guardan en la memoria como bytes (0001110001010101010)
    
Hay determinados lenguajes que me obligan a ir eliminando EXPLICITAMENTE la basura que queda en la RAM: C
Hay lenguajes que automaticamente detectan la BASURA que voy dejando en la RAM y la borran ellos. JAVA, PYTHON
    Garbage Collector
    
Software
    SO
    Driver
    Aplicación
    Script          <<<<< Un programita muy sencillo, que ejeuta una serie de instrucciones y termina.
    Demonio             <<
    Servicio            <<
    
Que aporta PYTHON frente a lenguajes como BASH (SH) o PowerShell de Miscrosoft?
    Dispone de muchas librerias que hacen funciones (calculo, comunicar con otros sistemas...)
    Orientación a objetos <
    Independencia de la plataforma - Portabilidad


# Paradigmas de programación

Forma de estructurar el código
Un programa es algo parecido a lo que podría ser una receta de cocina o unas instrucciones de montaje de un mueble de ikea.

## Programación imperativa

Vamos escribiendo las ordenes de forma secuencial. Nuestro código se ejecuta de forma lineal, de arriba a abajo.
RECETA DE TORTILLA DE PATATAS:
    Paso 0: Poner a calaentar una sarten con 300ml de aceita
    Paso 1: Pelar patatas
    Paso 2: Trocear patatas
    Paso2.5: Si los trozos son muy grandes... partirlos a la mitad < Condicionadas
    Paso 3: Lavar patatas
    Paso 4: Echarlas en la sarten
    Paso 5: Mientras las patatas no esten hechas... dejarlas en la sarten
    Paso 6: Cuando las patatas estén doraditas... sacarlas a un plato.


## Programación procedural. Se basa en la definición de procedimientos o funciones que podemos reutilizar
RECETA DE LASAÑA
    Paso 1: Pasta sumergirla en agua
    Paso 2: Calentar agua
    ..........
    Paso n: Bechamel <<< Podría explicar aqui como preparar la bechamel...
    Paso n: Preparar una bechamel segun se indica en la pag 17.
    
    
## Programación funcional. <<< En JAVA no ha estado disponible hasta la version 1.8

Las funciones son un tipo de datos.... y por tanto referenciables a través de una variable.
Una variable puede referenciar a una funcion....
    Podemos definir funcioens que tomen como argumentos otras funciones
    Podemos definir funciones que devuelvan otra función.

# Orientación a objetos



# Ejecución de un programa

Creamos un PROCESO en SO
    -> 1º El codigo del programa se sube a la RAM
    -> 2º Que más se reserva en RAM?
        - Una zona para poner las variables y sus valores
        - Una zona para el stack de funciones: ESTA LIMITADA EN TAMAÑO
            ^^^^^
            El historial de todas las llamadas a funciones en curso de
            de cada hilo que se esté ejecutando
            
MAIN:
21 factorialRecursividad      (6)                           -> 720
    TABLA DE VARIABLES
        resultado
18 factorialRecursividad      (5)                       -> 120
    TABLA DE VARIABLES
        resultado
18 factorialRecursividad      (4)                   -> 24       
    TABLA DE VARIABLES
        resultado
18 factorialRecursividad      (3)               -> 3
    TABLA DE VARIABLES
        resultado
18 factorialRecursividad      (2)           -> 2
    TABLA DE VARIABLES
        resultado
18 factorialRecursividad      (1)       -> 1
    TABLA DE VARIABLES
        resultado
18 factorialRecursividad      (0) -> 1
    TABLA DE VARIABLES
        resultado

PILA (Stack) Una estructura de datos de programación

Una pila es un tipo de coleccion: lista, tupla, diccionario
pila vs lista?
    Una pila sigue un modelo de datos LIFO: Last In -> First Out

Stackoverflow < Desbordamiento de pila
