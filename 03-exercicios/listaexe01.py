# Coleta e amostragem de dados

# 1 Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima.

seu_nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
metros = float(input("Me informe sua altura em metros:"))
print(f"Olá {seu_nome}, voce tem {idade} anos e mede {metros:.2f} metros!")

# 2 Calculadora com operadores

num1 = 9
num2 = 5
divisao = num1 // num2
print(divisao)

num1 = 13
num2 = 7
resto = num1 % num2
print(resto)

nota1 = 8.3
nota2 = 6
nota3 = 11.2
media = (nota1 + nota2 + nota3) / 3
print(media)


pesos = [1,2,3,4]
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / sum(pesos)
print(media_ponderada)

# Strings

texto = "Tudo em maiusculo nessa poha"
texto = texto.upper()
print(texto)


texto = "Tudo em minusculo nessa poha"
texto = texto.lower()
print(texto)


texto = "    Sem espaço  em branco   "
texto = texto.strip()
print(texto)


texto = "Sem a letra e e e e por que é uai"
texto = texto.replace("e","f")
print(texto)

texto = "Sem a letra e e e e por que é uai"
texto = texto.replace("e","@")
print(texto)

texto = "Sem a letra e e e e por que é uai"
texto = texto.replace("e","$")
print(texto)