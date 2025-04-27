while True:
    try:
        x = int(input("Insira um número: "))
        break
    except ValueError:
        print("Ops! Aceitamos apenas numeros inteiros...")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# Fluxo do try-except:
while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Você não digitou um número válido. Tente novamente")
    else:
        print(f"Você digitou: {numero}")
        break
    finally:
        print("Execução encerrada.")


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é permitido dividir por zero.")
    return a / b

resultado = dividir(10,0)
print(resultado)