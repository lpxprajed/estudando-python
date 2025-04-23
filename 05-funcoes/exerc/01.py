lista = []

while True:
    numero = input("Entre com um número: ")
    if numero == "":
        break
    lista.append(int(numero))
        

def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)



print(media(lista))
