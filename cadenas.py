from re import L


animal = "cocodrilo"
print(animal[4])
print(len(animal)) # len en una función que nos devuelve la longitud 
# animal[5]="l", no se puede porque las cadenas son inmutables
animal="elefante"
print(animal)
print(animal.isnumeric())
print(animal[2:4])
print(animal[:5])
print(animal[5:])
print(animal[-2]) # las posiciones negativas van de derecha a izquierda
for i in animal: # i toma los valores de cada posición de la cadena o string
    print(i)
    
for i in range(len(animal)): #i es una variable que va desde 0 hasta la longitud de animal
    print(animal[i])



