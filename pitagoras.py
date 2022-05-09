#Diseñe un progrma para calcular la hipotenusa de un triángulo rectángulo
#datos de entrada: a y b (cateto opuesto y cateto adyacente)
#datos de salida: h, hipotenusa

#operadores aritméticos
# + - * / %(módulo) **(potencia) //(división entera)
# P paréntesis
# E exponentes          4+5*3 = 19, esto es correcto
# M Multiplicación            =  27, esto esta incorrecto; No!
# D División            
# A Adición
# S Sustracción 

from cmath import pi


def pitagoras(a,b):
    h = (a**2 + b**2)**0.5 
    return h

a = int(input("Digite número 1:\n"))
b = int(input("Digite número 2:\n"))
print(pitagoras(a,b))