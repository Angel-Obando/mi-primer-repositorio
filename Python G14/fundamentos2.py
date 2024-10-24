
numero_dia = int(input("Ingrese un número del 1 al 7: "))


if numero_dia < 1 or numero_dia > 7:
    print("El número ingresado no es válido. Debe estar entre 1 y 7.")
else:
    
    if numero_dia == 1:
        print("Lunes")
    elif numero_dia == 2:
        print("Martes")
    elif numero_dia == 3:
        print("Miércoles")
    elif numero_dia == 4:
        print("Jueves")
    elif numero_dia == 5:
        print("Viernes")
    elif numero_dia == 6:
        print("Sabado") 

    else:
        print("Domingo") 