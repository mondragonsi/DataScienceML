import requests


nomeURL = input("Digite o nome do deputado: ")
api_url = "https://dadosabertos.camara.leg.br/api/v2/deputados?nome=" + nomeURL+ "&ordem=ASC&ordenarPor=nome"
response = requests.get(api_url)
print(response.json())

#put response.json in a pandas dataframe
import pandas as pd
df = pd.DataFrame(response.json()['dados'])
print(df.head())
print(df.info())

#get nome from df in a variable
nome = df['nome'].values[0]

print(nome)

#print partido from df
print(df['siglaPartido'].values[0])

#print nome and partido and email from df
print(df[['nome','siglaPartido','email']])









