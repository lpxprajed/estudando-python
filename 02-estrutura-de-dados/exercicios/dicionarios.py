dados_miguel = {
    "nome": "Miguel",
    "sobrenome": "Lopes",
    "idade": 17,
    "filhos": False,
    "formação": ["desenvolvimento de sistemas", "ciencias de dados"],
    "cargos": [
        {"nome": "estagiario", "empresa": "mercantil", "salario": 2200},
        {"nome": "da jr", "empresa": "itau", "salario": 5000},
        {"nome": "da pl", "empresa": "inter", "salario": 8000},
        {"nome": "da sr", "empresa": "oracle", "salario": 15000}  
    ]
}

# print(dados_miguel["cargos"][-1]["empresa"])

# dados_miguel["estado civil"] = "casado"
# print(dados_miguel)

print("Chaves", dados_miguel.keys())

print("Valores", dados_miguel.values())

print("intens", dados_miguel.items())


# Pegano chave e valores dentro de um dicionario
for chave, valor in dados_miguel.items(): 
    print(chave, "→ ", valor)