setores = {
 'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

soma_total = 0
qtd_pessoas = 0

# Calcular soma total e quantidade de pessoas
for chave, valor in setores.items():
    soma_total += sum(valor)
    qtd_pessoas += len(valor)
    # Calcular e imprimir a média de cada setor
    media_setor = sum(valor) / len(valor)
    print(f"Média do {chave}: {media_setor:.2f}")

# Calcular a média geral
media_geral = soma_total / qtd_pessoas
print(f"Média geral: {media_geral:.2f}")

# Contar pessoas acima da média geral
pessoas_acima_media_geral = 0
for chave, pessoas in setores.items():
    for pessoa in pessoas:
        if pessoa > media_geral:
            pessoas_acima_media_geral += 1

print(f"Número de pessoas acima da média geral: {pessoas_acima_media_geral}")
