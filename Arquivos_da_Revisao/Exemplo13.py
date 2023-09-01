import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('dados.csv', sep=';')

# Extrair os dados das colunas "nota1" e "nota2" em listas
peso = df['peso'].tolist()
altura = df['altura'].tolist()

print('Lista dos pesos:', peso)
print('Lista das alturas:', altura)

print('Lista das alturas:', len(altura))
print('Lista das alturas:', min(altura))
print('Lista das alturas:', max(altura))
print('Lista das alturas:', sum(altura))
