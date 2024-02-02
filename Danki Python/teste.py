

def transformar_binario(numero):

    numero = int(numero)
    return bin(numero)[2:]

def contador_zeros(binario):
    binario = str(binario)
    contador_zero = 0
    contador_maximo = 0
    dentro_de_um_espaço = False

    for i in binario:
        if i == "1":
            dentro_de_um_espaço = True
            contador_maximo = max(contador_maximo, contador_zero)
            contador_zero = 0
        elif dentro_de_um_espaço:
            contador_zero += 1
        

    return contador_maximo

binario = transformar_binario(32)

print(contador_zeros(binario))
print(binario)