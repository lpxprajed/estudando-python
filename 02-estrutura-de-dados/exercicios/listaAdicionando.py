idades = []

while True:
    idade = input("Digite uma idade: ")
    
    if idade == "":
        break
    
    idades.append(int(idade))

print(idades)

minimo = min(idades)
maximo = max(idades)
qtde = len(idades)
media = sum(idades) / len(idades)

print("MINIMO: ",  minimo) 
print("MAXIMO: ", maximo)
print("QTDE: ",  qtde) 
print("MEDIA: ", media) 