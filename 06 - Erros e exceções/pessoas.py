def divide_colunas(pressoes, temperaturas):
    resultado = []  # Lista para armazenar o resultado
    
    # Verificar se as listas têm o mesmo tamanho
    if len(pressoes) != len(temperaturas):
        raise ValueError("As listas de pressões e temperaturas devem ter o mesmo tamanho.")
    
    # Iterar pelas listas e realizar a divisão
    for pressao, temperatura in zip(pressoes, temperaturas):
        try:
            # Dividir pressão por temperatura
            resultado.append(pressao / temperatura)
        except ZeroDivisionError:
            # Lançar exceção em caso de divisão por zero
            raise ZeroDivisionError("Não é possível dividir por zero na temperatura.")
    
    return resultado


# Teste com dados sem exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

try:
    resultado = divide_colunas(pressoes, temperaturas)
    print("Resultado da divisão entre pressão e temperatura:", resultado)
except ValueError as e:
    print("Erro de valor:", e)
except ZeroDivisionError as e:
    print("Erro de divisão por zero:", e)


# Teste com exceção de ZeroDivisionError (Temperatura zero em um dos testes)
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

try:
    resultado = divide_colunas(pressoes, temperaturas)
    print("Resultado da divisão entre pressão e temperatura:", resultado)
except ValueError as e:
    print("Erro de valor:", e)
except ZeroDivisionError as e:
    print("Erro de divisão por zero:", e)


# Teste com exceção de ValueError (Listas de tamanhos diferentes)
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

try:
    resultado = divide_colunas(pressoes, temperaturas)
    print("Resultado da divisão entre pressão e temperatura:", resultado)
except ValueError as e:
    print("Erro de valor:", e)
except ZeroDivisionError as e:
    print("Erro de divisão por zero:", e)
