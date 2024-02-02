# Programa para resolver o exercício "Divisores I"

entrada = int(input())

for i in range(1, entrada + 1):
    if entrada % i == 0:
        print(f"{i}")


