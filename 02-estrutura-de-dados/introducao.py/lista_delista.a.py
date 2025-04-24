notas = [[8.0, 9.0, 10.0],
 [9.0, 7.0, 6.0],
 [3.4, 7.0, 7.0],
 [5.5, 6.6, 8.0],
 [6.0, 10.0, 9.5]]

print(notas[2][-1])

for i in notas:
    print(i)
    
    
notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []

for i in range(0, len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])

print(nomes)
print(notas_juntas)