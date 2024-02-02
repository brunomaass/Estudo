# Programa para resolver o exercicio "Conversão de Tempo"

entrada = int(input())

horas = entrada // 3600
minutos = (entrada % 3600) // 60
resto_Minutos = (entrada % 3600) % 60

segundos = 0
if resto_Minutos >= 0 and resto_Minutos <= 59:
    segundos = resto_Minutos

print(f"{horas}:{minutos}:{segundos}")
