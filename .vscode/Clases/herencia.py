class Model():
    tabla = False
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")
    
    def guardar(self):
        print(f"guardando {self.tabla} en BBDD")
    
    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla")

class Usuario(Model):
    tabla = 'Usuario'

usuario = Usuario()

usuario.guardar()

    