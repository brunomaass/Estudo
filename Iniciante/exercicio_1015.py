# Programa pra resolver o exercício "Distância Entre Dois Pontos"

import math

entrada1 = input()

numeros1 = entrada1.split()


# Segunda entrada

entrada2 = input()

numeros2 = entrada2.split()

x1 = float(numeros1[0])
x2 = float(numeros2[0])


y1 = float(numeros1[1])
y2 = float(numeros2[1])

calculo = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(f"{calculo:.4f}")

