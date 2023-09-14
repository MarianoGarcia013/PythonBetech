print('Bienvenidos a la calculadora')
salir = input('Para salir escribe Salir')
n1 = input('Ingrse un numero')
n2 = input('Ingrese otro numero')
print('Las operacioes son suma, multi, resta y div')
operacion = input('')
resultado = 0
while salir == 'Salir' :
    if operacion == 'suma':
        resultado = n1 + n2
        print(resultado)
    elif operacion == 'multi':
        resultado = n1 * n2
        print(resultado)
    elif operacion == 'resta':
        operacion = n1 - n2
        print(resultado)
    elif operacion == 'div':
        operacion = n1 / n2
        print(resultado)

        