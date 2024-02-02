# exercício para percorrer dicionario e localizar um item e mostrar uma frase

rios = {'nilo': 'egito',
        'amazonas': 'brasil',
        'mississipi': 'estados unidos',
        'danúbio': 'alemanha'

        }

print("-" * 30)

for chave, valor in rios.items():
    if chave == 'amazonas':
        print(f'O rio {chave.title()} é o maior rio do {valor.title()}')
    elif chave == 'nilo':
        print(f"O rio {chave.title()} é o rio mais extenso "
              f"do mundo e passa pelo {valor.title()}")
    elif chave == 'mississipi':
        print(f"O rio {chave.title()} corta a maior parte do centro "
              f"dos {valor.title()}")
    elif chave == 'danúbio':
        print(f"O rio {chave.title()} passa por uma região "
              f"extremamente bonita da {valor.title()}")

print("-" * 15 + "Rios" + "-" * 15)

for rio in rios.keys():
    print(rio.title())

print("-" * 15 + "Países" + "-" * 15)

for rio in rios.values():
    print(rio.title())

print("-" * 30)
