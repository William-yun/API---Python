import requests as Req

Url = "http://localhost/alunos/atualizar"
All = {"Id":"a3a3awa3d4a2-n3v5b-8y34-j4h54g-00476c00008", "Nome":"William", "Ra":1701666}

Retorno = Req.api.put(Url, json=All).json()
print(Retorno)
