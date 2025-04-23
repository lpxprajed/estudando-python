notas = []

for i in range(5):
    nota = int(input("Dite uma nota: "))
    notas.append(nota)

print(notas)

def calcNota(x):
    tirandoMenor = sum(x) - min(x)
    tirandoMaior = sum(x) - max(x)
    notas_finais = sum(x)
    media = sum(x) / len(x)
    
    return tirandoMaior, tirandoMenor, notas_finais, media

tirar_maior, tirar_menor, total, media = calcNota(notas)

print(f"Nota da manobra: {media}")

print(f"Soma das notas sem o maior valor: {tirar_maior}")
print(f"Soma das notas sem o menor valor: {tirar_menor}")
print(f"Soma total das notas: {total}")

