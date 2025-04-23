# Programa 11

# Valores dos lados
lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))


# Verificando se pode formar triangulo
if lado1 + lado2 > lado3 and lado2 + lado1 > lado3:
    print("Pode formar um triangulo!")
else:
    print("Não pode formar um triangulo!") 
    


if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")

elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
    print("Triângulo Isósceles")

elif lado1 != lado2 != lado3:
    print("Triângulo Escaleno")
      


       
    
    