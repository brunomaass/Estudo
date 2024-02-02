# Programa para resolver o exercício "Teste de Seleção"

entrada = input()

numeros = entrada.split()

convert = [int(i) for i in numeros]

primeira_condicao = ""
if convert[1] > convert[2] and convert[3] > convert[0]:
    primeira_condicao = "sim"
else:
    primeira_condicao = "nao"

segunda_condição = ""
if (convert[2] + convert[3]) > (convert[0] + convert[1]) and ((convert[0] and convert[1]) > 0):
    segunda_condição = "sim"
else:
    segunda_condição = "nao"

terceira_condicao = ""
if (convert[2] > 0 and convert[3] > 0):
    terceira_condicao = "sim"
else:
    terceira_condicao = "nao"

quarta_condicao = ""
if convert[0] % 2 == 0:
    quarta_condicao = "sim"
else:
    quarta_condicao = "nao"

teste1 = ""
if primeira_condicao == "sim" and segunda_condição == "sim":
    teste1 = "sim"
else: 
    teste1 = "nao"

tste2 = ""
if terceira_condicao == "sim" and quarta_condicao == "sim":
    teste2 = "sim"
else:
    teste2 = "nao"

if teste1 == "sim" and teste2 == "sim":
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
