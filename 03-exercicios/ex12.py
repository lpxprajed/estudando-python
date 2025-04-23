numero1 = int(input("num1 "))
numero2 = int(input("num2 "))

while numero1 < numero2:
    print(numero1)
    numero1 += 1


bacteria_a = 4
bacteria_b = 10
dias = 0

while bacteria_a < bacteria_b:
    bacteria_a *= 1.03
    bacteria_b *= 1.015
    dias += 1
    print(f"A:{bacteria_a:.2f} | B:{bacteria_b:.2f} | DIAS {dias}")
    

dados = 15
contador = 0

while contador < dados:
    nota = int(input("Avalie de 0 a 5: "))
    if nota > 5 or nota  < 0:
        print("Nota invalida.")
        continue
    else:
        print("Nota recebida.")    
    
      
    contador += 1
    
print("Obrigado pela avaliação.")    

temperatura = []

while True:
    temp = float(input("Informe uma temperatura: "))
    
    if temp == 273:
        break
    
    temperatura.append(temp)
    
media = sum(temperatura) / len(temperatura)
print(f"Media: {media:.2f}°C")    


num = int(input("Numero: "))
fator = 1

for i in range(1, num + 1):
    fator *= i

print(fator)


tabuada = int(input("Tabuada: "))
contador = 1

while contador <= 10:
    print(f"{tabuada} x {contador} = {tabuada * contador}")
    contador += 1


num = int(input("Numero: "))
divisor = 0

for n in range(1, num +1):
    if num % n == 0:
        divisor += 1
        
if divisor == 2:
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")

    
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


    
                