class Perro:
    patas = 4 
    def __init__(self, nombre, edad): 
        self.nombre = nombre # Propiedad dentro del constructor
        self.edad = edad          
    
    @classmethod # Es para agregarle un metodo a la clase
    def habla(self):
        print("guau")

    @classmethod
    def factory(cls): # Es una fabrica de objeto
        return cls('juanito',3) 
    

mi_perro = Perro
Perro.factory() # Aqui ya se obtiene un objeto 
