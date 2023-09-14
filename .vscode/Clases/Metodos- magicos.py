class Perro:
    def __init__(self, nombre, edad): 
        self.nombre = nombre # Propiedad dentro del constructor
        self.edad = edad     
    
    def __str__(self): # Metodos que estan siempre pero no se ven
        return f"Clase perro {self.nombre}"
    
    def habla(self):
        print(f"{self.nombre} dice guau")

miperro = Perro
texto = str(Perro) # Se obtiene la clase escrita por estar en el metodo str