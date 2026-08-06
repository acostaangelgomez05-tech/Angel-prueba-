print("bienvenidos a mi evaluador de rango numerico")
print("ingrese un numero para evaluar su rango")
numero = int(input())
if numero < 0:
    print("el numero es negativo")
elif numero > 0:
    print("el numero es positivo")
else:
    print("el numero es cero")