notas = [[7.0, 8.0, 9.0], [6.0, 6.5, 7.0], [9.0, 8.5, 10.0], [5.0, 5.5, 6.0]]

for i in notas:
    media = sum(i) / len(i)
    print(f'Média: {media:.2f}')


print(notas[1][1])
print(notas[-1][-1])

soma = sum(notas[2])
print(soma)

notas_acima_8 = []

for i in notas:
    for nota in i:
        if nota > 8:
            notas_acima_8.append(nota)

print(notas_acima_8)

def media(x):
    medias = []
    aprovacoes = []
    
    for i in x:
        m = sum(i) / len(i)
        medias.append(m)

        if m < 6:
            aprovacoes.append("não")
        else:
            aprovacoes.append("sim")

        print(f"Média: {m:.2f}")
    
    return medias, aprovacoes

medias, aprovados = media(notas)

print("Médias:", medias)
print("Aprovados:", aprovados)
