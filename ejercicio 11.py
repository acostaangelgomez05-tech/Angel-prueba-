print("bienvenidos a mis impuestos progresivos")

salario = float(input("salario anual: $"))

if salario <= 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = (salario - 10000) * 0.10
else:
    impuesto = (20000 * 0.10) + ((salario - 30000) * 0.20)

print(f"impuesto a pagar: ${impuesto:.2f}")