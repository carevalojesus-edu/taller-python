def dividir(a,b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

if __name__ == '__main__':

    valor1 = int(input("Ingrese el primer valor:"))
    valor2 = int(input("Ingrese el segundo valor:"))

    c, r = dividir(valor1=12, valor2=3)
    print(f"El cociente es {c} y el residuo es {r}")
