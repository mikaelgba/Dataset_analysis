import method

regiao_um = method.selecionar_regiao("Norte")
print(regiao_um)

dias, casos, mortes = method.criar_listas(regiao_um)    
method.gerar_grafico(dias, casos,"Casos na região Norte","Casos","Dias")
method.gerar_grafico(dias, mortes,"Mortes na região Norte","Mortes","Dias")


regiao_dois = method.selecionar_regiao("Nordeste")
print(regiao_dois)

dias, casos, mortes = method.criar_listas(regiao_dois)
method.gerar_grafico(dias, casos,"Casos na região Nordeste","Casos","Dias")
method.gerar_grafico(dias, mortes,"Mortes na região Nordeste","Mortes","Dias")

#Falta concertar o da regiao Centro-Oeste
regiao_tres = method.selecionar_regiao("Centro-Oeste")
print(regiao_tres)

dias, casos, mortes = method.criar_listas(regiao_tres)
method.gerar_grafico(dias, casos,"Casos na região Centro Oeste","Casos","Dias")
method.gerar_grafico(dias, mortes,"Mortes na região Centro Oeste","Mortes","Dias")

regiao_quatro = method.selecionar_regiao("Sudeste")
print(regiao_quatro)

dias, casos, mortes = method.criar_listas(regiao_quatro)
method.gerar_grafico(dias, casos,"Casos na região Sudeste","Casos","Dias")
method.gerar_grafico(dias, mortes,"Mortes na região Sudeste","Mortes","Dias")


regiao_cinco = method.selecionar_regiao("Sul")
print(regiao_cinco)

dias, casos, mortes = method.criar_listas(regiao_cinco)
method.gerar_grafico(dias, casos,"Casos na região Sul","Casos","Dias")
method.gerar_grafico(dias, mortes,"Mortes na região Sul","Mortes","Dias")



