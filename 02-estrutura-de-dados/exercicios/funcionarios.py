funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), 
                ('MG', 4), ('ES', 9), ('ES', 7), ('ES', 12), ('SP', 7),
                ('SP', 11), ('MG', 8), ('ES', 8), ('SP', 9), ('RJ', 13),
                ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7),
                ('ES', 14), ('SP', 10), ('MG', 12)]

# Agrupar os dados usando dict comprehension
agrupado = {estado: [qtd for estado_, qtd in funcionarios if estado_ == estado] for estado in set(estado_ for estado_, _ in funcionarios)}

# Resultado final
print(agrupado)
