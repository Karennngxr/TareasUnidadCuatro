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

        
        
#def calcular_valor_total(self):
#    return None
#
#def mostrar_detalles(self):
#    return None



    
        
        