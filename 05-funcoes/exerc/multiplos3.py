numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
numero_3 = []

def multiplo3(x):
    for i in x:
        if i % 3 == 0:
         numero_3.append(i)
         
    return numero_3

numero_3 = multiplo3(numeros)

print(numero_3)


        
        
            