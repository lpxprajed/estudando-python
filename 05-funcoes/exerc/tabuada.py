numero = int(input("Numero: "))

def tabuada(x):
    contador = 0
    while contador <= 10:
        multiplicacao = numero * contador
        print(f"{numero} X {contador} = {multiplicacao}")
        contador +=1
    
tabuada(numero)