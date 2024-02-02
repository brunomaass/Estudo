# Programa para resolver o exercício "Criptografia"

entrada0 = int(input())

# Verifica o primeiro valor que se refere a quantidade total de entradas de teste
for i in range(0, entrada0):
    
    entrada = input()
    lista = list(entrada)
    
    # Nesta passagem separa os numeros do outros caracteres
    passada1 = []
    for i in lista:
        if i.isalpha():
            passada1.append(ord(i) + 3)
        else:
            passada1.append(ord(i))


    passada1_convertido = []
    for i in passada1:
        passada1_convertido.append(chr(i))

    passada1_convertido = passada1_convertido[::-1]

    meio = len(passada1_convertido) // 2

    for i in range(meio, len(passada1_convertido)):
        passada1_convertido[i] = chr(ord(passada1_convertido[i]) - 1)

    passada1_convertido = "".join(passada1_convertido)
    print(passada1_convertido)



