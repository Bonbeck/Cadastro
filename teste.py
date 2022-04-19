import json

with open("teste.json", "r+") as f:
    #json.dump("{}", f)
    d = json.load(f)
print(d)
if "abc" in d:
    print("logado")
if "abc" in "abacaxiabc":
    print("logado")