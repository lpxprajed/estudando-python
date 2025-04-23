nota_1 = float(input("Informe a 1 primeira nota do aluno: "))
nota_2 = float(input("Informe a 2 segunda nota do aluno: "))
nota_3 = float(input("Informe a 3 terceira nota do aluno: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 6: 
 print(f"Aluno aprovado! {media:.2} pontos")
elif media >= 4:
 print(f"Aluno em recuperação! {media:.2} pontos")
else:
 print(f"Aluno reprovado! {media:.2} pontos")