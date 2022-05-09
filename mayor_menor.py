#Realice un programa que lea n numeros enteros y nos diga cuál es el mayor 
#de ellos y cuál es el menor de ellos
# datos entrada: la cantidad de números y los n números
# datos salida: el mayor y el menor


n = int(input("Digite la cantidad de números que desea ingresar\n"))
for i in range(n): #Este for cuenta de 0 hasta n-1
    numero = int(input(f"Ingrese el número {i+1}\n"))
    if i == 0:
        mayor = numero
        menor = numero
    else: 
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
print(f"El mayor de los {n} números ingresados es {mayor}")  
print(f"El menor de los {n} números ingresados es {menor}")      
    


