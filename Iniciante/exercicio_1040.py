# Programa para resolver o exercício "Média 3"

entrada = input().split()

numeros = [float(entrada[0]), float(entrada[1]), float(entrada[2]), float(entrada[3])]
# calcula a média
media = ((numeros[0] * 2) + (numeros[1] * 3) + (numeros[2] * 4) + (numeros[3] * 1)) / (2 + 3 + 4 + 1)

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("aluno reprovado.")   

exame = 0
media_final = 0
if media < 7 and media >= 5:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2
    if media_final >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {media_final}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {media_final}")
