# clasificador numerico

cantidad = int(input("¿cuántos números deseas evaluar?: "))
while cantidad < 1:
    print("Debes evaluar al menos 1 número.")
    cantidad = int(input("¿cuántos números deseas evaluar?: "))

positivos = 0
negativos = 0
ceros = 0

# Solicitud e incremento de contadores
for i in range(1, cantidad + 1):
    num = float(input(f"numero {i}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print("\n--- resumen ---")
print(f"positivos: {positivos}")
print(f"negativos: {negativos}")
print(f"ceros: {ceros}")

