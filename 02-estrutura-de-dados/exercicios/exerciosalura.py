# # 1 

# lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
# lista_de_listas = [sum(numero) for numero in lista_de_listas]

# print(lista_de_listas)

# # 2

# lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
# nome, altura, num3 = zip(*lista_de_tuplas)

# num3 = list(num3)
# print(num3)

# # 3

# lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
# lista = [(i, lista[i]) for i in range(len(lista))]
# print(lista)

# # 4 
# aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
# aluguel = [i for i in aluguel if i[0] == "Apartamento"]
# print(aluguel)

#5
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario = {meses: despesa for meses, despesa in zip(meses, despesa) if despesa > 500}
print(dicionario)