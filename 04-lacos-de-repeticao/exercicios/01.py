#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

numero1 = int(input("num1: "))
numero2 = int(input("num2: "))

while numero1 < numero2:
    print(numero1)
    numero1 += 1