age = int(input("Ingrese la edad: "))

if age >= 0 and age < 1:
    print("Es un bebé")

elif age >= 1 and age < 12:
    acompanante = input("¿Tiene acompañante? (si/no): ").lower()

    if acompanante == "si":
        print("Es infante, puede participar")
    else:
        print("Es infante, no puede participar")

elif age >= 12 and age < 18:
    permiso = input("¿Trae permiso para participar? (si/no): ").lower()

    if permiso == "si":
        print("Es adolescente, puede participar")
    else:
        print("Es adolescente, no puede participar")

else:
    print("Error: La edad debe estar entre 0 y 17 años")