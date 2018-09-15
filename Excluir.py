import requests as Req 

Url = "http://localhost/produto/del/{0}".format("af448dfa-b7b3-11e8-b045-005056c00008")

Retorno = Req.api.delete(Url).json()
print (Retorno)
