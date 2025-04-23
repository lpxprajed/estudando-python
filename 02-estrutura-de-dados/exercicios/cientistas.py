dados = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

medias = []
maior = 0
area_com_maior_media = ''

# Calcular as médias por área
for chave, valor in dados.items():
    media = sum(valor) / len(valor)
    medias.append(media)
    print(f"Média da {chave}: {media:.2f}")
    
    # Verificar se a média atual é a maior
    if media > maior:
        maior = media
        area_com_maior_media = chave

# Imprimir a área com a maior média
print(f"\nÁrea com a maior diversidade biológica: {area_com_maior_media} com média de {maior:.2f}")
