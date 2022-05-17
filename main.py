from cadastro import Cadastro, Login
from email_senha import EmailSenha
import json, random, string


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
            codigo = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
            dados = Login().retorna_email()
            retorno_email = EmailSenha(dados[0]).envia(codigo)
            print(retorno_email)
            if "não existe" in retorno_email:
                pass
            else:
                autenticacao = input("digite o codigo enviado no seu email: ")
                if autenticacao == codigo:
                    senha = input("digite sua nova senha: ")
                    confirmacao = input("confirme sua nova senha: ")
                    if senha == confirmacao:
                        Cadastro(dados[0], senha, dados[1], dados[2], dados[3], True).armazena()
                    else:
                        for i in range(2):
                            senha = input("digite sua nova senha: ")
                            confirmacao = input("confirme sua nova senha: ")
                            if senha == confirmacao:
                                Cadastro(dados[0], senha, dados[1], dados[2], dados[3], True).armazena()
                                break
                else:
                    i = 0
                    while autenticacao != codigo:
                        i += 1
                        autenticacao = input("digite o codigo enviado no seu email: ")
                        if i == 4:
                            break
            break
    if login == "logado":

        print("_"*50, "\n")
        print("1. consultar\n2. atualizar")
        print("_"*50, "\n")
        option = input("digite a opção: ")

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