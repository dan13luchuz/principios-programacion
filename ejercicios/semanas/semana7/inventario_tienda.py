# Constante para determinar cuándo un producto requiere reposición
STOCK_REPOSICION = 5

# Variables acumuladoras y contadores
total_inventario = 0
productos_registrados = 0
productos_reposicion = 0

# Preguntar si desea comenzar a registrar productos
continuar = input("¿Desea registrar un producto? (s/n): ")

while continuar.lower() == "s":
    print("\n--- Registro de producto ---")

    nombre_producto = input("Nombre del producto: ")
    precio_unitario = float(input("Precio unitario: ₡"))
    cantidad = int(input("Cantidad en existencia: "))

    if precio_unitario <= 0:
        print("Precio inválido. El producto no fue registrado.")

    else:
        valor_producto = precio_unitario * cantidad
        total_inventario = total_inventario + valor_producto
        productos_registrados = productos_registrados + 1

        if cantidad < STOCK_REPOSICION:
            productos_reposicion = productos_reposicion + 1
            print("El producto requiere reposición.")
        else:
            print("El producto no requiere reposición.")

        print("Producto registrado correctamente.")

    continuar = input("\n¿Desea continuar? (s/n): ")

print("\n--- Resumen del inventario ---")
print(f"Valor total del inventario: ₡{total_inventario:,.2f}")
print(f"Productos registrados: {productos_registrados}")
print(f"Productos que requieren reposición: {productos_reposicion}")