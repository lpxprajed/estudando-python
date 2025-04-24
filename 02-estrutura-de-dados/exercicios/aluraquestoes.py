# nomes = [('Miguel', 'MIG989'), ('Emmilly', 'EMM491'), ('Joao', 'JOA750'), ('Bruna', 'BRU42'),('Roberto', 'ROB45')]

# notas = [[8.0, 9.0, 10.0],
#  [9.0, 7.0, 6.0],
#  [3.4, 7.0, 7.0],
#  [5.5, 6.6, 8.0],
#  [6.0, 10.0, 9.5]]

# medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]
# situacao

# lista_completa = [nomes, notas, medias, situacao]
# lista_completa

alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)