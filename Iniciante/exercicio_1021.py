# Programa para resolver o exercício "Notas e Moedas"

entrada = input()
# Converte para float e calcula quanta notas de 100 e o resto
x1 = float(entrada) // 100
y1 = float(entrada) % 100
# Calcula a quantidade das notas de 100
nota100 = x1

# Armazena o valor das notas e o resto depois das comparações
nota50 = 0
resto50 = 0

nota20 = 0
resto20 = 0

nota10 = 0
resto10 = 0

nota5 = 0
resto5 = 0

nota2 = 0
resto2 = 0

nota1 = 0
resto1 = 0

#Calculo das Moedas abaixo de R$ 1.00
moeda50 = 0
resto_moeda50 = 0

moeda25 = 0
resto_moeda25 = 0

moeda10 = 0
resto_moeda10 = 0

moeda5 = 0
resto_moeda5 = 0

moeda1 = 0




if y1 <= 99:
    nota50 = y1 // 50
    resto50 = y1 % 50
if resto50 < 50:
    nota20 = resto50 // 20
    resto20 = resto50 % 20
if resto20 < 20:
    nota10 = resto20 // 10
    resto10 = resto20 % 10
if resto10 < 10:
    nota5 = resto10 // 5
    resto5 = resto10 % 5
if resto5 < 5:
    nota2 = resto5 // 2
    resto2 = resto5 % 2
if resto2 < 2:
    nota1 = resto2 // 1
    resto1 = resto2 % 1
if resto1 < 1:
    moeda50 = resto1 // 0.5
    resto_moeda50 = resto1 % 0.5
if resto_moeda50 < 0.50 :
    moeda25 = resto_moeda50 // 0.25
    resto_moeda25 = resto_moeda50 % 0.25
if resto_moeda25 < 0.25 :
    moeda10 = resto_moeda25 // 0.10
    resto_moeda10 = resto_moeda25 % 0.10
if resto_moeda10 < 0.10 :
    moeda5 = resto_moeda10 // 0.05
    resto_moeda5 = resto_moeda10 % 0.05
if resto_moeda5 < 0.05:
    moeda1 = resto_moeda5 // 0.009
   

    

print("NOTAS:")
print(int(nota100), "nota(s) de R$ 100.00")
print(int(nota50), "nota(s) de R$ 50.00")
print(int(nota20), "nota(s) de R$ 20.00")
print(int(nota10), "nota(s) de R$ 10.00")
print(int(nota5), "nota(s) de R$ 5.00")
print(int(nota2), "nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{nota1:.0f} moeda(s) de R$ 1.00")
print(f"{moeda50:.0f} moeda(s) de R$ 0.50")
print(f"{moeda25:.0f} moeda(s) de R$ 0.25")
print(f"{moeda10:.0f} moeda(s) de R$ 0.10")
print(f"{moeda5:.0f} moeda(s) de R$ 0.05")
print(f"{moeda1:.0f} moeda(s) de R$ 0.01")
