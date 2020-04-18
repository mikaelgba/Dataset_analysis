import matplotlib.pyplot as plt
import csv

nome_arquivo = "datasets\corona-virus-brazil/brazil_covid19.csv"

with open(nome_arquivo) as arquivo:
    
    csv_reader = csv.reader(arquivo, delimiter=',')

    data_at = ""
    countCasos = 0
    countMortes = 0
    dias = []
    casos = []
    mortes = []

    for i in csv_reader:

        if(i != [] and i[0] == data_at):
   
            countCasos += int(i[3])
            countMortes += int(i[4])

        elif(i != [] and i[0] != data_at):
            
            data_at = i[0]
            dias.append(i[0])
            casos.append(countCasos)
            mortes.append(countMortes)
            countCasos = 0
            countMortes = 0

plt.figure(figsize=(8, 6))
x_data, y_data = (dias,casos)
plt.bar(x_data, y_data)
plt.title("Numeros de Casos no Brasil")
plt.ylabel('Casos')
plt.xlabel('Dias')
plt.show()
plt.close()

plt.figure(figsize=(8, 6))
x_data, y_data = (dias,mortes)
plt.bar(x_data, y_data)
plt.title("Numeros de Mortes no Brasil")
plt.ylabel('Mortes')
plt.xlabel('Dias')
plt.show()
plt.close()        
