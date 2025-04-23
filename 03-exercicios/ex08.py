# Programa 12

opcao = int(input("Etanol 1 | Diesel 2 :  "))

# Valor 
valor_etanol = 1.70
valor_diesel = 2.0

# Escolhendo

if opcao == 1:
    quantos_litros_etanol = float(input("Digite quantos litros: "))
    if quantos_litros_etanol <= 15:
       valor_original = (valor_etanol * quantos_litros_etanol )
       desconto = (valor_original * 2) / 100
       valor_original = valor_original - desconto
       print(f"Total a se pagar {valor_original}")
    else:
       valor_original = (valor_etanol * quantos_litros_etanol )
       desconto = (valor_original * 4) / 100
       valor_original = valor_original - desconto
       print(f"Total a se pagar {valor_original}")

if opcao == 2:
    quantos_litros_diesel = float(input("Digite quantos litros: "))
    if quantos_litros_diesel <= 15:
        valor_original = (valor_diesel * quantos_litros_diesel)
        desconto = (valor_original * 3) / 100
        valor_original = valor_original - desconto
        print(f"Total a se pagar {valor_original}")
    else:
       valor_original = (valor_diesel * quantos_litros_diesel)
       desconto = (valor_original * 5) / 100
       valor_original = valor_original - desconto
       print(f"Total a se pagar {valor_original}")
       
            
            
