# Dicionário com os pesos para cada tipo de dado
pesos = {
    'Senha': 100,
    'Email': 15,
    'Telefone': 70,
    'Nome': 25
}

# Dicionário com os vazamentos de dados para cada site
vazamentos = {
    'Instagram': ['Senha', 'Nome'],
    'Twitter': ['Nome'],
    'Facebook': ['Email', 'Telefone'],
    'YouTube': ['Email', 'Senha', 'Telefone']
}

# Dicionário para armazenar a pontuação de cada site
pontuacao = {}

# Para cada site e seus respectivos vazamentos
for site, dados_vazados in vazamentos.items():
    # Inicializa a pontuação do site com 0
    pontuacao[site] = 0
    # Para cada dado vazado
    for dado in dados_vazados:
        # Adiciona o peso do dado vazado à pontuação do site
        pontuacao[site] += pesos[dado]

# Ordena os sites por pontuação em ordem decrescente
ranking = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)

# Imprime o ranking
for i, (site, pontos) in enumerate(ranking, start=1):
    print(f'{i}. {site}: {pontos} pontos')