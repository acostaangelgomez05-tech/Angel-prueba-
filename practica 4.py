# tranformador de texto 

palabra = input("ingresa una palabra: ").strip()

# Validación de palabra no vacía
while len(palabra) == 0:
    print("la palabra no puede estar vacía.")
    palabra = input("ingresa una palabra: ").strip()

VOCALES = "aeiouAEIOUáéíóúÁÉÍÓÚ"

print("\n--- Resultado ---")
# Enumerate nos da la posición (índice) y la letra en cada vuelta
for pos, letra in enumerate(palabra):
    if letra in VOCALES:
        resultado = pos * 3
    else:
        resultado = pos // 2
        
    print(f"Letra '{letra}' (Posición {pos}) -> Valor: {resultado}")