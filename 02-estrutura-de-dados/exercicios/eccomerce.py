id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

# Cabeçalho da tabela
cabecalho = ('id', 'quantidade', 'preco', 'total')

# Criando as tuplas com os dados, incluindo o valor total
cadastro = [cabecalho] + [(i, qtde, valor, qtde * valor) for i, qtde, valor in zip(id, quantidade, preco)]

# Exibindo o resultado
for linha in cadastro:
    print(linha)
