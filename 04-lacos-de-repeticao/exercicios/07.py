# Exercício 7: Faça um programa que peça um número inteiro e mostre se ele é primo ou não. Um número é primo se ele for maior que 1 e só for divisível por 1 e por ele mesmo.

num = int(input("Numero: "))
divisor = 0

for n in range(1, num +1):
    if num % n == 0:
        divisor += 1
        
if divisor == 2:
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")