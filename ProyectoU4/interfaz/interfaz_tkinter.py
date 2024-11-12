import tkinter as tk
from tkinter import messagebox, ttk
from producto.producto import Producto
from supermercado.supermercado import Supermercado

class SupermercadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermercado")
        self.root.geometry("350x350")
        
        self.root.style = ttk.Style(self.root)
        self.root.style.theme_use("clam")  # Cambia el tema → "clam", "alt", "default", etc.
        
        ttk.Label(self.root, text="Nombre del producto:").grid(row=0, column=0, sticky="e", pady=5)
        self.nombre_entry = ttk.Entry(self.root, width=25)
        self.nombre_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(self.root, text="Precio del producto:").grid(row=1, column=0, sticky="e", pady=5)
        self.precio_entry = ttk.Entry(self.root, width=25)
        self.precio_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.root, text="Cantidad del producto:").grid(row=2, column=0, sticky="e", pady=5)
        self.cantidad_entry = ttk.Entry(self.root, width=25)
        self.cantidad_entry.grid(row=2, column=1, pady=5)
        
        self.registrar_button = ttk.Button(self.root, text="Registrar Producto", command=self.registrar_producto)
        self.registrar_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.mostrar_button = ttk.Button(self.root, text="Mostrar Productos", command=self.mostrar_productos)
        self.mostrar_button.grid(row=4, column=0, columnspan=2, pady=5)
        
        self.calcular_total_button = ttk.Button(self.root, text="Calcular Valor Total", command=self.calcular_valor_total_productos)
        self.calcular_total_button.grid(row=5, column=0, columnspan=2, pady=5)
        
        self.productos_text = tk.Text(self.root, height=8, width=40, state="disabled", bg="#f0f0f0")
        self.productos_text.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.supermercado = Supermercado()

    def registrar_producto(self):
        nombre = self.nombre_entry.get()
        
        try:
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            nuevo_producto = Producto(nombre=nombre, precio=precio, cantidad_disponible=cantidad)
            self.supermercado.registrar_producto(nuevo_producto)
            
            messagebox.showinfo("Registro exitoso", f"Producto '{nombre}' registrado correctamente.")
            
            self.nombre_entry.delete(0, tk.END)
            self.precio_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error de entrada", "Ingresa valores numéricos válidos en precio y cantidad.")
    
    def mostrar_productos(self):
        self.productos_text.config(state="normal")
        self.productos_text.delete(3.0, tk.END)
        
        if not self.supermercado.lista_productos:
            messagebox.showinfo("Productos", "No hay productos registrados.")
        else:
            for producto in self.supermercado.lista_productos:
                detalles = producto.mostrar_detalles() + "\n"
                self.productos_text.insert(tk.END, detalles)
        
        self.productos_text.config(state="disabled")

    def calcular_valor_total_productos(self):
        valor_total = sum(producto.calcular_valor_total() for producto in self.supermercado.lista_productos)
        
        messagebox.showinfo("Valor Total", f"El valor total de todos los productos es: ${valor_total:.2f}")


#import tkinter as tk
#from tkinter import messagebox
#from producto.producto import Producto
#from supermercado.supermercado import Supermercado
#
#class SupermercadoApp:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("Supermercado")
#        
#        tk.Label(self.root, text="Nombre del producto:").grid(row=0, column=0, sticky="e")
#        self.nombre_entry = tk.Entry(self.root)
#        self.nombre_entry.grid(row=0, column=1)
#        
#        tk.Label(self.root, text="Precio del producto:").grid(row=1, column=0, sticky="e")
#        self.precio_entry = tk.Entry(self.root)
#        self.precio_entry.grid(row=1, column=1)
#        
#        tk.Label(self.root, text="Cantidad del producto:").grid(row=2, column=0, sticky="e")
#        self.cantidad_entry = tk.Entry(self.root)
#        self.cantidad_entry.grid(row=2, column=1)
#        
#        self.registrar_button = tk.Button(self.root, text="Registrar Producto", command=self.registrar_producto)
#        self.registrar_button.grid(row=3, column=0, columnspan=2)
#        
#        self.mostrar_button = tk.Button(self.root, text="Mostrar Productos", command=self.mostrar_productos)
#        self.mostrar_button.grid(row=4, column=0, columnspan=2)
# 
#        self.productos_text = tk.Text(self.root, height=10, width=40, state="disabled")
#        self.productos_text.grid(row=5, column=0, columnspan=2, pady=10)
#        
#        self.supermercado = Supermercado()
#        
#        
#
#    def registrar_producto(self):
#        nombre = self.nombre_entry.get()
#        
#        try:
#            precio = float(self.precio_entry.get())
#            cantidad = int(self.cantidad_entry.get())
#            nuevo_producto = Producto(nombre=nombre, precio=precio, cantidad_disponible=cantidad)
#            self.supermercado.registrar_producto(nuevo_producto)
#            
#            # Mostrar mensaje de éxito en ventana emergente
#            messagebox.showinfo("Registro exitoso", f"Producto '{nombre}' registrado correctamente.")
#            
#            # Limpiar campos después de registrar
#            self.nombre_entry.delete(0, tk.END)
#            self.precio_entry.delete(0, tk.END)
#            self.cantidad_entry.delete(0, tk.END)
#        except ValueError:
#            messagebox.showerror("Error de entrada", "Ingresa valores numéricos válidos en precio y cantidad.")
#    
#    def mostrar_productos(self):
#        self.productos_text.config(state="normal")
#        self.productos_text.delete(1.0, tk.END)
#        
#        if not self.supermercado.lista_productos:
#            messagebox.showinfo("Productos", "No hay productos registrados.")
#        else:
#            for producto in self.supermercado.lista_productos:
#                detalles = producto.mostrar_detalles() + "\n"
#                self.productos_text.insert(tk.END, detalles)
#        
#        self.productos_text.config(state="disabled")
#