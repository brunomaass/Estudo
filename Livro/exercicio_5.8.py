# Escrever uma saudação para cada usuário de uma lista e uma saudação especial para o admin

usuarios = ["bruno", "jose", "marcos", "carlos", "admin"]

if usuarios == []:
    print("Precisamos encontrar alguns usuários!")
else:
    for usuario in usuarios:
        if usuario == "admin":
            print(f"Olá {usuario} seja bem vindo!, gostaria de um relatório completo?")
        else:
            print(f"Olá {usuario} seja bem vindo!")