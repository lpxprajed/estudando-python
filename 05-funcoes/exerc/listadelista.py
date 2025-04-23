dados = [[6.0, 7.0, 8.0], [5.0, 6.5, 4.0],[10.0, 9.5, 8.0],[7,8,9]]

for i in dados:
    media = sum(i) / len(i)
    if media < 6:
       aprovado = False
    else:
        aprovado = True
    
    print(f"Media: {media:.2f} Aprovado: {aprovado}")
