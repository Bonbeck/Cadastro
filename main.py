from cadastro import Cadastro, Login
import json

login = False
cadastro = False
opcao = input("1. login\n2. cadastrar ")

if opcao == "1":
    login = Login().autenticacao()
    tentativas = 0
    while login == "senha incorreta":
        print("senha incorreta")
        login = Login().autenticacao()
        tentativas += 1
        if tentativas == 2:
            break
    if login == "logado":
        option = input("digite a opção: ")

        print("_"*50, "\n")
        print("1. consultar\n2. atualizar")
        print("_"*50, "\n")

        if option == "1":
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
            #to do: atualizar()
    

elif opcao == "2":
    Cadastro().armazena()

#usuario logado
