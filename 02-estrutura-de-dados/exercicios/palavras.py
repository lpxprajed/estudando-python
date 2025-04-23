palavras = {}

while True:
    palavra = input("Entre com uma palavra: ")
    if palavra == "":
        break
    
    if palavra not in palavras:
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1

for chave, valor in palavras.items():
    print(chave, ":", valor)
        
