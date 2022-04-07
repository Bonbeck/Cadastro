from cadastro import Cadastro
import json

print("_"*50, "\n")
print("1. cadastrar\n2. consultar\n3. atualizar")
print("_"*50, "\n")

option = input("digite a opção: ")

if option == "1":
    Cadastro().armazena()
elif option == "2":
    with open("db.json", "r", encoding="utf8") as db:
        data = json.load(db)
    print("_"*50, "\n")
    print("1. consultar base\n2. consultar usuario")
    print("_"*50, "\n")

    option = input("digite a opção: ")

    if option == "1":
        for id in data:
            print(id, data[id]["nickname"])
    elif option == "2":
        user = input("qual usuário você deseja consultar? ")
        for id in data:
            for user_db in data[id]:
                if user in data[id][user_db]:
                    print(user)

    #    print(data)
    