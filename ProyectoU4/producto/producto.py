from producto.excepciones import ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        if not nombre:
            raise ProductoInvalidoException("El nombre no puede estar vacío.")
        if precio <= 0:
            raise PrecioInvalidoException("El precio debe ser mayor a cero.")
        if cantidad_disponible < 0:
            raise CantidadInvalidaException("La cantidad no puede ser negativa.")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
    
    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad_disponible
    
    def mostrar_detalles(self) -> str:
        valor_total = self.calcular_valor_total()
        return (f"Nombre: {self.nombre}, Precio: ${self.precio}, "
                f"Cantidad: {self.cantidad_disponible}, Valor Total: ${valor_total:.2f}")
