try:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite um numero: "))
    
    divisao = numero1 / numero2
    print(divisao)
    
except ValueError:
    print("Opss! Você digitou um valor errado. Tente novamente")
except ZeroDivisionError:
    print("Não é possivel dividir por zero!!!")
except Exception as e:
    print(f"Erro inesperado: {e}")