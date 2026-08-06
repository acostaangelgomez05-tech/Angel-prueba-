print("bienvenidos a mi categorizador de triangulo")

lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))

if lado1 == lado2 and lado2 == lado3:
    print("triangulo equilatero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("triangulo isosceles") 
else:  
    print("triangulo escaleno")