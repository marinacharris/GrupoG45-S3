datosPersonales = {
    'nombre': 'Carlos',
    'edad': 40,
    'id': 32658741,
    'telefono': 3015874896,
    'direccion': 'Calle 75 89 25',
    'Permiso_AR': True,
    'hijos': {'hijo1': 'María', 'hijo2': 'Sofía'}
}

for i in datosPersonales: # la variable i toma los valores de las llaves
    print(i)

for i in datosPersonales:
    print(datosPersonales[i]) # Se imprimen los valores de cada llave

# métodos
#copy
datosPersonales2 = datosPersonales.copy()
print(datosPersonales2)
#clear
datosPersonales2.clear()
print(datosPersonales2)
#pop, borra una llave y devuelve su valor
print(datosPersonales.pop('hijos'))
print(datosPersonales.keys())
#print(datosPersonales[1]), los índices numéricos no funcionana como llaves
#get, obtiene un valor de una llave
print(datosPersonales.get('nombre'))
print(datosPersonales['nombre'])
print(datosPersonales.setdefault('nombre'))
#setdefault
datosPersonales.setdefault('email', 'prueba@gmail.com')
datosPersonales['cargo'] = 'Operario'
print(datosPersonales)


 