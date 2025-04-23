# Listas com os gols marcados e sofridos pelo time em cada partida
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

# Função que calcula os pontos e o aproveitamento do time
def calcular_pontos(marcados, sofridos):
    resultado = []   # Lista para armazenar se o time venceu, empatou ou perdeu cada partida
    pontuacao = []   # Lista para armazenar os pontos conquistados em cada partida

    # Percorre os gols marcados e sofridos ao mesmo tempo
    for gm, gs in zip(marcados, sofridos):
        if gm > gs:
            resultado.append("venceu")
            pontuacao.append(3)  # Vitória vale 3 pontos
        elif gm == gs:
            resultado.append("empatou")
            pontuacao.append(1)  # Empate vale 1 ponto
        else:
            resultado.append("perdeu")
            pontuacao.append(0)  # Derrota vale 0 pontos
    
    # Soma total de pontos conquistados
    total_pontos = sum(pontuacao)

    # Calcula o número total de jogos e a pontuação máxima possível
    total_jogos = len(marcados)
    pontuacao_maxima = total_jogos * 3  # Cada jogo pode render no máximo 3 pontos

    # Calcula o aproveitamento percentual
    aproveitamento = (total_pontos / pontuacao_maxima) * 100

    # Retorna os pontos e o aproveitamento arredondado para duas casas decimais
    return total_pontos, round(aproveitamento, 2)

# Fim da função

# Chamada da função com os dados das listas
pontos, aproveitamento = calcular_pontos(gols_marcados, gols_sofridos)

# Exibe os resultados
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento}%")
