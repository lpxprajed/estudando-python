# Dicionário com as idades
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}


while True:
 pesquisa = input("Digite o nome da pessoa: ").strip()

 try:
    # Tenta acessar a chave no dicionário
    idade = idades[pesquisa]
    print(f"A idade de {pesquisa} é {idade}.")
    break
 except KeyError:
    # Caso a chave não seja encontrada, exibe a mensagem de erro
    print("Nome não encontrado.")
    continue