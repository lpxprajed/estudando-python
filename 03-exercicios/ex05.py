# Consoante ou vogal


letra_fornecida = str(input("Digite uma letra:"))
vogais = "A","E","I","O","U"

if letra_fornecida in vogais:
    print("É uma vogal")
elif letra_fornecida not in vogais:
    print("É uma consoante") 
else:
    print("Digite uma opção valida")  