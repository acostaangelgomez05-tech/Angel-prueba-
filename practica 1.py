# validacion del numero positivo con while

numero = int(input("ingrese un numero positivo"))
while numero <= 0:
    print("error el numero debe ser mayor a cero")
    numero = int(input("ngesa un numero positivo: "))

suma_pares = 0

# Iteración para encontrar y sumar pares
for i in range(1, numero + 1):
    if i % 2 == 0:
        suma_pares += 1
        print(f"La suma de los números pares desde 1 hasta {numero} es: {suma_pares}")