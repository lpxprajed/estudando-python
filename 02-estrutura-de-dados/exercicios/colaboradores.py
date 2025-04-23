lista_salario = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {}

contador_minimo = 0

for salario in lista_salario:
    abono = salario * 0.1
    if abono < 200:
        abono = 200
    
    if abono == 200:
        contador_minimo +=1
        
    
    abonos[salario] = abono
    
   

total_gasto = sum(abonos.values())
maior_abono = max(abonos.values())
print(f"Total gasto com abonos: R$ {total_gasto:.2f}")
print(f"Maior valor de abono: R$ {maior_abono:.2f}")
print(f"Colaboradores que receberam o abono mínimo: {contador_minimo}")


    
        

