# Realice un programa que lea el código numérico de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario y debe permitir consultar un producto 
# por su llave.
def crear(productos):
    codigo = int(input('Digite el código\n'))
    nombre = input('Digite el nombre del producto\n')
    precio = int(input('Digite el precio unitario del producto\n'))
    cantidad = int(input('Digite la cantidad del producto\n'))
    productos.setdefault(codigo,[nombre, precio, cantidad])
    return productos
    
def mostrar():
    pass

def consultar():
    pass


continuar = 's'
productos = {}
while continuar == 's' or continuar == 'S':
    print('MENU')
    print('1. Crear producto')
    print('2. Mostrar productos ')
    print('3. Consultar producto')
    opcion = int(input(f'Digite una de las tres opciones [1/2/3]:\n'))
    if opcion == 1:
        crear(productos)
        print('Producto creado')
        print(productos)
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        consultar()
    else:
        print('Digite una opción valida')

    continuar = input('Presione "s" para continuar o cualquier letra para salir\n')