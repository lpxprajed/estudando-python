lista = []

while len(lista) < 5:
    numero = input("Digite um numero: ")
    lista.append(numero)

print(lista)

def converte_lista(x):
   try: 
    x = [float(numero) for numero in x]
    return x
   except ValueError:
    print("Sua lista contem valores que não são númericos!!!")
   finally:
    print('Fim da execução da função')   
    
    
resultado = converte_lista(lista)
print(resultado)