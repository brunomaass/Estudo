# Programa para resolver exercício "Lanche"

entrada = input().split()

numeros = [int(entrada[0]), int(entrada[1])]

x1 = 4.0
x2 = 4.5
x3 = 5.0
x4 = 2.0
x5 = 1.50

if numeros[0] == 1:
    print(f"Total: R$ {(numeros[1] * x1):.2f}" )
elif numeros[0] == 2:
    print(f"Total: R$ {(numeros[1] * x2):.2f}" )
elif numeros[0] == 3:
    print(f"Total: R$ {(numeros[1] * x3):.2f}" )
elif numeros[0] == 4:
    print(f"Total: R$ {(numeros[1] * x4):.2f}" )
elif numeros[0] == 5:
    print(f"Total: R$ {(numeros[1] * x5):.2f}" )