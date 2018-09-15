import requests as req
import json

url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{0}/current?token={1}"
url = url.format("3477","742fc47f17ced614c3f4b9da2957d3a6")
retorno = req.api.get(url).json()

url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{0}/current?token={1}"
url = url.format("7140","742fc47f17ced614c3f4b9da2957d3a6")
retorno2 = req.api.get(url).json()

url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{0}/current?token={1}"
url = url.format("8050","742fc47f17ced614c3f4b9da2957d3a6")
retorno3 = req.api.get(url).json()
print(retorno)
print(retorno2)
print(retorno3)
