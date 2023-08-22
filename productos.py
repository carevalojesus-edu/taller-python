class Producto:
    def __init__(self, nombre_prod, precio_prod, stock_prod):
        self.nombre = nombre_prod
        self.precio = precio_prod
        self.stock = stock_prod

    def __str__(self):
        print(f"Nombre del Producto: {self.nombre} | Precio: S/ {self.precio} | Stock: {self.stock}")