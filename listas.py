# Las listas son estructuras de datos que se utilian para guardar varios 
# elementos en una sola variable
# Las listas son mutables
# las listas son indexadas 

MarcasCarros = ['Nissan', 'Audi', 'Chevrolet', 'Renault']
print(MarcasCarros[1])
MarcasCarros[1]='Toyota'
print(MarcasCarros[1])

datosPersonales = ['Carlos', 40, 'Medellín', 'Contador', [10, 50, 20]]
print(type(datosPersonales), type(datosPersonales[2]))

for i in datosPersonales:
    print(i)
