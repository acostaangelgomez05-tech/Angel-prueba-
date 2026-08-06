print("bienvenidos a mi facturador electrico escalonado")

consumo = float(input("Consumo en KWh: "))

if consumo <= 100:
    factura = consumo * 0.50
elif consumo <= 300:
    factura = (100 * 0.50) + ((consumo - 100) * 1.00)
else:
    factura = (100 * 0.50) + (200 * 1.00) + ((consumo - 300) * 1.50)

print(f"Factura: ${factura:.2f}")