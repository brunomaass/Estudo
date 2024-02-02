# Programa para resolver o exercício "Área"

entrada = input()

pi = 3.14159

numeros = entrada.split()

triangulo = float(numeros[0]) * float(numeros[2]) / 2
circulo = pi * float(numeros[2]) * float(numeros[2])
trapezio = (float(numeros[0]) + float(numeros[1])) * float(numeros[2]) / 2
quadrado = float(numeros[1]) * float(numeros[1])
retangulo = float(numeros[0]) * float(numeros[1])

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
