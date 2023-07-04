import requests

nomeURL = input("Digite o nome do deputado: ")
api_url = "https://dadosabertos.camara.leg.br/api/v2/deputados?nome=" + nomeURL+ "&ordem=ASC&ordenarPor=nome"
response = requests.get(api_url)
print(response.json())

#put response.json in a pandas dataframe
import pandas as pd
dfPolitico = pd.DataFrame(response.json()['dados'])

#print nome and partido and email from dfPolitico
print(dfPolitico[['nome','siglaPartido','email']])









