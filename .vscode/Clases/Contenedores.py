class Producto: # Un producto va a estar en una categoria
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio   
    
          
class Categoria:
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    def agregar(self, producto):
        self.productos.append(producto)
    
    def imprimir(self):
        for producto in self.productos:
            print(producto)

martillo = Producto('martillo', 150)
pala = Producto('pala', 100)
bicicleta = Producto('bicicleta', 245)
ferreteria = Categoria('ferreteria', [martillo, pala]) # Le pasamos a la categoria los productos que tiene
ferreteria.agregar(bicicleta) # Se agrego un producto a la categoria
ferreteria.imprimir()