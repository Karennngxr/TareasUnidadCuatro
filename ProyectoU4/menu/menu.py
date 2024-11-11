from producto.producto import Producto
from producto.excepciones import ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException
from supermercado.supermercado import Supermercado

class Menu:
    
    supermercado: Supermercado = Supermercado()
    
    def iniciar_menu(self):
        while True:
            print("---------------- SUPERMERCADO -------------------")
            print("1. Registrar Producto")
            print("2. Mostrar lista total de productos")
            print("3. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                print("Hasta luego")
                break 
            else:
                print("Opción inválida, intenta de nuevo.")
            
    def registrar_producto(self):
        print("\nSeleccionaste registrar un producto.")
        try:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            nuevo_producto = Producto(nombre=nombre, precio=precio, cantidad_disponible=cantidad)
            
            self.supermercado.registrar_producto(nuevo_producto)
        
        except ProductoInvalidoException as e:
            print(f"Error: {e}")
        
        except PrecioInvalidoException as e:
            print(f"Error: {e}")
        
        except CantidadInvalidaException as e:
            print(f"Error: {e}")
        
        except ValueError:
            print("Error: Entrada inválida. Asegúrate de ingresar un número válido para el precio y la cantidad.")


    def mostrar_productos(self):
        print("---- Productos registrados en Supermercado -----")
        self.supermercado.mostrar_productos()
