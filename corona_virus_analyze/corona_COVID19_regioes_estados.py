import method

estados = ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia",
           "Roraima", "Tocantins", "Alagoas", "Bahia", "Ceará",
           "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte",
           "Sergipe", "Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul",
           "Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo",
           "Paraná", "Rio Grande do Sul", "Santa Catarina"]

regions = ["Norte","Nordeste","Centro-Oeste","Sudeste","Sul"]

for i in estados:
    method.listar_dados_estado(i)

for i in regions:
    
    regiao = method.selecionar_regiao(i)
    print(regiao)
    dias, casos, mortes = method.criar_listas(regiao)    
    method.gerar_grafico(dias, casos,"Casos na região " + i,"Casos","Dias")
    method.gerar_grafico(dias, mortes,"Mortes na região " + i,"Mortes","Dias")
