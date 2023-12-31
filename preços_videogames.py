# -*- coding: utf-8 -*-
"""Cópia de Preços_Videogames.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZaOvqRL7XFShgpfhiCTb6uAeydxxmvGq
"""

# Este conjunto de dados contém uma lista de jogos com vendas
# superiores a 100.000 cópias. Foi gerado por um scrape de vgchartz.com.

# Análise descritiva, prescritiva, diagnóstica e preditiva.

# Importando bibliotecas:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fazendo upload do arquivo CSV:

from google.colab import files
import io

uploaded = files.upload()

file_name = next(iter(uploaded))

# Carregando o DataSet:

df = pd.read_csv(io.StringIO(uploaded[file_name].decode('utf-8')))

# ANÁLISE EXPLORATÓRIA DOS DADOS:

# Visualizando as primeiras linhas do DataFrame:

df.head()

df.info()

# Fornece informações sobre o tipo de dados de cada coluna
# e se há valores ausentes.

df.describe()

# Mostra as estatísticas descritivas para colunas numéricas.

# Contgem de valores unicos em uma coluna especifíca:

df['Genre'].value_counts()

df['Platform'].value_counts()

df['Publisher'].value_counts()

# Criação de Gráficos:

# Quantidade de Jogos por Plataforma:

plt.figure(figsize=(10, 6))
sns.countplot(y='Platform', data=df)
plt.title('Qtde de Jogos por Plataforma')
plt.xticks(rotation=90)
plt.show()

# Explorando a relação entre duas váriaveis:

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rank', y='Global_Sales', data=df)
plt.show()

# Correlação entre as variáveis:

corr_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True,
            cmap='coolwarm', fmt='.2f',
            linewidths=0.5)
plt.show()

# Este gráfico acima mostrará uma matriz de correlação para variáveis numéricas.

# Total de vendas globais por gênero do game:

plt.figure(figsize=(12, 8))
sns.barplot(x='Global_Sales', y='Genre', data=df, errorbar=None)
plt.title('Vendas Globais por Gênero')
plt.xlabel('Vendas Globais (em milhões)')
plt.ylabel('Gênero')
plt.xticks(rotation=45, ha='right') # Ajusta a rotação dos rótulos para melhorar a leitura.
plt.show()