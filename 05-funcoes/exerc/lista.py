lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

def funcs(x):
    tamanho = len(x)
    maior = max(x)
    soma = sum(x)
    menor = min(x)
    
    return(tamanho, maior, soma,menor)

tamanho, maior, soma, menor = funcs(lista)

print(f"A lista possui {tamanho} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")