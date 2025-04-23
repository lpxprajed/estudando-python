votos = {
"Design 1": 1334, 
"Design 2": 982, 
"Design 3": 1751, 
"Design 4": 210,
"Design 5": 1811 
}



soma = sum(votos.values())
maior = max(votos.values())
porcentagem = (maior / soma) * 100

print(f"Soma de todos os votos: {soma}")
print(f"Maior número de votos: {maior}")

#
    
for design, voto in votos.items():
    if voto == maior:
        print(f"{design} é o design vencedor com {porcentagem:.2f}% dos votos.")