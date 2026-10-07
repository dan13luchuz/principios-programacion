# Programa 3: El mayor de tres números

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print("El mayor es:", mayor)