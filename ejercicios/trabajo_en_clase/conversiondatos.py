"""
Tipos de datos: 
    - números enteros: int
    - números decimales: float
    - strings: str  
"""

"""
int(
    input("Ingrese un número entero: ")
    )
"""
numero1 = int(input("Ingrese un número entero: "))
print("Número 1 =", numero1)
print("Tipo de dato", type(numero1))
resultadoSuma = numero1 + 5 
print("Número 1: ", numero1, "+ 5 = ", resultadoSuma)
print("* - " * 12)

numero2 = float(input("Ingrese un número decimal: "))
print("Número 2 =", numero2)
print("Tipo de dato", type(numero2))
resultadoSumaNumero2 = numero2 + 5 
print("Número 2: ", numero2, "+ 5 = ", resultadoSumaNumero2)
print("-" * 50)

numero3 = float(input("Ingrese un número negativo: "))
print("Número 3 =", numero3)
print("Tipo de dato", type(numero3))
resultadoSumaNumero3 = numero3 + 5 
print("Número 3: ", numero3, "+ 5 = ", resultadoSumaNumero3)