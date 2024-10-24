# Información del usuario
usuario = {}
reservas = []
vuelos = [
    {"destino": "Nueva York", "fecha": "15/11/2024", "precio": 300},
    {"destino": "Madrid", "fecha": "20/11/2024", "precio": 450},
    {"destino": "Tokio", "fecha": "25/11/2024", "precio": 600}
]
paquetes = [
    {"destino": "Cancún", "duración": "7 días", "precio": 1200},
    {"destino": "París", "duración": "5 días", "precio": 1500},
    {"destino": "Roma", "duración": "6 días", "precio": 1400}
]

continuar = True

print("\n¡BIENVENID@ A EXPLORA TU MUNDO!")
print("\nSomos una agencia de viajes diseñada para que tus vacaciones soñadas sean más fáciles de elegir.")
print("\nQueremos saber más de ti para personalizar tu búsqueda.")
nombreUsuario = input("Cuéntanos... ¿Cuál es tu nombre?: ")
identificacionUsuario = input(f"Hola {nombreUsuario}, ingresa tu número de identidad por favor: ")

usuario["nombre"] = nombreUsuario
usuario["identificacion"] = identificacionUsuario

print(f"\n{nombreUsuario}, tu número de identificación {identificacionUsuario} ha sido guardado exitosamente.")
print("En cualquier momento puedes modificar tu usuario o tu documento.")

while continuar:
    print("\n OPCIONES :")
    print("1. Modificar mi usuario")
    print("2. Ver hoteles disponibles")
    print("3. Ver vuelos disponibles")
    print("4. Ver paquetes todo incluido disponibles")
    print("5. Salir :(")
    
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        nuevoUsuario = input("Ingresa tu nuevo nombre: ")
        nuevaIdentificacion = input("Ingresa tu nueva identificación: ")
        usuario["nombre"] = nuevoUsuario
        usuario["identificacion"] = nuevaIdentificacion
        print(f"¡Bienvenid@ {nuevoUsuario}, tu identificación {nuevaIdentificacion} ha sido modificada y actualizada correctamente!")

    elif opcion == "2":
        while True:
            print("\nOpciones:")
            print("1. Agregar reserva")
            print("2. Eliminar reserva")
            print("3. Mostrar todas las reservas")
            print("4. Regresar al menú principal")
            
            opcionHotel = input("Ingrese una opción: ")
            
            if opcionHotel == "1":
                nombre_hotel = input("Ingrese el nombre del hotel: ")
                fecha_entrada = input("Ingrese la fecha de entrada (DD/MM/AAAA): ")
                fecha_salida = input("Ingrese la fecha de salida (DD/MM/AAAA): ")
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                
                nueva_reserva = {
                    "hotel": nombre_hotel,
                    "fecha_entrada": fecha_entrada,
                    "fecha_salida": fecha_salida,
                    "cliente": nombre_cliente
                }
                
                reservas.append(nueva_reserva)
                print("Reserva agregada exitosamente.")
            
            elif opcionHotel == "2":
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
            
            elif opcionHotel == "3":
                if len(reservas) == 0:
                    print("No hay reservas registradas.")
                else:
                    for reserva in reservas:
                        print(f"Hotel: {reserva['hotel']}")
                        print(f"Fecha de entrada: {reserva['fecha_entrada']}")
                        print(f"Fecha de salida: {reserva['fecha_salida']}")
                        print(f"Cliente: {reserva['cliente']}")
                        print("--------------------")
            
            elif opcionHotel == "4":
                break
            
            else:
                print("Opción inválida.")
    
    elif opcion == "3":
        print("\nVuelos disponibles:")
        for vuelo in vuelos:
            print(f"Destino: {vuelo['destino']}, Fecha: {vuelo['fecha']}, Precio: ${vuelo['precio']}")
    
    elif opcion == "4":
        print("\nPaquetes todo incluido disponibles:")
        for paquete in paquetes:
            print(f"Destino: {paquete['destino']}, Duración: {paquete['duración']}, Precio: ${paquete['precio']}")
    
    elif opcion == "5":
        print("¡Hasta luego!")
        continuar = False
    
    else:
        print("Opción inválida.")