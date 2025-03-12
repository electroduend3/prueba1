def suma (a, b):
    return a + b    # La función suma recibe dos parámetros y devuelve la suma de ambos
def resta (a, b):
    return a - b    # La función resta recibe dos parámetros y devuelve la resta de ambos
def multiplicacion (a, b):
    return a * b    # La función multiplicación recibe dos parámetros y devuelve la multiplicación de ambos
def division (a, b):
    return a / b    # La función división recibe dos parámetros y devuelve la división de ambos
# # Se pueden realizar operaciones aritméticas con las funciones    

# Llamada a la función suma
suma1 = suma(3, 2)
print (suma1)    # La salida de esta sentencia es 5
# Llamada a la función resta
resta1 = resta(3, 2)
print (resta1)   # La salida de esta sentencia es 1
# Llamada a la función multiplicación
multiplicacion1 = multiplicacion(3, 2)
print (multiplicacion1) # La salida de esta sentencia es 6  
# Llamada a la función división
division1 = division(3, 2)
print (division1) # La salida de esta sentencia es 1.5  

def saludo (nombre):
    return "Hola " + nombre # La función saludo recibe un parámetro y devuelve el texto Hola seguido del nombre
def despedida (nombre):
    return "Adiós " + nombre # La función despedida recibe un parámetro y devuelve el texto Adiós seguido del nombre

saludo1 = saludo("Juan")
print (saludo1) # La salida de esta sentencia es Hola Juan
despedida1 = despedida("Juan")
print (despedida1) # La salida de esta sentencia es Adiós Juan

def en_pantalla (frase1, frase2):
    print (frase1, frase2) # La función en_pantalla recibe dos parámetros y los imprime en la consola. "return" no es obligatorio en este caso. En otros lenguajes a las funciones que no devuelven un valor se les llama procedimientos

en_pantalla("Hola", "mundo!") # La salida de esta sentencia es Hola mundo!
en_pantalla("Me gusta", "Python") # La salida de esta sentencia es Me gusta Python

# POLIMORFISMO
# El polimorfismo es la capacidad de una función para adaptarse a los diferentes tipos de datos que recibe como parámetros
# En Python no es necesario declarar el tipo de dato de los parámetros que recibe una función
suma1 = suma(3, 2)
print (suma1)    # La salida de esta sentencia es 5
suma2 = suma("Hola", "mundo!")
print (suma2)    # La salida de esta sentencia es Holamundo!    # La función suma se adapta a los diferentes tipos de datos que recibe como parámetros
# En el caso de la función suma, si recibe dos números, devuelve la suma de ambos
# si recibe dos cadenas, concatena ambas cadenas
# si recibe un número y una cadena, devuelve un error de tipo de datos
# En Python no es necesario declarar el tipo de dato de los parámetros que recibe una función
suma3 = suma(1.5, 2.5)  # La salida de esta sentencia es 4.0
print (suma3)    # La función suma se adapta a los diferentes tipos de datos que recibe como parámetros

#FUNCIONES ANIDADAS
def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) 
    f2(b) # Llamamos a f2 desde f1
f1('Python') # Llamamos a f1 que devuelve "Python" y llama a f2 que imprime 100

# Devolviendo multiples valores
def f1(a, b):
    return a + b, a - b, a * b, a / b
# Llamamos a f1 que devuelve 4 valores y los asignamos a 4 variables
suma, resta, multiplicacion, division = f1(3, 2)
print (suma) # La salida de esta sentencia es 5
print (resta) # La salida de esta sentencia es 1
print (multiplicacion) # La salida de esta sentencia es 6
print (division) # La salida de esta sentencia es 1.5

# Otro ejemplo
def maxmin(lista):
    return max(lista), min(lista) # Devielve una tupla de 2 elementos
l = [1, 3, 5, 6, 0] # Lista de 5 elementos
maximo, minimo = maxmin(l) # Desempaqueta la tupla en 2 variables
print(minimo, maximo) # La salida de esta sentencia es 0 6

# RECURSIVIDAD
# La recursividad es la capacidad de una función de llamarse a sí misma
'''Un ejemplo muy habitual de recursividad en
programación es la función que calcula el factorial de
un número (recordemos que el factorial de x es igual
a x * (x-1) * (x-2) * … * 1'''
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
gnfactorial = factorial(5) 
print(gnfactorial) # La salida de esta sentencia es 120

# Descomponer un número en factores primos
def descomponer_factores(n): 
    factores = []  # Inicializa una lista vacía para almacenar los factores primos
    divisor = 2  # Comienza con el divisor más pequeño, que es 2
    while n > 1:  # Continúa el bucle hasta que n sea mayor que 1
        while n % divisor == 0:  # Mientras n sea divisible por el divisor sin dejar residuo
            factores.append(divisor)  # Añade el divisor a la lista de factores
            n //= divisor  # Divide n por el divisor y actualiza n
        divisor += 1  # Incrementa el divisor en 1 para probar el siguiente número
    return factores  # Devuelve la lista de factores primos

# Ejemplo de uso
numero = 56  # Define el número a descomponer en factores primos
factores = descomponer_factores(numero)  # Llama a la función y almacena el resultado en la variable factores
print(f"Los factores primos de {numero} son: {factores}")  # Imprime los factores primos del número

# Función lambda
# Las funciones lambda son funciones anónimas que se pueden definir en una sola línea
# Se utilizan para definir funciones simples que no requieren de un nombre
# Sintaxis: lambda parámetros: expresión
# Ejemplo
f = lambda x, y: x + y  # Define una función lambda que suma dos números
print(f(3, 2))  # La salida de esta sentencia es 5

# Ejemplo de uso de lambda
# La función sorted() ordena los elementos de una lista
# Sintaxis: sorted(iterable, key=lambda x: x)
# Ejemplo
l = [(1, 2), (3, 1), (5, 10), (4, 2)]  # Define una lista de tuplas
l_ordenada = sorted(l, key=lambda x: x[1])  # Ordena la lista por el segundo elemento de cada tupla
print(l_ordenada)  # La salida de esta sentencia es [(3, 1), (1, 2), (4, 2), (5, 10)]
# La lista se ordena de menor a mayor según el segundo elemento de cada tupla

# AMBITO DE LAS VARIABLES
# El ámbito de una variable es la parte del programa donde la variable es accesible
# Las variables pueden ser locales o globales
# Las variables locales son aquellas definidas dentro de una función y solo son accesibles dentro de esa función
# Las variables globales son aquellas definidas fuera de una función y son accesibles desde cualquier parte del programa
# Ejemplo
def f():
    x = 10  # Variable local
    print(x)  # Imprime el valor de la variable local
f()  # Llama a la función   
# print(x)  # Genera un error porque la variable x es local y no es accesible fuera de la función

# Ejemplo de variable global
x = 10  # Variable global
def f():
    print(x)  # Imprime el valor de la variable global
f()  # Llama a la función
print(x)  # Imprime el valor de la variable global

# Modificar una variable global desde una función
x = 10  # Variable global
def f():
    global x  # Indica que se va a modificar la variable global x
    x = 20  # Modifica el valor de la variable global
    print(x)  # Imprime el valor de la variable global
f()  # Llama a la función
print(x)  # Imprime el valor de la variable global

# Ejemplo de variable local y global con el mismo nombre
x = 10  # Variable global
def f():
    x = 20  # Variable local con el mismo nombre que la variable global
    print(x)  # Imprime el valor de la variable local
f()  # Llama a la función
print(x)  # Imprime el valor de la variable global

# Ejemplo de variable local y global con el mismo nombre y uso de la palabra reservada global
x = 10  # Variable global
def f():
    global x  # Indica que se va a modificar la variable global x
    x = 20  # Modifica el valor de la variable global
    print(x)  # Imprime el valor de la variable global
    x = 30  # Modifica el valor de la variable global
    print(x)  # Imprime el valor de la variable global
f()  # Llama a la función
print(x)  # Imprime el valor de la variable global

