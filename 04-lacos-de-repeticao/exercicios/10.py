
soma = 0
cout = 0

while cout < 4:
    altura = float(input("Digite a altura da primeira pessoa: "))
    soma += altura
    cout += 1
    
print(f"{soma:.2f}")