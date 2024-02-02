'''02 - Escreva uma função de potenciação, em que os dados de entrada são:
 base e expoente (inteiros).'''


def potecia_numeros(x, y):
    return x ** y


x = int(input('Digite o número: '))
y = int(input('Digite a potência: '))

print(f'{x} elevado à {y} é: {potecia_numeros(x,y)}')
