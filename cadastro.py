import random, json
from textwrap import indent

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

        with open("db.json", "r+", encoding="utf8") as db:
            dados.update(base)
            db.seek(0)
            json.dump(dados, db, ensure_ascii=False, indent=2)
        return 