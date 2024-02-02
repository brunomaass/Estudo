# Verificando nomes de usuário para ver se está disponível

curret_users = ["Bruno", "José", "Carlos", "Marcos", "Antônio"]
new_users = ["Bruno", "Antônio", "Benedito", "Lucas", "Rafaela"]

curret_users_low = []
for usuarios in curret_users:
    curret_users_low.append(usuarios.lower())

new_users_low = []
for usuarios in new_users:
    new_users_low.append(usuarios.lower())


for curret_users_low in curret_users_low:
    if curret_users_low in new_users_low:
        print("O Nome: " + curret_users_low + " Não podera ser utilizado")

print(30 * "-")

for new_users_low in new_users_low:
    if new_users_low not in curret_users_low:
        print("Nome: " + new_users_low + " adicionado com sucesso")
