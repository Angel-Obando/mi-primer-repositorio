"""
calificacion = float(input("Ingrese su calificación (0-100): "))

if calificacion >= 90:
    print("Sobresaliente")
elif calificacion >= 80:
    print("Notable")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Suspendio")
"""

hora = int(input("Ingrese la hora actual (0-23): "))
sistema_activado = input("¿El sistema está activado? (sí/no): ").lower() == "sí"
nivel_seguridad = input("Ingrese el nivel de seguridad (bajo, medio, alto): ").lower()

if sistema_activado and 6 < hora < 18:
    print("Sistema seguro.")
elif sistema_activado and (nivel_seguridad == "medio" or nivel_seguridad == "alto"):
    print("Sistema moderadamente seguro.")
else:
    print("Sistema no seguro.")