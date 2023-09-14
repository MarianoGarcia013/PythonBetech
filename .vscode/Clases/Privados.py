class Perro:
    patas = 4 
    def __init__(self, nombre, edad): 
        self.__nombre = nombre # Propiedad dentro del constructor
        self.edad = edad  

    def get_nombre(self):
        return self.__nombre # Para que podamos usar la propiedad fuera de la clase
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice hola") 

    @classmethod
    def factory(cls): # Es una fabrica de objeto
        return cls('juanito',3) 
    
perro1 = Perro
print(perro1.__dict__) # Nos muestra todas las propuedades en diccionario

    
           

  