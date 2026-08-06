# cajero automatico

saldo = 5000.0
opcion = ""

while opcion != "3":
    print("\n--- cajero automatico ---")
    print("1) consultar saldo")
    print("2) retirar dinero")
    print("3) salir")
    opcion = input("selecciona una opción (1-3): ")

    if opcion == "1":
        print(f"\n💵 Tu saldo actual es: ${saldo:.2f}")
        
    elif opcion == "2":
        monto = int(input("\n¿cuánto deseas retirar? (múltiples de 100): "))
        
        # Validación: Múltiplo de 100, positivo y con fondos suficientes
        while monto <= 0 or monto % 100 != 0 or monto > saldo:
            if monto > saldo:
                print("❌ saldo insuficiente.")
            else:
                print("❌ El monto debe ser un entero positivo múltiplo de 100.")
            monto = int(input("Ingresa un monto válido: "))

        # Descuento del saldo
        saldo -= monto
        billetes_100 = monto // 100
        
        print("\nDispensing cash...")
        for _ in range(billetes_100):
            print("💵 Entregando billete de $100")
            
        print(f"¡Retiro exitoso! Saldo restante: ${saldo:.2f}")

    elif opcion == "3":
        print("\nGracias por usar el cajero automático. ¡Hasta luego! 👋")
    else:
        print("\nOpción no válida. Intenta de nuevo.")

