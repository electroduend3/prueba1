# Como norma general, los comentarios se escriben en la línea anterior al código que se desea comentar
# Este es un comentario de una sola línea
'''Este es un comentario de varias líneas
   que se extiende por varias líneas
   y se cierra con tres comillas simples'''
# La salida de esta sentencia es Hola mundo!
print ('Hola mundo!') # La función print() imprime el texto Hola mundo! en la consola (SALIDA DE DATOS)

# También se puede asignar el texto a una variable y luego imprimir la variable
'''La variable gs_saludo almacena el texto Hola mundo!
   y luego se imprime el contenido de la variable
   que es Hola mundo!
   La forma habitual de nombrar variables en Python es con minúsculas y separando las palabras con guiones bajos
   Ejemplo: gs_saludo, gn_numero, gb_bandera, donde gs es para cadenas, gn para números y gb para booleaanos
   donde la g es de global y la s, n o b es el tipo de dato que almacena la variable'''
gs_saludo = 'Hola mundo!' 
print (gs_saludo) 
gn_numero = 5
print (gn_numero)   # La salida de esta sentencia es 5
gb_bandera = True
print (gb_bandera)  # La salida de esta sentencia es True   o Verdadero
gn_numero1 = 3
gn_numero2 = 2
gn_suma = gn_numero1 + gn_numero2
print (gn_suma)     # La salida de esta sentencia es 5
gn_resta = gn_numero1 - gn_numero2
print (gn_resta)    # La salida de esta sentencia es 1
gb_bandera1 = gn_numero1 > gn_numero2
print (gb_bandera1) # La salida de esta sentencia es True o Verdadero
gb_bandera2 = gn_numero1 < gn_numero2
print (gb_bandera2) # La salida de esta sentencia es False o Falso
gb_bandera3 = gn_numero1 == gn_numero2  # El doble igual es para comparar si dos valores son iguales
print (gb_bandera3) # La salida de esta sentencia es False o Falso      
gb_bandera4 = gn_numero1 != gn_numero2  # El signo de exclamación seguido de un igual es para comparar si dos valores son diferentes
print (gb_bandera4) # La salida de esta sentencia es True o Verdadero   

# ENTRADA DE DATOS
gs_nombre_introducido = input("Introduzca su nombre:") # Esta sentencia solicita al usuario que introduzca su nombre
# y lo almacena en la variable gs_nombre_introducido
print ("Hola", gs_nombre_introducido) # Esta sentencia imprime el texto Hola seguido del nombre introducido por el usuario
'''IMPORTANTE: Todo lo introducido por el usuario mediante input (), se considera como texto, por lo que si se desea realizar
 operaciones aritméticas con los datos introducidos por el usuario, se debe convertir el texto a número, ya sea entero o flotante,
 a esto  se le denomina casting'''
gn_numero_introducido = int(input("Introduzca su edad:")) # Esta sentencia solicita al usuario que introduzca un número entero
# y lo almacena en la variable gn_numero_introducido   
print ("El número introducido es:", gn_numero_introducido) # Esta sentencia imprime el texto El número introducido es: seguido del número introducido por el usuario
'''Como norma, realiza casting con números con los que vas hacer operaciones aritméticas, por ejemplo la edad,
 pero no con datos como el número de teléfono'''
'''Las constantes son variables cuyo valor no cambia a lo largo de la ejecución del programa, en Python no existen las constantes
pero se pueden simular utilizando variables, para identificarlas, escribimos sus nombres en mayúsculas'''
PI = 3.1416
print (PI) # La salida de esta sentencia es 3.1416
# Se pueden realizar operaciones aritméticas con las constantes
radio = 5
area = PI * radio ** 2
print (area) # La salida de esta sentencia es 78.54
perimetro = 2 * PI * radio
print (perimetro) # La salida de esta sentencia es 31.416

