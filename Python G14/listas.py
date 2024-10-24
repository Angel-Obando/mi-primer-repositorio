# lista = [12, 34, 3, "hola", 3.4, 45.67,  "python", True, [ 34, "bienvenidos"]]

# print(lista)

# numeros = [2, 5, 6, 7, 8 ]
# print(numeros)
# print(numeros[1])

#--------------------------METODOS DE LISTAS---------------------------------

# frutas = ["piña", "sandia", "manzana", "manzana"]
# #metodo append(elemento) : agrega elementos a la lista
# frutas.append("uvas")
# print(frutas)

# #insert(posicion, elemento) : inserta un elemento a la lista en la posicion especifica
# frutas.insert(1, "bananos")
# print(frutas)

# #remove(elemento). elimina un elemento de la lista
# frutas.remove("uvas")
# print(frutas)

# #pop : elimina de la lista un elemento, pero me lo almacena en una variable
# elemento = frutas.pop(0)
# print("se elimino de la lista esta fruta",elemento)
# print(frutas)

# print(frutas[:2])
# print(frutas)

# #----------------------------------------------------------------------------------------

# contador = frutas.count("manzana")
# print(contador)

# print(len(frutas))#contar los elementos

# nombres = []

# nombre1 = input("ingrese el primer nombre: ")
# nombres.append(nombre1)
# nombre2 = input("ingrese el primer nombre: ")
# nombres.append(nombre2)
# nombre3 = input("ingrese el primer nombre: ")
# nombres.append(nombre3)

# print("los nombres que usted ingreso son: ",nombres)

#------------------------------------------------------------------

# productos = []

# producto1 = float(input("ingrese el precio de su primer producto "))
# productos.append(producto1)
# producto2 = float(input("ingrese el precio de su segundo producto2 "))
# productos.append(producto2)
# producto3 = float(input("ingrese el precio de su tercer producto "))
# productos.append(producto3)

# print("El precio de sus productos es: ",productos)

# suma = producto1 + producto2 + producto3
# print("el total de sus productos es: ",suma)

# listaCompras = []

# while True:
#     producto = input("ingrese el nombre del producto a la lista: ")
#     listaCompras.append(producto)
    
#     continuar = input("quiere agregar mas productos? (si/no): ").lower()
#     if continuar == "no":
#         break
# print (f"\n------LISTA DE PRODUCTOS-------")

# for i in listaCompras:
#     print(i)

# contactos = []

# print("------------AGENDA TELEFONICA-----------")

# while True :
#     print("\n1. agregar contacto")
#     print("\n2. eliminar contacto")
#     print("\n3. mostar contacto")
#     print("\n4. salir")
    
#     opcion = input("ingrese una opcion")
    
#     if

# películas = []  # Lista para almacenar las películas

# while True:
#     print("\n------------Menú------------")
#     print("\n1. Agregar película")
#     print("\n2. Eliminar película")
#     print("\n3. Mostrar películas")
#     print("\n4. Buscar película")
#     print("\n5. Salir")

#     opcion = input("Selecciona una opción: ")

#     if opcion == "1":
#         pelicula = input("Ingrese el nombre de la película: ")
#         películas.append(pelicula)
#         print(f"La película '{pelicula}' se ha agregado a la lista.")

#     elif opcion == "2":
#         pelicula_eliminar = input("Ingrese el nombre de la película a eliminar: ")
#         if pelicula_eliminar in películas:
#             películas.remove(pelicula_eliminar)
#             print(f"La película '{pelicula_eliminar}' se ha eliminado.")
#         else:
#             print("La película no se encuentra en la lista.")

#     elif opcion == "3":
#         if películas:
#             print("Tus películas favoritas:")
#             for pelicula in películas:
#                 print(pelicula)
#         else:
#             print("Tu lista de películas está vacía.")

#     elif opcion == "4":
#         pelicula_buscar = input("Ingrese el nombre de la película a buscar: ")
#         if pelicula_buscar in películas:
#             print(f"La película '{pelicula_buscar}' se encuentra en la lista.")
#         else:
#             print("La película no se encuentra en la lista.")

#     elif opcion == "5":
#         print("¡Hasta luego!")
#         break

#     else:
#         print("Opción inválida. Por favor, elige una opción del menú.")
    

tareas = []
id_tarea = 1

while True:
    print("\n--- Gestor de Tareas ---")
    print("1. Crear una nueva tarea")
    print("2. Leer todas las tareas")
    print("3. Actualizar una tarea")
    print("4. Eliminar una tarea")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (AAAA-MM-DD): ")
        tarea = {"id": id_tarea, "descripcion": descripcion, "fecha_vencimiento": fecha_vencimiento}
        tareas.append(tarea)
        id_tarea += 1
        print("Tarea agregada exitosamente.")

    elif opcion == 2:
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("\nLista de Tareas:")
            for tarea in tareas:
                print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Fecha de vencimiento: {tarea['fecha_vencimiento']}")

    elif opcion == 3:
        id_actualizar = int(input("Ingrese el ID de la tarea a actualizar: "))
        encontrada = False
        for tarea in tareas:
            if tarea['id'] == id_actualizar:
                nueva_descripcion = input("Ingrese la nueva descripción (o deje vacío para mantener): ")
                nueva_fecha = input("Ingrese la nueva fecha de vencimiento (o deje vacío para mantener): ")
                tarea['descripcion'] = nueva_descripcion if nueva_descripcion else tarea['descripcion']
                tarea['fecha_vencimiento'] = nueva_fecha if nueva_fecha else tarea['fecha_vencimiento']
                print("Tarea actualizada exitosamente.")
                encontrada = True
                break
        if not encontrada:
            print("Tarea no encontrada.")

    elif opcion == 4:
        id_eliminar = int(input("Ingrese el ID de la tarea a eliminar: "))
        encontrada = False
        for i, tarea in enumerate(tareas):
            if tarea['id'] == id_eliminar:
                del tareas[i]
                print("Tarea eliminada exitosamente.")
                encontrada = True
                break
        if not encontrada:
            print("Tarea no encontrada.")

    elif opcion == 5:
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")