# Programa para resolver o exercício "Idade em Dias"

entrada = int(input())

anos = entrada // 365

meses = (entrada % 365) // 30

dias = (entrada % 365) % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
