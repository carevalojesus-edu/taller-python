

if __name__ == '__main__':

    for i in range(1,11):
        print(i)
    
    suma = 0
    numero = int(input("Ingrese la cantidad de numeros a sumar:"))

    for i in range(numero):
        suma += int(input(f"Ingrese el numero {i+1}:"))
    
    print(f"La suma es {suma}")


    