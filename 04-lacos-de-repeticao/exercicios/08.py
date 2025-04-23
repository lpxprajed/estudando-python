# Exercício 8: Faça um programa que leia a idade de várias pessoas. O programa deverá perguntar se a pessoa quer continuar ou não. No final, mostre:
# - A quantidade de pessoas que tem entre 0 e 25 anos.
# - A quantidade de pessoas que tem entre 26 e 50 anos.
# - A quantidade de pessoas que tem entre 51 e 75 anos.
# - A quantidade de pessoas que tem entre 76 e 100 anos.
# - A quantidade de pessoas que tem mais de 100 anos.
# - A quantidade total de pessoas.

grupo_0a25 = 0
grupo_26a50 = 0
grupo_51a75 = 0
grupo_76a100 = 0 

while True:
    idade = int(input("Informe sua idade: "))
    
    if 0 <= idade <= 25:
     print("sua idade esta entre 0 a 25")   
     grupo_0a25 +=1  
    
    elif 26 <= idade <= 50:
        print("sua idade esta entre 26 a 50")
        grupo_26a50 +=1
        
    elif 51 <= idade <= 75:
        print("sua idade esta entre 51 a 75")
        grupo_51a75 +=1
    
    elif 76 <= idade <= 100:
        print("sua idade esta entre 76 a 100")
        grupo_76a100 +=1
    if idade == 0:
        break
    
print(f"Grupo 0 a 25: {grupo_0a25}")
print(f"Grupo 26 a 50: {grupo_26a50}")
print(f"Grupo 51 a 75: {grupo_51a75}")
print(f"Grupo 76 a 100: {grupo_76a100}") 
print(f"Total de pessoas: {grupo_0a25 + grupo_26a50 + grupo_51a75 + grupo_76a100}")
