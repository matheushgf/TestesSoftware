import json
import requests

class Aluguel():
    def __init__(self):
        #Define a URL de base da API
        self.URL_BASE = 'https://aluguebug.herokuapp.com/calc'

    def get_request(self, url):
        #Faz a requisição com a URL tratada e retorna em forma de JSON
        try:
            resposta = requests.get(url)
            dados = json.loads(resposta.json())
        except:
            dados = None
        return dados
        
    def calcular_aluguel(self, valor_nominal, dia):
        #Trata os dados passados para gerar a URL completa
        url_completa = self.URL_BASE + '?dados={"valor_nominal":' + str(valor_nominal) + ', "dia":' + str(dia) + '}'
        dados = self.get_request(url_completa)
        return dados['valor_calculado'] if (dados != None) else -1.0
