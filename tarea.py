# Ejercicio 1: Mayor de edad
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2: Par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

# Ejercicio 3: Comparar dos números
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
if a > b:
    print("El primero es mayor")
elif b > a:
    print("El segundo es mayor")
else:
    print("Son iguales")

# Ejercicio 4: Verificar si el año es bisiesto
año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

# Ejercicio 5: Calcular el descuento en una compra
precio = float(input("Precio original: "))
descuento = float(input("Descuento (%): "))
final = precio - (precio * descuento / 100)
print("Precio final:", final)

# Ejercicio 6: Operaciones aritméticas básicas
a = float(input("Número 1: "))
b = float(input("Número 2: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

# Ejercicio 7: Número dentro de un rango
n = int(input("Número: "))
if 10 <= n <= 50:
    print("Está en el rango")
else:
    print("Fuera del rango")

# Ejercicio 8: Información del usuario
nombre = input("Tu nombre: ")
edad = input("Tu edad: ")
ciudad = input("Tu ciudad: ")
print("Nombre:", nombre, "Edad:", edad, "Ciudad:", ciudad)

# Ejercicio 9: Suma de dos números
a = int(input("Número 1: "))
b = int(input("Número 2: "))
print("Suma:", a + b)

# Ejercicio 10: Comparación de dos números con operadores lógicos
a = int(input("Número 1: "))
b = int(input("Número 2: "))
print(a > 10 and b > 10)

# Ejercicio 11: Comparación de tres números con operadores lógicos
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
if a > b and b > c:
    print("Se cumple: a > b > c")
else:
    print("No se cumple")

# Ejercicio 12: Operadores lógicos (and, or, not)
x = True
y = False
print("and:", x and y)
print("or:", x or y)
print("not x:", not x)

# Ejercicio 13: Combinación de operadores lógicos y relacionales
n = int(input("Número: "))
if n % 2 == 0 and 20 <= n <= 50:
    print("Es par y está en el rango")
else:
    print("No cumple con ambas condiciones")

# Ejercicio 14: Calificación por nota
nota = int(input("Nota (1-100): "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")

# Ejercicio 15: Determinar si un número es positivo, negativo o cero
n = float(input("Número: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Cero")
