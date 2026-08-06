print("bienvenidos a mi simulador de cajero automatico")
saldo = 1000
retiro = float(input("monto a retirar: $"))

if retiro <= saldo and retiro % 10 == 0:
    saldo_final = saldo - retiro
    print(f"retiro exitoso. saldo restante $ {saldo_final}")

else:
    if retiro > saldo:
         print("error: saldo insuficiente")     
    if retiro % 10 != 0:
         print ("el monto debe ser multiplo de 10")

