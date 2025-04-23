lista_numero = [1,1,1,1,2,3,4,5,4,4,4,6,7,8,7,8,9,6,6,4,4,8,8,9,9,3,3,3,3,2,2,2,1,5,6,5,5,5,4]

numero = int(input("Dite um número: ")) # Usuario escolhe um número 

contador = 0 # Contagem desse número

for i in lista_numero: # i vai valer por cada elemento desta lista
    if i == numero: # Se i = numero entao conte 1
        contador +=1
    
print(f"Seu número {numero} : Apareceu {contador}") # Mostrando essa contagem