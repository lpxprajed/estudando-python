lista1 = [4,6,7,9,10]
lista2 = [-4,6,'E',7]


def recebe(x, y):
    resultado = []
    if len(x) != len(y):
        raise IndexError ('A quantidade de elementos em cada lista é diferente.')
        
    for valor1,valor2  in zip(x, y):
     try:   
        soma = valor1 + valor2
        tupla = (valor1, valor2, soma)
        resultado.append(tupla)
     except TypeError:
         raise TypeError("Erro: tipo de dado inválido nas listas.")
     

    return resultado

resultado = recebe(lista1, lista2)
print(resultado)

# Tratando erros


