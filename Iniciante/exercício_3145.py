
# Resposta do exercício "Uma Jornada Inesperada"

lista = input() # Recebe os dados
numeros = lista.split() # Converte em lista e ignora os espaços

covert = int(numeros[1]) / (int(numeros[0]) + 2) # Calcula de acordo com a fórmula apresentada


print(f"{covert:.2f}") # Saída com 2 casa decimais
