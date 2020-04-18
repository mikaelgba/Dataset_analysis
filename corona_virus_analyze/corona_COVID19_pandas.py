import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nome_arquivo = "datasets\corona-virus-brazil/brazil_covid19.csv"
dataset = pd.read_csv(nome_arquivo)


print("Teste Booleano se casa indice tem numeros de caso maior que 500")
print(dataset["cases"] > 500,"\n")

print("Descricao completa")
print(dataset.describe())

print(dataset.groupby("region").mean(),"\n")

print(dataset["cases"].plot.hist(),"\n")

print(dataset["cases"].plot.hist(bins=30, edgecolor='black'), "\n")

print(dataset["cases"].value_counts().plot.bar(), "\n")

print(dataset["cases"].value_counts().plot.barh(), "\n")

print(dataset["region"].value_counts(),"\n")

print(dataset["region"].value_counts(normalize=True),"\n")

print(dataset)
