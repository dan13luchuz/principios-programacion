'''
Una institución organiza un evento presencial y necesita un sistema que determine si una persona puede ingresar y, en caso afirmativo, qué tipo de acceso recibirá.

Para tomar la decisión, el sistema debe conocer los siguientes datos:
    - La edad de la persona (age).
    - Si posee una entrada válida (hasValidTicket).
    - Si pertenece a la institución (belongsToInstitution).
    - La hora en la que intenta ingresar (entryHour).

La organización ha establecido las siguientes reglas:
    - Para ingresar, la persona debe tener una entrada válida.
    - Si no tiene una entrada válida, el acceso es denegado, independientemente de las demás condiciones.
    - Las personas menores de 18 años no pueden ingresar al evento.
    - Las personas de 18 años o más pueden continuar con la evaluación de las demás condiciones.
    - Si la persona pertenece a la institución y llega antes de las 18:00, recibe acceso preferencial.
    - Si pertenece a la institución pero llega a las 18:00 o después, recibe acceso general.
    - Si no pertenece a la institución, puede ingresar únicamente con acceso general.
'''


hasValidTicket = input("¿Tiene una entrada válida? (si/no): ")
age = int(input("Ingrese su edad: "))
belongsToInstitution = input("¿Pertenece a la Univercidad CENFOTEC? (si/no): ")
entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

# Posible solución 1

if hasValidTicket == "no":
    print("Acceso denegado: no tiene una entrada válida")
elif age < 18:
    print("Acceso denegado: es menor de edad")
elif belongsToInstitution == "si":
    if entryHour < 18: 
        print("Acceso permitido: acceso preferencial")
    else:
        print("Acceso permitido: acceso general")
else: 
    print("Acceso permitido: acceso general")


# Posible solución 2

if hasValidTicket == "si":
    if age < 18:
        print("Acceso denegado: es menor de edad")
    elif belongsToInstitution == "si":
        if entryHour < 18: 
            print("Acceso permitido: acceso preferencial")
        else:
            print("Acceso permitido: acceso general")
    else: 
        print("Acceso permitido: acceso general")
else: 
    print("Acceso denegado: no tiene una entrada válida")


#Posible solución 3
hasValidTicket = input("¿Tiene una entrada válida? (si/no): ")

if hasValidTicket == "no":
    print("Acceso denegado: no tiene una entrada válida")
else:
    age = int(input("Ingrese su edad: "))

    if age < 18:
        print("Acceso denegado: es menor de edad")
    else:
        belongsToInstitution = input("¿Pertenece a la Universidad CENFOTEC? (si/no): ")

        if belongsToInstitution == "si":
            entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

            if entryHour < 18:
                print("Acceso permitido: acceso preferencial")
            else:
                print("Acceso permitido: acceso general")
        else:
            print("Acceso permitido: acceso general")

# Posible solución 4
# "texto".lower() Permite convertir un texto a letras minúsculas. Ejemplo: "Si", "sI", "SI", "si" serían convertidas a "si"
# "texto".upper() Permite convertir un texto a mayúsculas 

hasValidTicket = input("¿Tiene una entrada válida? (si/no): ").lower()

if hasValidTicket == "no":
    print("Acceso denegado: no tiene una entrada válida")
else:
    age = int(input("Ingrese su edad: "))

    if age < 18:
        print("Acceso denegado: es menor de edad")
    else:
        belongsToInstitution = input("¿Pertenece a la Universidad CENFOTEC? (si/no): ").lower()

        if belongsToInstitution == "si":
            entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

            if entryHour < 18:
                print("Acceso permitido: acceso preferencial")
            else:
                print("Acceso permitido: acceso general")
        else:
            print("Acceso permitido: acceso general")
# "texto".lower() Permite convertir un texto a letras minúsculas. Ejemplo: "Si", "sI", "SI", "si" serían convertidas a "si"
# "texto".upper() Permite convertir un texto a mayúsculas