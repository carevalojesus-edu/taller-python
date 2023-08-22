

if __name__ == '__main__':

    numero = int(input("Ingrese un numero:"))

    #validar si es numero primo
    contador = 0

    for i in range(numero):
        if numero % (i+1) == 0:
            contador += 1
    
    if contador > 2:
        print("El numero no es primo")
    else:
        print("El numero es primo")	