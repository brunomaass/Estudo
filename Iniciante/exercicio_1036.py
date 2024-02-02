# Programa para resolver o exercício "Fórmula de Bhaskara"

entrada = input()

numeros = entrada.split()

a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])

delta = (b * b) - 4 * a * c

calc_raiz1 = 0
calc_raiz2 = 0
if a == 0 or delta <= 0:
    print("Impossivel calcular")
else:
    calc_raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    calc_raiz2 = (-b - (delta ** 0.5)) / (2 * a) 
    print(f"R1 = {calc_raiz1:.5f}")
    print(f"R2 = {calc_raiz2:.5f}")
