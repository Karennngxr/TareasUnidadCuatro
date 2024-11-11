class ProductoInvalidoException(Exception):
    def __init__(self, mensaje="El nombre del producto no puede estar vacío."):
        super().__init__(mensaje)

class PrecioInvalidoException(Exception):
    def __init__(self, mensaje="El precio debe ser un valor positivo mayor que cero."):
        super().__init__(mensaje)

class CantidadInvalidaException(Exception):
    def __init__(self, mensaje="La cantidad debe ser un valor positivo."):
        super().__init__(mensaje)
