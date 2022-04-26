import email
from operator import truediv
import random, json
from RSA import main

class Cadastro():
    def __init__(self):
        self.nickname = input("digite seu apelido: ")
        self.senha = input("digite sua senha: ")
        self.email = input("digite seu email: ")

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
        base[id]["email"] = self.email

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
        self.dados = json.load(self.bd)
        self.nickname = input("nickname: ")

    def autenticacao(self):
        senha = input("senha: ")
        validacao = False

        for id in self.dados:
            if senha == self.dados[id]["senha"]:
                validacao = True
                if self.nickname == self.dados[id]["nickname"]:
                    with open(f"{self.nickname}_privkey.txt", "r", encoding="utf8") as pk:
                        private_key = pk.read()
                        priv_key = private_key.split(",")[1]
                    pub_key = str(self.dados[id]["chave publica"][1])
                    #print(type(pub_key), type(priv_key))
                    if pub_key == priv_key:
                        return "logado"
            else:
                validacao = False
        if validacao == False:
            return "senha incorreta"
    
    def retorna_email(self):
        for id in self.dados:
            if self.nickname == self.dados[id]["nickname"]:
                return self.dados[id]["email"]

        