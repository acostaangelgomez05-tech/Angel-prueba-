print("bienvenidos a mi conversor de minutos y horas a segundos")

print("ingrese la cantidad de minutos que desea convertir a segundos")
minutos = int(input())

print("ingrese la cantidad de horas que desea convertir a segundos")
horas = int(input())

segundos = minutos * 60 + horas * 3600
print("la cantidad de segundos es:", segundos)