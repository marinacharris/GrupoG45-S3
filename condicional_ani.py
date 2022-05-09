#Realice un programa que convierta notas numéricas en porcentaje a letras,
#según la siguiente informacion:
# 0.0% - 59.99% -> D
# 60.0% - 75.99% -> C
# 76.00% - 85.99% -> B
# 86.00% - 100% -> A 

def notas_letras(nota):
    if nota >= 0 and nota < 60:
        letra = "D"
    elif nota >=60 and nota < 76:
        letra = "C"
    elif nota >=76 and nota < 86:
        letra = "B"
    elif nota >= 86 and nota <=100:
        letra = "A"
    else:
        return f"Digite una nota váilda, entre 0 y 100"
    return letra

try:
    nota = int(input("Digite una nota váilda, entre 0 y 100:\n"))
    print(notas_letras(nota))
except:
    print("Debe digitar solo números")
    