# Constantes
PRECIO_ESTANDAR = 25000
PRECIO_DELUXE = 35000
PRECIO_COLECCIONISTA = 50000

DESCUENTO_CANTIDAD = 0.10
DESCUENTO_CANTIDAD_MAYOR = 0.15
DESCUENTO_ESTUDIANTE = 0.05

CANTIDAD_MINIMA = 3
CANTIDAD_DESCUENTO_MAYOR = 5


# Entrada de datos
edicion = input(
    "Ingrese la edición (estandar/deluxe/coleccionista): "
).lower()

cantidad = int(
    input("Ingrese la cantidad de videojuegos: ")
)

es_estudiante = input(
    "¿Es estudiante? (si/no): "
).lower()


# Determinar precio unitario
if edicion == "estandar":
    precio_unitario = PRECIO_ESTANDAR
elif edicion == "deluxe":
    precio_unitario = PRECIO_DELUXE
elif edicion == "coleccionista":
    precio_unitario = PRECIO_COLECCIONISTA
else:
    precio_unitario = None
    print("Error: la edición ingresada no es válida.")


# Continuar si la edición es válida
if precio_unitario is not None:

    subtotal = precio_unitario * cantidad

    # Nueva regla: 5 juegos o más = 15 %
    if cantidad >= CANTIDAD_DESCUENTO_MAYOR:
        descuento_cantidad = subtotal * DESCUENTO_CANTIDAD_MAYOR
        subtotal_con_descuento = subtotal - descuento_cantidad

        if es_estudiante == "si":
            descuento_estudiante = (
                subtotal_con_descuento * DESCUENTO_ESTUDIANTE
            )
        else:
            descuento_estudiante = 0

    # Regla original: 3 o 4 juegos = 10 %
    elif cantidad >= CANTIDAD_MINIMA:
        descuento_cantidad = subtotal * DESCUENTO_CANTIDAD
        subtotal_con_descuento = subtotal - descuento_cantidad

        if es_estudiante == "si":
            descuento_estudiante = (
                subtotal_con_descuento * DESCUENTO_ESTUDIANTE
            )
        else:
            descuento_estudiante = 0

    # Menos de 3 = sin descuentos
    else:
        descuento_cantidad = 0
        subtotal_con_descuento = subtotal
        descuento_estudiante = 0

    total_pagar = subtotal_con_descuento - descuento_estudiante

    print("\n--- RESUMEN DE COMPRA ---")
    print("Edición seleccionada:", edicion)
    print("Precio unitario: ₡", precio_unitario)
    print("Subtotal: ₡", subtotal)
    print("Descuento por cantidad: ₡", descuento_cantidad)
    print("Descuento por estudiante: ₡", descuento_estudiante)
    print("Total a pagar: ₡", total_pagar)