# 01

def ler_numero():
  while True:
    try:
     x = int(input("Digite um número: "))
     break
    except ValueError:
      print("Você não digitou um número inteiro Tente novamente")
      
  return x


resultado = ler_numero()
print(resultado)

# 02

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é permitido dividir por zero.")
    
    return a / b

divisao = dividir(10, 0)
print(divisao)

# 03

for i in range(1):
    try:
        numero = int(input("Dite um numero: "))
        numero2 = int(input("Dite um numero: "))
        conta = numero / numero2
        print(conta)
    except ValueError:
        print("Entrada inválida.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    
    finally:
        print("fim da execucão")
         

        