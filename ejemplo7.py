

if __name__ == '__main__':

    suma = 0
    numero = int(input("Introduzca un numero (0 para salir):"))

    while numero != 0:
        suma += numero
        numero =  numero = int(input("Introduzca un numero (0 para salir):"))
    
    print(f"La suma de los numeros ingresado es {suma}")