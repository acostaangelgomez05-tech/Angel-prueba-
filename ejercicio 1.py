print("bienvenidos a mi calculadora de propinas")

print("por favor, ingrese el total de la factura")
total_factura = float (input())

print("por favor, ingrese el porcentaje de propina que desea dejar (por ejemplo, 15 para 15%)")
porcentaje_propina = float (input())

propina = total_factura * (porcentaje_propina / 100)
print("la propina es de:", propina)
