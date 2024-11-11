from typing import List
from producto.producto import Producto

class Supermercado:
    def __init__(self):
        self.lista_productos: List[Producto] = []

    def registrar_producto(self, producto: Producto):
        self.lista_productos.append(producto)
        print(f"Producto {producto.nombre} registrado con éxito.")

    def mostrar_productos(self):
        if not self.lista_productos:
            print("No hay productos registrados.")
            return

        for producto in self.lista_productos:
            print(producto.mostrar_detalles())
        
        # Mostrar el valor total de todos los productos
        print(f"Valor neto total de todos los productos: ${self.calcular_valor_total_productos():.2f}")

    def calcular_valor_total_productos(self) -> float:
        valor_total = sum(producto.calcular_valor_total() for producto in self.lista_productos)
        return valor_total        