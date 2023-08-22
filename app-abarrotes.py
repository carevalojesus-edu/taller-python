from productos import Producto

menu_opciones = [
    "1. Agregar producto",
    "2. Ver productos",
    "3. Agregar Stock",
    "4. Vender",
    "5. Salir"
]

productos = []

def agregar_producto():
    print("Agregando producto")
    nombre_producto = input("Ingrese el nombre del producto:")
    precio_producto = float(input("Ingrese el precio del producto:"))
    stock_producto = int(input("Ingrese el stock del producto:"))

    obj_producto = Producto(nombre_producto, precio_producto, stock_producto)
    productos.append(obj_producto)
    print("Producto agregado correctamente")

def ver_productos():
    print("\nLista de productos")
    for producto in productos:
        print(f"Nombre del Producto: {producto.nombre} | Precio: S/ {producto.precio} | Stock: {producto.stock}")

def agregar_stock():
    print("\nAgregando stock")
    
    for producto in productos:
        print(f"{producto.nombre} | Stock: {producto.stock}")
    
    nombre_producto = input("Ingrese el nombre del producto:")

    for pro in productos:
        if pro.nombre == nombre_producto:
            cantidad = int(input("Ingrese la cantidad a agregar:"))
            pro.stock += cantidad
            print("Stock agregado correctamente")
            break

def vender():
    print("\nVender producto")

    for producto in productos:
        print(f"{producto.nombre} | Stock: {producto.stock}")

    precio_total = 0

    while comprar != "NO":
        nombre_producto = input("Ingrese el nombre del producto:")

        for pro in productos:
            if pro.nombre == nombre_producto:
                cantidad = int(input("Ingrese la cantidad a comprar:"))
                if cantidad > pro.stock:
                    print("No hay stock suficiente")
                    break
                else:
                    pro.stock -= cantidad
                    precio_total += pro.precio * cantidad
            else:
                print("El producto no existe")
                break
        
        comprar = input("¿Desea comprar otro producto? SI/NO:").upper()


if __name__ == "__main__":

   

    while True:
        
        print("Bienvenido a la tienda de abarrotes")
        print("Seleccione una opción:")
        
        for opcion in menu_opciones:
            print(opcion)

        opcion = int(input("Ingrese una opción:"))


        if opcion == 1:
            agregar_producto()
            
        elif opcion == 2:
            ver_productos()
            
        elif opcion == 3:
            agregar_stock()

        elif opcion == 4:
            vender()
            
        elif opcion == 5:
            break
