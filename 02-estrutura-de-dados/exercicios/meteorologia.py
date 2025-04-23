listaMeses = []
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

contador2 = 0

for i in meses:
    temperatura = input(f"Forneça a temperatura do mes {meses[contador2]}: ")
    temperatura = float(temperatura)
    listaMeses.append(temperatura)
    contador2 += 1
    
mediaAnual = sum(listaMeses) / len(listaMeses)
print(f"Media Anula: {mediaAnual:.2f}")

contador1 = 0
for temperatura in listaMeses:
        if temperatura > mediaAnual:
         print(f"{meses[contador1].capitalize()}: {temperatura}°C")
        
        contador1 +=1



    