# Lista para almacenar las reservas
reservas = []

# Bucle principal del programa
while True:
    print("\nOpciones:")
    print("1. Agregar reserva")
    print("2. Eliminar reserva")
    print("3. Mostrar todas las reservas")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_hotel = input("Ingrese el nombre del hotel: ")
        fecha_entrada = input("Ingrese la fecha de entrada: ")
        fecha_salida = input("Ingrese la fecha de salida: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        nueva_reserva = {
            "hotel": nombre_hotel,
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida,
            "cliente": nombre_cliente
        }

        reservas.append(nueva_reserva)
        print("Reserva agregada exitosamente.")

    elif opcion == "2":
        if len(reservas) == 0:
            print("No hay reservas registradas.")
        else:
            for i, reserva in enumerate(reservas):
                print(f"{i+1}. {reserva['hotel']} - {reserva['cliente']}")
            
            try:
                indice = int(input("Ingrese el número de la reserva a eliminar: ")) - 1
                del reservas[indice]
                print("Reserva eliminada.")
            except (ValueError, IndexError):
                print("Número de reserva inválido.")

    elif opcion == "3":
        if len(reservas) == 0:
            print("No hay reservas registradas.")
        else:
            for reserva in reservas:
                print(f"Hotel: {reserva['hotel']}")
                print(f"Fecha de entrada: {reserva['fecha_entrada']}")
                print(f"Fecha de salida: {reserva['fecha_salida']}")
                print(f"Cliente: {reserva['cliente']}")
                print("--------------------")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")