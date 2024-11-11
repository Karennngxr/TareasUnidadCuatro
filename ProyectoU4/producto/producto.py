from producto.excepciones import ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        if not nombre:
            raise ProductoInvalidoException()
        if precio <= 0:
            raise PrecioInvalidoException()
        if cantidad_disponible < 0:
            raise CantidadInvalidaException()
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
    
    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad_disponible
    
    def mostrar_detalles(self) -> str:
        valor_total = self.calcular_valor_total()
        return (f"Nombre: {self.nombre}, Precio: ${self.precio}"
                f"Cantidad: {self.cantidad_disponible}, Valor Total: ${valor_total}")