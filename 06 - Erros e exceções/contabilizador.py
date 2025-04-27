gabarito = ['D', 'A', 'B', 'C', 'A']
testes = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def corrige_provas(gabarito, testes):
    notas = []  # Lista para guardar as notas dos alunos
    
    for aluno in testes:  # Para cada aluno
        pontuacao = 0  # Começa com 0 pontos
        
        for resposta_aluno, resposta_gabarito in zip(aluno, gabarito):  # Para cada resposta
            # Verificar se a resposta do aluno é válida
            if resposta_aluno not in ['A', 'B', 'C', 'D']:
                raise ValueError(f"A alternativa {resposta_aluno} não é uma opção de alternativa válida")
            
            # Se a resposta estiver correta
            if resposta_aluno == resposta_gabarito:
                pontuacao += 1
        
        notas.append(pontuacao)  # Adiciona a nota do aluno na lista de notas
    
    return notas

resulotad = corrige_provas(gabarito, testes)
print(resulotad)