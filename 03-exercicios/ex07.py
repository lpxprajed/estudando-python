# Programa 13

quantidade_vendas_2022 = float(input("Vendas de 2022: "))
quantidade_vendas_2023 = float(input("Vendas de 2023: "))

variacao = (quantidade_vendas_2023 - quantidade_vendas_2022) / quantidade_vendas_2022 * 100

if variacao > 20:
    print("Bonificar time de vendas")
    
elif variacao >= 2 :
    print("Pequena bonificação para time de vendas")
    
elif variacao <= 2:
    print("Planejamento de políticas de incentivo às vendas.")

elif variacao < -10:
    print("corte de gastos")
         
