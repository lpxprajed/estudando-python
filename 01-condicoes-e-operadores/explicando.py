# OPERADORES ARITMÉTICOS
a = 10
b = 3

print("Soma:", a + b)          # 13
print("Subtração:", a - b)     # 7
print("Multiplicação:", a * b) # 30
print("Divisão:", a / b)       # 3.333...
print("Divisão inteira:", a // b) # 3
print("Resto da divisão (módulo):", a % b) # 1
print("Potência:", a ** b)     # 1000

print("-" * 30)

# OPERADORES RELACIONAIS (COMPARAÇÃO)
a = 5
b = 10

print("Igual (a == b):", a == b)     # False
print("Diferente (a != b):", a != b) # True
print("Maior que (a > b):", a > b)   # False
print("Menor que (a < b):", a < b)   # True
print("Maior ou igual (a >= b):", a >= b) # False
print("Menor ou igual (a <= b):", a <= b) # True

print("-" * 30)

# ESTRUTURA CONDICIONAL
idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")

print("-" * 30)

# OPERADORES LÓGICOS
a = 5
b = 10

print("AND (a > 2 and b < 20):", a > 2 and b < 20)  # True
print("OR (a > 10 or b < 20):", a > 10 or b < 20)   # True
print("NOT (not a > 10):", not a > 10)              # True
