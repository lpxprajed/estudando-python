# %%

for i in range (1,11):
    print(i)
    
# %%

numero = 0

for i in range(1,21):
    if numero % 2 == 0:
        print(numero)
    numero += 1
    
# %%

numero = int(input("Digite um número: "))

for i in range(1,10 +1):
    print(numero * i)
    
# %%

contagem = 10

for i in range(1,contagem + 1):
    print(contagem - i + 1)
    i -= 1 


# %% 

soma = 0

for i in range(1,101):
    soma = i + soma
    print(soma)
    i +=1
    
# %%
total = 0

for i in range(1,6):
    soma = int(input("De um valor"))
    i += 1
    total += soma
    
print(total)
    
# %%
numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")



# %%
