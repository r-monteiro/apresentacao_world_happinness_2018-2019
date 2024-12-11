# -*- coding: utf-8 -*-
"""Cópia de PI TRABALHO FINAL_2023-CERRRRRTINHO

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c9KhiOq7aLTkbJ6HP60MfNa2tswv51BC

**TRABALHO FINAL PROJETO INTEGRADOR**

INTEGRANTES:

- MATEUS NATAN ROES SALGUEIRO;
- PAULO ELIAS TAVARES GENEROZO;
- RAFAEL AUGUSTO MORAES MONTEIRO.
__________________________________________________

**UPLOAD BASE DE DADOS**
"""

from google.colab import drive
import pandas as pd

# MONTA NO GOOGLE DRIVE
drive.mount('/content/drive')

# CARREGA O ARQUIVO .CSV DE 2018
arquivo_WH_2018 = '/content/drive/MyDrive/dados_projeto_integrador2023/WH_2018.csv'
df2018 = pd.read_csv(arquivo_WH_2018)

# CARREGA O ARQUIVO .CSV DE 2019
arquivo_WH_2019 = '/content/drive/MyDrive/dados_projeto_integrador2023/WH_2019.csv'
df2019 = pd.read_csv(arquivo_WH_2019)

#importando as bibliotecas python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""**WORLD HAPPINNESS 2018**"""

# 2018.1) exibe o .csv e mostra a qtde de linhas e colunas
display(df2018)
df2018.shape

# 2018.2) mostra o dataframe como matriz transposta
df2018.T

# 2018.3) exibe primeiras linhas do dataframe
df2018.head()

# 2018.4) verifica se há valores NaN no dataframe
df2018.isna()

# 2018.5) mostra estatísticas
estatistica2018 = df2018.describe()
print(estatistica2018)

# 2018.6) mostra os países ou regiões únicas
paises2018 = df2018['Country or region'].unique()
print(paises2018)

#exibe a quantidade países ou regiões únicas
print()
num_paises = df2018 ['Country or region'].nunique()
print(f"{num_paises} países únicos.")

"""___________________________________________
**WORLD HAPPINESS 2019**
"""

# 2019.1) exibe o .csv e mostra a qtde de linhas e colunas
display(df2019)
df2019.shape

# 2019.2) mostra o dataframe como matriz transposta
df2019.T

# 2019.3) exibe primeiras linhas do dataframe
df2019.head()

# 2019.4) verifica se há valores NaN no dataframe
df2019.isna()

# 2019.5) mostra estatísticas
estatistica2019 = df2019.describe()
print(estatistica2019)

# 2019.6) mostra os países ou regiões únicas
paises2019 = df2019['Country or region'].unique()
print(paises2019)

#exibe a quantidade países ou regiões únicas
print()
num_paises = df2019 ['Country or region'].nunique()
print(f"{num_paises} países únicos.")

"""_________________________

**GRÁFICOS**

*É importante destacar que, para gráficos que demandam uma visualização clara, devido à impossibilidade de implementar a divisão por região nos países, optamos por separar os 156 países dos rankings de 2018 e 2019 em 6 grupos de 26 países, seguindo a ordem do ranking do dataframe, ou seja, grupo 1 são os 26 primeiros, grupo 2 os 26 seguintes, etc. Essa abordagem visa exemplificar o uso dos gráficos, proporcionando uma análise mais focada e compreensível.

- GRÁFICO DE BARRAS
"""

# Divião dos países em 6 grupos de 26
df2018['Group'] = pd.cut(df2018['Overall rank'], bins=6, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6'])
df2019['Group'] = pd.cut(df2019['Overall rank'], bins=6, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6'])

# Configura as figuras e os eixos
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8), sharey=True)

# Gráfico de BARRAS [2018]
sns.barplot(x='Group', y='Perceptions of corruption', data=df2018, color='blue', errorbar=None, ax=axes[0])
axes[0].set_title('Perceptions of Corruption por Grupo de 26 países - 2018')
axes[0].set_xlabel('Grupo')
axes[0].set_ylabel('Perceptions of Corruption')
axes[0].grid(True, linestyle='--', alpha=0.7)

# Gráfico de BARRAS [2019]
sns.barplot(x='Group', y='Perceptions of corruption', data=df2019, color='green', errorbar=None, ax=axes[1])
axes[1].set_title('Perceptions of Corruption por Grupo de 26 países - 2019')
axes[1].set_xlabel('Grupo')
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.suptitle('Comparação de Perceptions of Corruption por Grupo - 2018 e 2019')

plt.show()

"""- GRÁFICO HISTOGRAMA"""

# Configura o estilo
sns.set(style="whitegrid")

# Cria subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), sharey=True)

# Histograma [2018]
sns.histplot(df2018['Score'], bins=15, kde=True, color='blue', ax=axes[0])
axes[0].set_title('Distribuição do Score - 2018')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Frequência')

# Histograma [2019]
sns.histplot(df2019['Score'], bins=15, kde=True, color='green', ax=axes[1])
axes[1].set_title('Distribuição do Score - 2019')
axes[1].set_xlabel('Score')
axes[1].set_ylabel('Frequência')

# Ajusta layout
plt.tight_layout()

plt.show()

"""- BOXPLOT"""

# 2018

# Divião dos países em 6 grupos de 26
df2018['Groups'] = pd.cut(df2018.index, bins=6, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6'])

# Cria boxplots para cada grupo
plt.figure(figsize=(12, 8))
sns.boxplot(x='Groups', y='GDP per capita', data=df2018)
plt.title('Boxplots dividindo os Países em 6 Grupos de 26 países cada - 2018')
plt.ylabel('GDP per capita')
plt.xlabel('Groups')
plt.show()

# 2019

# Divião dos países em 6 grupos de 26
df2019['Groups'] = pd.cut(df2019.index, bins=6, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6'])

# Cria boxplots para cada grupo
plt.figure(figsize=(12, 8))
sns.boxplot(x='Groups', y='GDP per capita', data=df2019)
plt.title('Boxplots dividindo os Países em 6 Grupos de 26 países cada - 2019')
plt.ylabel('GDP per capita')
plt.xlabel('Groups')
plt.show()

"""- DISPERSÃO COM REGRESSÃO LINEAR"""

# Configura as figuras e os eixos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico de dispersão com regressão linear [2018]
sns.regplot(x=df2018['GDP per capita'], y=df2018['Healthy life expectancy'], ax=ax1, scatter_kws={'color': 'green', 'alpha': 0.8})
ax1.set_title('2018')
ax1.set_xlabel('GDP per capita')
ax1.set_ylabel('Healthy life expectancy')

# Gráfico de dispersão com regressão linear [2019]
sns.regplot(x=df2019['GDP per capita'], y=df2019['Healthy life expectancy'], ax=ax2, scatter_kws={'color': 'green', 'alpha': 0.8})
ax2.set_title('2019')
ax2.set_xlabel('GDP per capita')
ax2.set_ylabel('Healthy life expectancy')

plt.show()

# Gráfico de dispersão com regressão linear, mas as bolinhas ficam maiores caso o pais tenha maior 'Perception of corruption'.

# Configura as figuras e os eixos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# [2018]
sns.regplot(x=df2018['GDP per capita'], y=df2018['Healthy life expectancy'], ax=ax1, scatter_kws={'color': 'green', 'alpha': 0.8, 's': df2018['Perceptions of corruption']*500})
ax1.set_title('2018')
ax1.set_xlabel('GDP per capita')
ax1.set_ylabel('Healthy life expectancy')

# [2019]
sns.regplot(x=df2019['GDP per capita'], y=df2019['Healthy life expectancy'], ax=ax2, scatter_kws={'color': 'green', 'alpha': 0.8, 's': df2019['Perceptions of corruption']*500})
ax2.set_title('2019')
ax2.set_xlabel('GDP per capita')
ax2.set_ylabel('Healthy life expectancy')

plt.show()

"""- MAPA DE CALOR COM ANOTAÇÕES"""

# [2018]

# Seleciona as colunas
colunas_incluir= df2018.columns.difference(['Overall rank', 'Country', 'Year', 'Region'])

# Correlaciona os valores
corr_matrix = df2018[colunas_incluir].corr()

# Cria o mapa de calor
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)

plt.title('2018')

plt.show()

# [2019]

# Seleciona as colunas
colunas_incluir= df2019.columns.difference(['Overall rank', 'Country', 'Year', 'Region'])

# Correlaciona os valores
corr_matrix = df2019[colunas_incluir].corr()

# Cria o mapa de calor
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)

plt.title('2019')

plt.show()

"""- GRÁFICO DE LINHAS
*As base de dados não satisfazeram o gráfico de linha. Com isso em mente, optamos por importar outra, que mostra os suicídios por Estado e Ano no Brasil.
"""

# CARREGA O ARQUIVO .CSV DE tristeza_estados_anos
tristeza = '/content/drive/MyDrive/dados_projeto_integrador2023/tristeza_estados_anos.csv'
dftristeza = pd.read_csv(tristeza)

display(dftristeza)

dftristeza.isna()

# Cria um gráfico de linhas com sns.lineplot
sns.lineplot(x='ano', y='n', data=dftristeza, marker='o', color='black', label='n')

# Adiciona título e rótulos aos eixos
plt.title('Progressão de N ao longo dos Anos 2010-2019')
plt.xlabel('Ano')
plt.ylabel('Valor de n')

plt.show()

# Cria um gráfico de linhas com sns.lineplot
sns.lineplot(x='estado', y='n', data=dftristeza, marker='o', color='black', label='n')

# Adiciona título e rótulos aos eixos
plt.title('Variação de n por Estado')
plt.xlabel('Estado')
plt.ylabel('Valor de n')

# Rotaciona os estados do eixo X para melhorar a legibilidade
plt.xticks(rotation=90, ha='center')

plt.show()