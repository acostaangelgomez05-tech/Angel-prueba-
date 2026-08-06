print("bienvenidos a mi agsinador de becas")

promedio = float(input("promedio: "))
ingresos = float(input("ingresos familiares: $"))
distancia = float(input("distancia a la universidad (km):"))

if promedio > 90 and ingresos < 500:
    print("beca completa")
elif promedio > 80 and distancia > 50:
    print("beca transporte")
else:
    print("no aplica para beca")