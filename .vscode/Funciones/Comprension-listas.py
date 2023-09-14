usuarios = [['Juan', 3],
            ['Lucio',1],
            ['Ramon',2],
            ['Robert',4]]

# map
# nombres = [usuario[0] for usuario in usuarios]

#filtrar - filter
nombres = [usuario for usuario in usuarios if usuarios[1]]
#print(nombres)

#set significa grupo o conunto
primer = {1,2,3,4}
segundo = [3,4,5]
segundo = set(segundo)

print(primer | segundo) # agrega los de arriba y borra los repetido
print(primer & segundo) # agrega todos junto con los repetidos
print(primer - segundo)
print(primer ^ segundo) # Solo elimina los duplibcados
if 5 in segundo:
    print('Hola mundo')


#Diccionarios
punto = {'x':25, 'y': 50}
print(punto)
print(punto['x'])
print(punto['y'])

punto['z'] = 45 # Agrega uno mas al diccionario
print(punto) 

for llave, valor in punto.items():
   print(llave,valor)