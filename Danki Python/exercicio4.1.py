'''01 - Escreva um programa em que sejam lidos dois números reais,
X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas.
No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne
 a média aritmética deles;'''


def maior_numero(x, y):
    if x > y:
        return x
    else:
        return y


x = input('Digite um número: ')
y = input('Agora digite outro número: ')

print(f'O maior número é: {maior_numero(x, y)}')


def media_numeros(x, y):
    return (int(x) + int(y)) / 2


print(f'\nA média aritmmética entre os números é: {media_numeros(x, y)}')
