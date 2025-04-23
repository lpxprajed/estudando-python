
contador = 1

while contador <= 15:
    print(f"Avaliação {contador}")
    nota = float(input("Digite uma nota de 0 a 5: "))
    if nota <= 5:
        print("Nota valida, obrigado!")
    else:
        print("Nota invalida")
        continue
    contador += 1
    
    



   
          