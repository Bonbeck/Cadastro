from operator import truediv
import random, json
from RSA import main

class Cadastro():
    def __init__(self):
        self.nickname = input("digite seu apelido: ")
        self.senha = input("digite sua senha: ")

    def armazena(self):
        try:
            db = open("db.json", "r")
            print("lendo a base")
        except FileNotFoundError:
            db = open("db.json", "w")
            print("arquivo criado")
            db.write("{}")
            db.close()
            db = open("db.json", "r")
        
        dados = json.load(db)

        base = {}
        id = random.randint(0, 1000)
        
        while id in dados:
            id = random.randint(0, 1000)
        #if id not in dados:
        #    print("nao existe o id")
        #else:
            #print("existe na base")

        base[id] = {}
        base[id]["nickname"] = self.nickname
        base[id]["senha"] = self.senha
        base[id]["chave publica"] = main(self.nickname)

        with open("db.json", "r+", encoding="utf8") as db:
            dados.update(base)
            db.seek(0)
            json.dump(dados, db, ensure_ascii=False, indent=2)
        return

class Login():
    def __init__(self):
        try:
            self.bd = open("db.json", "r", encoding="utf8")
        except:
            Cadastro()

    def autenticacao(self):
        dados = json.load(self.bd)
        nickname = input("nickname: ")
        senha = input("senha: ")
        validacao = False

        for id in dados:
            if senha == dados[id]["senha"]:
                validacao = True
                if nickname == dados[id]["nickname"]:
                    with open(f"{nickname}_privkey.txt", "r", encoding="utf8") as pk:
                        private_key = pk.read()
                        priv_key = private_key.split(",")[1]
                    pub_key = str(dados[id]["chave publica"][1])
                    #print(type(pub_key), type(priv_key))
                    if pub_key == priv_key:
                        return "logado"
            else:
                validacao = False
        if validacao == False:
            return "senha incorreta"
            