print("bienvenidos a mi sistema de multa de trafico")

limite =float(input("limite de velocidad: "))
actual =float(input("velocidad actual: "))

if actual <= 0 or actual < 0:
    print("error los valores de velocidad deben ser mayor a 0")
elif actual > limite:
    exceso = actual - limite
    multa = 50 +(exceso * 5)
    print(f"multa por exceso de velocidad ({exceso:.1f} km/h de exceso): ${multa:.2f}")
else:
    print("velocidad permitida sin multa por exceso de velocidad")