print("validador estrictos de fechas")

dia = int(input("dia: "))
mes = int(input("mes: "))
año = int(input("año: "))

# Validar año
if año <= 0:
    print("Fecha inválida")
else:
    # Validar mes
    if mes < 1 or mes > 12:
        print("Fecha inválida")
    else:
        # Determinar días del mes
        if mes == 2:
            # Febrero - verificar bisiesto
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                dias_max = 29
            else:
                dias_max = 28
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias_max = 30
        else:
            dias_max = 31
        
        # Validar día
        if dia >= 1 and dia <= dias_max:
            print("Fecha válida")
        else:
            print("Fecha inválida")