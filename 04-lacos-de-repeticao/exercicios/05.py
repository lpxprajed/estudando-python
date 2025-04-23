# Fatorial de um número inteiro positivo

num = int(input("Numero: "))
fator = 1

for i in range(1, num + 1):
    fator *= i

print(fator)