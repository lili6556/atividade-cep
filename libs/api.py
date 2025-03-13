import requests as req
import json

def via_cep(cep):

    retorno = req.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(retorno)
    return json.loads(retorno.text)