"""
EJERCICIO #1
Crea un programa que pida el nombre y la edad del usuario.
El programa debera imprimir en que año el usuario cumplira 100 años
"""
nombre = input ("Ingresa tu nombre : ")
edad = int(input("Ingresa tu edad : "))
print("Tu " + nombre + "edad en cien años será " + str((edad + 100)))
"""
EJERCICIO #2
Crea un programa que pida un numero entero positivo y le haga saber al usuario si es par o primo
(PISTA: investiga el operador modulo, denotado como % en muchos lenguajes de programacion)
"""
#numero = int(input("Ingresa un número entero positivo"))
#if(numero )




"""
EJERCICIO #3
Tome estas listas: 
a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 02, 21, 90]
y crea un programa que cree una nueva lista (o array)
que contenga los elementos que NO se encuentran repetidos en ninguna de las dos lista anteriores
y se imprima la lista completa (tambien se puede imprimir cada elemento de la lista)
"""
#a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
#b = [1, 5, 77, 22, 90, 25, 83, 100, 22, 21, 90]




"""
EJERCICIO #4
Crea un programa que le pida al usuario una palabra y muestre si esa palabra es un palindromo
NOTA: un palindromo es una palabra que se puede escribir al derecho y al reves de la misma manera.
(Por ejemplo: ana, ala, oso)
(EXTRA: intenta hacerlo en 4 lineas de codigo solamente (investiga IF TERNARIO en Python))
"""
# list es un método
palabra = input("Ingresa una palabra : ")
lpalabra = list(palabra)
print("Es palindrómo") if lpalabra == list(reversed(palabra)) else print("No es palindrómo")
 
"""
EJERCICIO #5
Crea un programa con un diccionario que contenga de llave un nombre
y de valor el cumpleaños de esta persona.
El programa pedira el nombre de la persona y se debera imprimir la fecha de su cumpleaños
"""
diccionario = {"Andres":"Pato 18/10/2000", "Ana":"Vaca 04/10/2000"}
nombre = input("Ingresa Andrés o Ana: ")
print(diccionario[nombre])  
