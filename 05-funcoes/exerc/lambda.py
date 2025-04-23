palavras = ["python", "é", "legal"]
# Faça com lambda e map

maisculas = list(map(lambda x: x.upper(), palavras))
print(maisculas)
