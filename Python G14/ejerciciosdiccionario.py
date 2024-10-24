# contactos = []

# # Crear un contacto
# nuevo_contacto = {'nombre': 'Juan', 'apellido': 'Pérez', 'telefono': '1234567890'}
# contactos.append(nuevo_contacto)

# # Crear otro contacto
# contactos.append({'nombre': 'Ana', 'apellido': 'García', 'telefono': '9876543210'})

# # Leer todos los contactos
# for contacto in contactos:
#     print(f"Nombre: {contacto['nombre']}, Apellido: {contacto['apellido']}, Teléfono: {contacto['telefono']}")

# # Actualizar el teléfono de Juan Pérez
# for contacto in contactos:
#     if contacto['nombre'] == 'Juan' and contacto['apellido'] == 'Pérez':
#         contacto['telefono'] = '5555555555'

# # Eliminar a Ana García
# for i in range(len(contactos)):
#     if contactos[i]['nombre'] == 'Ana' and contactos[i]['apellido'] == 'García':
#         del contactos[i]
#         break



# diccionarioContacto = {
#     "juan": "3333",
#     "Carlos": "8999",
#     "Dario": "89877",
#     "javier": "171652"
# }
# #crear
# diccionarioContacto["Diana"]= "6655"
# print(diccionarioContacto)
# print(f"contacto agregado: Diana {diccionarioContacto['Diana']}")

# #leer contacto
# print("\nDICCIONARIO CONTACTOS")
# for nombre, telefono in diccionarioContacto.items():
#     print(f"{nombre} : {telefono}")

# #eliminar
# del


#---------------------------------------------------------

# inventario = {}
# continuar = True

# while continuar :
#     print("\n Opciones")
#     print("1. agregar o actualizar un producto: ")
#     print("2. Eliminar un producto: ")
#     print("3. mostrar el inventario: ")
#     print("4. para salir")

#     opcion = input("ingrese una opcion entre 1 al 4 :")

#     if opcion == "1": 
#         #agregar
#         producto = input("ingrese el nombre del producto :").lower()
#         cantidad = int(input(f"ingrese la cantidad del producto {producto} :"))

#         if producto in inventario:
#             inventario[producto] += cantidad
#             print(f"se agrego {cantidad} unidades de {producto}. total : {inventario[producto]} unidades ")
#         else:
#             inventario[producto] = cantidad
#             print(f"{producto.capitalize()} añadido al inventario con {cantidad} unidades")

#     #eliminar
#     elif opcion == "2":
#         producto = input("ingrese el nombre del producto a eliminar: ").lower()

#         if producto in inventario:
#             del inventario[producto]
#             print(f"{producto} eliminado del inventario ")

#         else:
#             print(f"producto {producto} No existe en el inventario")

#     #mostrar 
#     elif opcion == "3":
#         print("\n INVENTARIO ACTUAL")
#         if inventario :
#             for producto, cantidad in inventario.items():
#                 print(f"{producto} : {cantidad} unidades")

#         else:
#             print("inventario vacio")       

#     #salir
#     elif opcion == "4":
#         continuar = False
#         print("gracias por visitarnos")
#     else:
#         print("opcion incorrectar")


