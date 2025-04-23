saldo_em_conta = 0 
# Inicio do laço 
while True:
    saldo = input("Digite seu saldo: ") # pede o saldo ao usuário
    
    if saldo == "": # se o saldo for vazio, sai do laço
        break # sai do laço
    
    saldo_em_conta += float(saldo) # soma os valores digitados
    
print(f"Saldo em conta: {saldo_em_conta:.2f}") # Resultado final
        
