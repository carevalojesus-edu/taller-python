def saludar():
    print("Hola, te estoy saludando desde la función saludar del módulo ejemplo9.py")

def despedir():
    print("Adios, te estoy despidiendo desde la función despedir del módulo ejemplo9.py")

def sumar(a,b):
    print(f"La suma de {a} + {b} es {a+b}")


def imprimir(valor):
    print(valor)

def cuadrado(x):
    return x ** 2

if __name__ == '__main__':
    despedir()
    sumar(25,50)
    imprimir("Hola mundo")
    imprimir(cuadrado(5))
        