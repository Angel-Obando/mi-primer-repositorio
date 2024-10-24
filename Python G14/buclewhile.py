#contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1
    
# print("fin del bucle")

#------------------------------------------------------------------------------------

# while contador <= 100:
#     contador += 1
#     print(contador)
#     if contador == 50:
#         break
    
# print("fin del bucle")

#------------------------------------------------------------------------------------

contador = 0
notas = []
mayores_a_7 = 0
menores_a_7 = 0

while contador < 10:
    nota = float(input(f"Ingrese la nota del alumno {contador+1}: "))
    notas.append(nota)
    contador += 1

i = 0
while i < len(notas):
    if notas[i] >= 7:
        mayores_a_7 += 1
    else:
        menores_a_7 += 1
    i += 1


print("Alumnos con notas mayores o iguales a 7:", mayores_a_7)
print("Alumnos con notas menores a 7:", menores_a_7)