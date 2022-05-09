
try:
    x = int(input("Digite un número entero:\n"))
    print(x)
    print(y)
except ValueError:
    print("solo puede digitar números, no se aceptan letras o símbolos")
except NameError:
    print("Error de definición de variable")
'''
x = int(input("Digite un dato:\n"))
print(x)

'''