#  adivinanza de numero con ronda 

numero_oculto = 18
jugar = "s"

# Bucle principal para repetir el juego
while jugar.lower() == "s":
    adivinado = False
    print("\n--- ¡Nuevo juego! Tienes 3 intentos ---")
    
    # 3 Intentos de juego
    for intento in range(1, 7):
        numero_usuario = int(input(f"Intento {intento}/3 - Ingresa tu número: "))
        
        if numero_usuario == numero_oculto:
            print("🎉 ¡Felicidades! Adivinaste el número.")
            adivinado = True
            break
        elif numero_usuario < numero_oculto: 
            print("El número oculto es mayor 📈")
        else:
            print("El número oculto es menor 📉")
            
    if not adivinado:
        print(f"❌ Agotaste tus intentos. El número oculto era: {numero_oculto}")
        
    jugar = input("\n¿Quieres volver a jugar? (s/n): ")

print("¡Gracias por jugar! 👋")
