PORCENTAJE_DESCUENTO = 10

precio_original = float(input("Ingrese el precio original: "))

monto_descuento = precio_original * PORCENTAJE_DESCUENTO / 100

precio_final = precio_original - monto_descuento

print("Precio final:", precio_final)