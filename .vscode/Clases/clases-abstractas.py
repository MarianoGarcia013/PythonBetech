from abc import ABC, abstractclassmethod

class Model(ABC):
    @property
    @abstractclassmethod
    def tabla(self):
        pass

    def buscar_por_id(self, _id):
        print (f"buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = 'Usuario'

    def guardar(self):
        print(f"guardando usuario")


usuario = Usuario()
