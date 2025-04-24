# notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

# def media(lista: list = [0]) -> float :
#     media = sum(lista) / len(lista)
    
#     return media

# medias = [round(media(nota),1) for nota in notas]
# print(medias)

nomes = [('Miguel', 'MIG989'), ('Emmilly', 'EMM491'), ('Joao', 'JOA750'), ('Bruna', 'BRU42'),('Roberto', 'ROB45')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

nomes = [nome[0] for nome in nomes]
nomes 

estudadntes = list(zip(nomes, medias))
candidatos = [estudante[0] for estudante in estudadntes if estudante[1] >= 8]
print(candidatos)