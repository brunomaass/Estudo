# Programa para resolver o exercício "Bolinhas de Natal"
import math

bolinhas = int(input()) # Recebe o valor digitado pelo usuário
galhos = int(input()) # Recebe o valor digitado pelo usuário

quantGalhos = galhos * 0.5 # Descobre a quanto é a metade dos galhos

total = quantGalhos - bolinhas # Descobre a diferença entre o total de bolinhas e a metade das quant de galhos
totalArredondado = math.floor(total) # Arredonda a quantidade para baixo com a biblioteca math

comp = bolinhas * 2 # Descobre a quantitadde de bolinhas é igual a quantidade da metadde dos galhos

# condicional pa ra saida de acordo com o exercício
if comp >= galhos:
    print("Amelia tem todas as bolinhas!")
else:
    print(f"Faltam {totalArredondado:.0f} bolinhas(s)")