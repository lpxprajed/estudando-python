# Exercício 4 - Média de temperaturas

temperatura = []

while True:
    temp = float(input("Informe uma temperatura: "))
    
    if temp == 273:
        break
    
    temperatura.append(temp)
    
media = sum(temperatura) / len(temperatura)
print(f"Media: {media:.2f}°C")