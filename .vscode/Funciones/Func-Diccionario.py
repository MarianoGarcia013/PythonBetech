def get_productos(**datos):
    print(datos['id'], datos['name'])


get_productos(id= 'id',
              name = 'iPhone',
              desc = 'Esto es un iPhone')