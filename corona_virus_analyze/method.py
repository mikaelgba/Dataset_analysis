import matplotlib.pyplot as plt
import csv

nome_arquivo = "datasets\corona-virus-brazil/brazil_covid19.csv"

def gerar_grafico(lista_um, lista_dois, titulo, y, x):

    plt.figure(figsize=(8, 6))
    x_data, y_data = (lista_um, lista_dois)
    plt.bar(x_data, y_data)
    plt.title(titulo)
    plt.ylabel(y)
    plt.xlabel(x)
    return plt.show()

def selecionar_regiao(regiao_entrada):

    with open(nome_arquivo) as arquivo:
    
        csv_reader = csv.reader(arquivo, delimiter=',')

        data_at = ""
        regiao_atual = ""
        countCasos = 0
        countMortes = 0
        regiao = []
    
        for i in csv_reader:
           
            if(i != [] and i[0] == data_at and i[1] == regiao_entrada):
   
                countCasos += int(i[3])
                countMortes += int(i[4])

            elif(i != [] and i[0] != data_at and i[1] != regiao_entrada):
          
                regiao.append([data_at, countCasos, countMortes])
                regiao_atual = i[1]
                data_at = i[0]
                countCasos = 0
                countMortes = 0
                
    return regiao

def selecionar_estado(estado_entrada):

    with open(nome_arquivo) as arquivo:
    
        csv_reader = csv.reader(arquivo, delimiter=',')

        estado_saida = []
    
        for i in csv_reader:
           
            if(i != [] and i[2] == estado_entrada):

                estado_saida.append([i[0], int(i[3]), int(i[4])])
                  
    return estado_saida

def criar_listas(lista_entrda):
    
    dias = []
    casos = []
    mortes = []
    
    for i in lista_entrda:
        
        dias.append(i[0])
        casos.append(i[1])
        mortes.append(i[2])

    return dias, casos, mortes

def listar_dados_estado(nome_estado):

    estado = selecionar_estado(nome_estado)
    dias, casos, mortes = criar_listas(estado)
    return gerar_grafico(dias, casos, "Casos no " + nome_estado,"Casos","Dias"), gerar_grafico(dias, mortes,"Mortes no " + nome_estado,"Mortes","Dias")
