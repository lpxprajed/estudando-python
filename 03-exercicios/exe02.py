# Exercicio 02

# Seguranças
quantidades_segurancas = 5 
salario_segurança = 3000

# Docente
quantidades_docentes = 16
salario_docente = 6000

# Diretoria
quantidades_diretores = 1
salario_diretor = 12500

# A quantidade total de emepregados

quantidade_funcionarios = quantidades_segurancas + quantidades_diretores + quantidades_docentes
print(f"Total de empregados: {quantidade_funcionarios}")

# A diferença entre o salário mais baixo e mais alto

diferença_salarial = salario_diretor - salario_segurança
print(f"Diferença do maior salario para o menor: R$ {diferença_salarial}")

# A média ponderada da faixa salarial da escola.

media_salarial = (quantidades_segurancas * salario_segurança + quantidades_docentes * salario_docente + quantidades_diretores * salario_diretor) / (quantidade_funcionarios)
print(f"Media salarial: R$ {media_salarial:.2f}")
