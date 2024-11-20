print("Calculadora")
print()

numero_uno = int(input("Ingresa el primer numero:"))
numero_dos = int(input("Ingrese el segundo numero:"))


Operacion = input(" Introducce la operacion que deseas hacer (suma, resta, multiplicacion, division): ")
if Operacion == "suma":
    suma = numero_uno + numero_dos
    print("El resultado de la suma es: ", round(suma,2))
elif Operacion == "resta":
    resta = numero_uno - numero_dos
    print("Elresultado de la resta es: ", round(resta, 2))
elif Operacion == "multiplicacion":
    multiplicacion = numero_uno * numero_dos
    print("El resultado de la multiplicacion es:", round(multiplicacion,2))
elif Operacion == "division": 
    if numero_uno or numero_dos==0:
       print("No se puede multiplicar por zero, ingresa otro numero: ")
    else:
        division = numero_uno / numero_dos 
        print("El resultado de la division es:", round(division,2))

