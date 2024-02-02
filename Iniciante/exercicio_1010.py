# Programa para resolver o exercício "Cálculo Simples"

entrada1 = input() # Primeira linha com entrada de dados

numeros1 = entrada1.split() # Converte em lista e ignora os espaços

entrada2 = input() # Segunda linha com entrada de dados

numeros2 = entrada2.split() # Converte em lista e ignora os espaços


valor1 = int(numeros1[1]) * float(numeros1[2]) # Multiplica a quantidade pelo valor de acordo com a ordem do exercício

valor2 = int(numeros2[1]) * float(numeros2[2]) # Multiplica a quantidade pelo valor de acordo com a ordem do exercício

total = valor1 + valor2 # Obtem o valor total 

print(f"VALOR A PAGAR: R$ {total:.2f}")