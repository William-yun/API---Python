import requests as Req

Url = "http://localhost/alunos/cadastrar"
All = {"Nome":"William", "Ra":1701666, "Ativo":"Ativo"}

Retorno = Req.api.post(Url, json=All).json()
print(Retorno)
