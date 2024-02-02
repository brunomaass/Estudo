# Programa para resolver o exercício "Gasto de Combustível"

tempo = int(input())
velocidade = int(input())

distancia = velocidade * tempo

consumo = distancia / 12

print(f"{consumo:.3f}")
