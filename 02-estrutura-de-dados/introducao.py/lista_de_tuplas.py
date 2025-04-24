from random import randint
estudantes = ["Miguel", "Emmilly", "Joao", "Bruna"]
codigo_estudante = []

def gera_codigo():
    return str(randint(0 ,999))

for i in range(len(estudantes)):
    codigo_estudante.append((estudantes[i], estudantes[i][0: 3].upper() + gera_codigo()))

print(codigo_estudante)