# nombreDiccionario = {
#     "clave1": "valor1",
#     "clave2": "valor2",
#     "clave3": "valor3"
# }

# informacionPersonal = {
#     "nombre": "gabriela",
#     "edad": 8,
#     "ciudad": "medellin"
# }
# print(informacionPersonal)

# nombres = {
#     "nombre": "carlos",
#     "edad": 30,
#     "cursos": ["py","js","nodejs","java"]
# }
# print(nombres)
# print(nombres["nombre"])
# print(nombres["edad"])
# print(nombres["cursos"][1])

#------------AGREGAR---------------------------------

# miDiccionario ={
#     "nombre" : "sara",
#     "edad" : 30
# }
# miDiccionario["profesion"] = "Desarrollador"
# print(miDiccionario)

# #-------------EDITAR----------------------------------------
# miDiccionario["edad"] = 32
# print(miDiccionario)
# #------------ELIMINAR-------------------------------------
# del miDiccionario["edad"]
# print(miDiccionario)

# #pop eliminar del diccionario y almacenarse en una variable
# texto = miDiccionario.pop("nombre")
# print(miDiccionario)
# print(texto)

# #-----------agregar multiples valores-----------------------
# nuevosDatos = {
#     "ciudad": "buenaventura",
#     "telefono": 21323,
#     "direccion": "calle 34 #45-90"
# }
# for clave, valor in nuevosDatos.items():
#     miDiccionario[clave] = valor
    
# print(miDiccionario)

# #-------------multiples valotres--------------------------
# claveEliminar = ["profesion", "ciudad"]

# for clave in claveEliminar :
#     if clave in miDiccionario:
#         del miDiccionario[clave]
        
# print(miDiccionario)

# #--------------------------------------------------------
# estudiante = {}

# nombre = input("ingese su nombre: ")
# estudiante["datos"] = nombre

# print(f"el nombre es {estudiante['datos']}")

