class Perro:
    patas = 4 # variable de clase
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre # Propiedad dentro del constructor
        self.edad = edad
        
    
    def habla(self): # Para ingresar a las propiedades dentro de la clase es con self
        print(f"el perro se llama {self.nombre}, y tiene {self.edad}")

Perro.patas = 3 # Se puede cambiar los atributos mas adelante
# Esto solo lo cambia para la instancia y no para la clase

mi_perro = Perro("chanchito",1) # se tiene que pasar los argumentos para crearla
mi_perro2 = Perro("chanchito",1)
print(Perro.patas)
