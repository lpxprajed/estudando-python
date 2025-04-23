#append(x): adiciona um item ao final da lista

lista = []
add_lista = input("Qualquer coisa: ")
lista.append(add_lista) 
print(lista)

dados = []

for i in range(1,6):
    fornceca_dados = input("Forneça seus dados: ")
    dados.append(fornceca_dados)
    
print(dados)
    
#extend(): adiciona todos os itens de uma vez ao final da lista

lista = []

a = [1,2,3,45]
b = [1,4,5,6]

lista.extend(a) 
print(lista)

lista.append(b) # O append vai adiconar outra lista com esses dados
print(lista)
 
# insert(i, x): insere um item em um indice especifico e aumenta o tamanho da lista (i, x) 

lista = [1,2,3,4,5,6,7]

lista.insert(3, 9)
print(lista)

# remove(x): Remove o primeiro intem com o valor selecionado

lista = [1,2,3,4,5,5,6]
print(lista)
lista.remove(6)
print(lista)

# pop(i): Remove por indice, e se nenhum for fornecido, ele ira remover o ultimo da lista

lista = [1,2,3,4,5,6,7]
print(lista)
lista.pop(3)
print(lista)
lista.pop()
print(lista)

# clear(): Remove todos os indices de uma lista

lista = ["Eu",1,2, "Lopes" , [1,2,3,4]]
print(lista)
lista.clear()
print(lista)

# index(x): Retorna o indice do valor selecionado

lista = [1,2,3,4,5,6,7]
lista.index(2)
print(lista.index(3))

# count(x): Conta quantas vezes um valor apareceu

lista = [1,2,3,4,5,6,7,1,2,1,2,3,4,5,6,6,7,8,8,8]
print(lista.count(8))

# reverse(): Inverte a ordem da lista

lista = [1,2,3,4,5,6,7]
print(lista)
lista.reverse()
print(lista)

# copy(): Copia os intens de uma lista

lista1 = [1,2,3,4,5,6,7]
lista2 = lista1.copy()
lista2.append(8)

print(lista2) 

    
    
    