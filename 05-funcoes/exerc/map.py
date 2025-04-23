numeros = [1, 2, 3, 4]
por = list(map(lambda x: x * 3, numeros))
print(por)

palavras = ["Python", "É", "MUITO", "Legal"]
maisculas = list(map(lambda x: x.lower(), palavras))
print(maisculas)


palavras = ["Oi", "Tudo", "Bem"]
add =  list(map(lambda x: x + "!", palavras))
print(add)


numeros = [1, 2, 3, 4, 5]
impar_par = list(map(lambda x: x + 2 if x % 2 == 0 else x + 1, numeros ))
print(impar_par)
# Resultado esperado: [2, 4, 4, 6, 6]


nomes = ["joão", "MARIA", "ana"]
titulo = list(map(lambda x: x.title(), nomes))
print(titulo)
# Resultado esperado: ["João", "Maria", "Ana"]


precos = [10, 25.5, 99.9]
real = list(map(lambda x: "R$" + str(x), precos))
print(real)
# Resultado esperado: ["R$10", "R$25.5", "R$99.9"]


notas = [5, 7, 9, 4]
situacao = list(map(lambda x: "aprovado" if x >= 7 else "reprovado", notas))
print(situacao)
# Resultado esperado: ["reprovado", "aprovado", "aprovado", "reprovado"]

idades = [15, 18, 22, 12]
maior_menor = list(map(lambda x: "maior" if x >= 18 else "menor", idades))
print(maior_menor)
# Resultado esperado: ["menor de idade", "maior de idade", "maior de idade", "menor de idade"]
