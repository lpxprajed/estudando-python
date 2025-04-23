""" 
3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.


"""

dados = 15
contador = 0

while contador < dados:
    nota = int(input("Avalie de 0 a 5: "))
    if nota > 5 or nota  < 0:
        print("Nota invalida.")
        continue
    else:
        print("Nota recebida.")    
    
      
    contador += 1
    
print("Obrigado pela avaliação.")    