

if __name__ == '__main__':

    estudiantes = ["christian", "jose", "maria", "josefina", "josefa", "josefino"]

    print(estudiantes[0])
    print(estudiantes[-1])
    print(len(estudiantes))

    estudiantes[1] = "Kurt"

    for estudiante in estudiantes:
        print(estudiante)

    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante:")
    estudiantes.append(nuevo_estudiante)

    for estudiante in estudiantes:
        print(estudiante)

    print("estduiantes")

    print(estudiantes)

    sub_lista = estudiantes[1:3]
    print(sub_lista)
