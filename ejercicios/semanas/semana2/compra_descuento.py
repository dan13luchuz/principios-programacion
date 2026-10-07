tipo_juego = input("Ingrese el tipo de juego (Play/Xbox): ")
precio_unitario = float(input("Ingrese el precio del juego: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

subtotal = precio_unitario * cantidad
descuento = subtotal * 0.05
total = subtotal - descuento

print("\n--- Datos de la compra ---")
print("Tipo de juego:", tipo_juego)
print("Precio unitario:", precio_unitario)
print("Cantidad comprada:", cantidad)
print("Subtotal:", subtotal)
print("Descuento aplicado (5%):", descuento)
print("Total a pagar:", total)