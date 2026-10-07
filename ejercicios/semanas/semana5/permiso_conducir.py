# Ejercicio 4: Permiso para conducir

edad = int(input("Ingrese su edad: "))

tiene_licencia = input(
    "¿Posee licencia de conducir? (si/no): "
).lower() == "si"

licencia_vigente = input(
    "¿La licencia está vigente? (si/no): "
).lower() == "si"

permiso_especial = input(
    "¿Posee permiso especial? (si/no): "
).lower() == "si"


if not licencia_vigente and not permiso_especial:
    print("No puede conducir.")

elif (
    (edad >= 18 and tiene_licencia and licencia_vigente)
    or
    (edad < 18 and permiso_especial)
):
    print("Puede conducir.")

else:
    print("No puede conducir.")