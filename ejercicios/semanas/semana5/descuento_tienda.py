# Ejercicio 2: Descuento en una tienda

edad = int(input("Ingrese la edad del cliente: "))
monto_compra = float(input("Ingrese el monto total de la compra: "))

tarjeta_frecuente = input(
    "¿Tiene tarjeta de cliente frecuente? (si/no): "
).lower() == "si"


if (tarjeta_frecuente and monto_compra >= 50000) or edad >= 65:
    descuento = 10
else:
    descuento = 0


monto_descuento = monto_compra * descuento / 100
monto_final = monto_compra - monto_descuento


print("Monto original:", monto_compra)
print("Porcentaje de descuento:", descuento, "%")
print("Monto final:", monto_final)