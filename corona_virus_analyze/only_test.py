import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nome_arquivo = "datasets\corona-virus-brazil/brazil_covid19.csv"
dataset = pd.read_csv(nome_arquivo)

dataset.plot.scatter(x='preco', y='area', s=.5)

plt.figure(figsize=(8,5))

regioes =[["Amazonas","Acre","Amapá","Pará","Rondônia","Roraima","Tocantins"]
          ,["Alagoas","Bahia","Ceará","Maranhão","Paraíba","Pernambuco","Piauí","Rio Grande do Norte","Sergipe"]
          ,["Distrito Federal","Goiás","Mato Grosso","Mato Grosso do Sul"]
          ,["Espírito Santo","Minas Gerais","Rio de Janeiro","São Paulo"]
          ,["Paraná","Rio Grande do Sul","Santa Catarina"]]

norte = 0
norteste = 0
centro = 0
sudeste = 0
sul = 0
list_aux = list(dataset)
for j in range(len(list_aux)):

    if(list_aux[j][1] == "Norte"):
        norte += list_aux[j][3]

    if(list_aux[j][1] == "Nordeste"):
        norteste += j[3]

    if(list_aux[j][1] == "Centro-Oeste"):
        centro += j[3]

    if(list_aux[j][1] == "Sudeste"):
        sudeste += j[3]

    if(list_aux[j][1] == "Sul"):
        sul += j[3]
print(norte)
        
x_data = ["Norte","Nordeste","Centro","Sudeste","Sul"]
y_data = [norte,norteste,centro,sudeste,sul]

plt.bar(x_data, y_data)
plt.ylabel('Casos')
plt.xlabel('Estados')
plt.show()

'''f = open(nome_arquivo)
data = csv.load(f)
f.close()

f = open("issues.csv","wb+")
csv_file=csv.writer(f)

csv_file.writerow(["Dia","casos","mortes"])

for item in data:

    csv_file.writerow([item["Dia"],item["casos"],item["mortes"]])'''


'''X = []
y = []
#dataAnt

for i, j  in dataset.iteritems():

    if(i != []):
        #X.append(i["date"].values)
        print(i, j)'''

'''plt.figure(figsize=(8,6))
x_data, y_data = (dataset["date"].values, dataset["cases"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('Casos')
plt.xlabel('Dias')
plt.show()'''
