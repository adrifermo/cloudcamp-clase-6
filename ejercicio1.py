
usuarios = [[],[],[]]

tamaño = 2

for i in range(tamaño):
    print("Ingrese los datos de la persona ", i + 1)
    nombre = input("Nombre: ")
    id = input("Identificación: ")
    edad = input("Edad: ")
    
    usuarios[0].append(nombre)
    usuarios[1].append(id)
    usuarios[2].append(edad)
    
for i in range(tamaño):
    print("nombre: ", usuarios[0][i])
    print("id: ", usuarios[1][i])
    print("edad: ", usuarios[2][i])