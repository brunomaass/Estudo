# Programa resolver o exercício "cédulas"

entrada = int(input())

x1 = entrada // 100
y1 = entrada % 100
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

if y1 <= 99:
    nota50 = y1 // 50
    resto50 = y1 % 50
if resto50 <= 49:
    nota20 = resto50 // 20
    resto20 = resto50 % 20
if resto20 <= 19:
    nota10 = resto20 // 10
    resto10 = resto20 % 10
if resto10 <= 9:
    nota5 = resto10 // 5
    resto5 = resto10 % 5
if resto5 <= 4:
    nota2 = resto5 // 2
    resto2 = resto5 % 2
if resto2 <= 2:
    nota1 = resto2 // 1
    resto1 = resto2 % 1

print(entrada)
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")
