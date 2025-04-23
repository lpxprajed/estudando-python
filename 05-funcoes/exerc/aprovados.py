nomes = ['João', 'Maria', 'Carlos', 'Fernanda']
notas = [[6.0, 7.5, 8.0], [5.5, 6.0, 6.5], [7.0, 7.0, 7.0], [8.0, 9.0, 10.0]]

for nota, nome in zip(notas, nomes):
    media = sum(nota) / len(nota)
    if media > 8:
        print("-------------")
        print(f"Aluno: {nome} \n Media: {media:.2f}")
        
    
