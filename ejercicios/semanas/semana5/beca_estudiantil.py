# Ejercicio: Beca estudiantil

# Solicitar los datos del estudiante
promedio = float(input("Ingrese el promedio académico (0-100): "))
asistencia = float(input("Ingrese el porcentaje de asistencia (0-100): "))

programa_apoyo = input(
    "¿Pertenece a un programa de apoyo institucional? (si/no): "
).lower() == "si"


# Primera condición:
# Promedio de 80 o más Y asistencia de 85% o más
condicion_academica = promedio >= 80 and asistencia >= 85

# Segunda condición:
# Programa de apoyo Y asistencia de 75% o más
condicion_apoyo = programa_apoyo and asistencia >= 75


# El estudiante obtiene la beca si cumple una de las dos condiciones
if condicion_academica or condicion_apoyo:
    print("Obtiene la beca.")
else:
    print("No obtiene la beca.")