vendas = {'Produto A': 300, 
          'Produto B': 80, 
          'Produto C': 60,
          'Produto D': 200,
          'Produto E': 250,
          'Produto F': 30}

soma = 0 
for valor in vendas.values():
    soma += valor

maior = max(vendas.values())
print("Maior Valor:",maior)
print(f"Soma de todos os valores: {soma}")
    
    
   
    