gabarito = [
"D",
"A",
"C",
"B",
"A",
"D",
"C",
"C",
"A",
"B"
]

nota = 0
contador = 1


for i in range(10):
    print("Questão", contador)
    resposta = input("Resposta: ").upper()
    
    if resposta == gabarito[i]:
        nota +=1
        
    contador +=1

print(nota)
    

    
    