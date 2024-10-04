print (" ")
print("Danna Paola Martinez Jimenez")
print (" ")
# Lista de precios
precios = [43, 57, 92, 20, 37, 5, 9]

# Ordenar y mostrar precios
print(sorted(precios))

print (" ")
print (" ")

# Almacenando las materias en una lista
materias = ["Matematicas", "Ecosistemas", "Humanidades", "Ingles", "Framework", "Metodologias", "Lengua y  Comunicacion"]

# Desplegando las materias en pantalla
for materia in materias:
    print(materia)
    
print (" ")
print (" ")

# Lista de materias
materias = ["Matematicas", "Ecosistemas", "Humanidades", "Ingles", "Framework", "Metodologias", "Lengua y Comunicación"]

# Mostrar el mensaje para cada materia
for materia in materias:
    print("Estoy cursando", materia)

print (" ")
print (" ")

# Lista de materias
materias = ["Matematicas", "Ecosistemas", "Humanidades", "Ingles", "Framework", "Metodologias", "Lengua y Comunicación"]

# Pedir calificaciones y mostrar resultados
for materia in materias:
    calificacion = input("Calificación en " + materia + ": ")
    print("En", materia, "has obtenido", calificacion + ".")

print (" ")
print (" ")

# Lista para almacenar los números
numeros = []
num = int(input("Ingresa la cantidad de numeros ganadores: "))

# Pedir los números triunfadores
for i in range(num): 
    numero = int(input("Ingrese un numero ganador: "))
    numeros.append(numero)

# Mostrar los números ordenados
numeros.sort()
print("Numeros ganadores en orden:", numeros)
print (" ")












