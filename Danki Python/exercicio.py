
def encaixa_numeros(entrada1, entrada2):
    entrada1 = str(entrada1)
    entrada2 = str(entrada2)

    if entrada1.endswith(entrada2):
        print('encaixa')
    else:
        print('não encaixa')

primeira_entrada = int(input())
for i in range(primeira_entrada):
    a = input().split()
    a0 = a[0]
    a1 = a[1]

    encaixa_numeros(a0, a1)
