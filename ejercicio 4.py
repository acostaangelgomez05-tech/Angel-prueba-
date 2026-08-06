print("bienvenidos a mi sistema de descuento de edades")
print("ingrese su edad ")
edad = int(input())
if edad < 18:
    print("usted es menor de edad, no tiene descuento") 
elif edad >= 18 and edad <= 60:
    print("usted tiene un descuento del 20%")
    tiene = input("su descuento de entrada es de 10$")
else:
    print("usted tiene un descuento del 30%")
    tiene = input("su descuento de entrada es de 15$")
print("gracias por usar nuestro sistema de descuento de edades")
print("vuelva pronto")