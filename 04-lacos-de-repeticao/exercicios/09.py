# Exercício 9 - Votação
# Faça um programa que simule uma votação. O programa deve ler o número do candidato escolhido pelo eleitor e contabilizar os votos. O programa deve aceitar os seguintes números de candidatos:
# 1, 2, 3, 4. O número 5 deve ser contabilizado como voto nulo e o número 6 como voto em branco. O programa deve parar de ler os votos quando o eleitor digitar 0. No final, o programa deve imprimir o total de votos para cada candidato, o total de votos nulos e o total de votos em branco.
# Além disso, o programa deve calcular e imprimir a porcentagem de votos nulos e em branco em relação ao total de votos.


contador = 0
    
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0



while contador < 10:
    voto = int(input("Escolha seu candidato: "))
    
    if voto == 1:
        candidato1 += 1
        print(f"Você votou no candidato: {voto}")
    
    elif voto == 2:
        candidato2 += 1
        print(f"Você votou no candidato: {voto}")
        
    elif voto == 3:
        candidato3 += 1
        print(f"Você votou no candidato: {voto}")
    
    elif voto == 4:
        candidato4 += 1
        print(f"Você votou no candidato: {voto}")
    
    elif voto == 5:
        nulo +1
        print(f"Você votou em nulo: {voto}")
    
    elif voto == 6:
       branco += 1
       print(f"Você votou em branco: {voto}")
        
        
    contador +=1
    
print(f"candidato 1: {candidato1}")
print(f"candidato 2: {candidato2}")
print(f"candidato 3: {candidato3}")
print(f"candidato 4: {candidato4}")
print(f"Votos nulos: {nulo}")
print(f"Votos em branco: {branco}")
print(f"Total de votos: {candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco}")

total = (candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco)
porcentagem_nulo = (nulo / total) * 100
porcentagem_branco = (branco / total) * 100

print(f"Total de votos: {total}")
print(f"Porcentagem de votos nulos: {porcentagem_nulo:.2f}%")
print(f"Porcentagem de votos em branco: {porcentagem_branco:.2f}%")