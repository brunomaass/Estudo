# Programa para resolver o exercício "Revisão de Contrato"

entrada = input().split()

if entrada[0] == "0" and entrada[1] == "0":
    print("")
else:
    entrada1 = [i for i in entrada[0]]
    entrada2 = [i for i in entrada[1]]

    entrada2 = [i for i in entrada2 if i not in entrada1]

    entrada1 = "".join(entrada1)
    entrada2 = "".join(entrada2)

    if entrada2 == "":
        print("0")
    else:
        entrada1 = int(entrada1)
        entada2 = int(entrada2)

    
        intsaida = 0
        if int(entrada2) <= 0:
            saida = int(0)
            print(saida)
        else:
            print(str(entrada2).lstrip("0"))
  