# %%
eu = ["Miguel", "Lopes", 17, "Namorando", True,"Analista"]
emmilly = ["Emmilly","Almeida",17,"Namorando", True, "Engenheira"]

print(eu[1])
print(eu[2])

print(emmilly[0:3])

# %%

idade = [17,17,18,20,12,19]

len(idade) # Len mostra quantos elementos tem dento de uma lista
sum(idade) # Sum soma todas os valores dentro de uma lista
min(idade) 
max(idade)

media = sum(idade) / len(idade)
print(f"{media:.2f}")

# %%

miguel = [
    "Miguel",
    "Lopes"
    ,"Casado"
    ,[1200,3500,500]
    ,["Estagio","An Junior", "An Pleno"],
    ["Emmilly","Fabiana","Alessanda"]
    ]

print(miguel)
nome = miguel[0]
sobrenome = miguel[1]
status = miguel[2]

salario = miguel[3]
cargos = miguel[4]
familia = miguel[5]

# Qual o nome da sua namorada? 

miguel[5][0]

# Qual o seu cargo e salario?

print(f"Cargo: {cargos[1]} Salario {salario[1]}")



# %%

numeros = [1,5,7,9,12,35,76]
numeros[::2]

# %%
