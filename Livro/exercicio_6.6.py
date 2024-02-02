#Programa para resolver exercício enquete

pessoas = {
    'Bruno': 'python',
    'joão': 'c', 
    'marcos': 'c#', 
    'maria': 'Rubby',
    'carlos': 'javascript',
    'anonio': 'java'
    
}

respondido = {
    'maria': 'Rubby',
    'carlos': 'javascript',
    'anonio': 'java'
}

for nome in pessoas.keys():
    if nome in respondido:
        print(f'{nome.title()}, obrigado por responder a pesquisa!')
        print("-" * 30)
   
for nome in pessoas.keys():
    if nome not in respondido:
        print(f'{nome.title()} por favor responda a pesquisa!')
        print("-" * 30)