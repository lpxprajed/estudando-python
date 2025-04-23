# Calculadora

num1 = float(input("Informe o número: "))
num2 = float(input("Informe o segundo número: "))

print("1 = + | 2 = - | 3 = x | 4 = /")
qual_operacao =  int(input("Qual operação deseja realizar: "))

if qual_operacao == 1:
    resultado = num1 + num2
    print(resultado)
    if resultado % 2 == 0:
     print("par")
    else:
     print("impar")
     
    if resultado >= 0:
        print("positivo")
        print(type(resultado))
    else:
        print("negativo")
        print(type(resultado))


elif qual_operacao == 2:
    resultado = num1 - num2
    print(resultado)
    if resultado % 2 == 0:
     print("par")
    else:
     print("impar")
     
    if resultado >= 0:
        print("positivo")
        print(type(resultado))
    else:
        print("negativo")
        print(type(resultado))
    
elif qual_operacao == 3:
    resultado = num1 * num2
    print(resultado) 
    if resultado % 2 == 0:
     print("par")
    else:
     print("impar") 
    
    if resultado >= 0:
        print("positivo")
        print(type(resultado))
    else:
        print("negativo")
        print(type(resultado))
        
elif qual_operacao == 4:
    resultado = num1 / num2
    print(resultado)
    if resultado % 2 == 0:
     print("par")
    else:
     print("impar") 
    
    if resultado >= 0:
        print("positivo")
        print(type(resultado))
    else:
        print("negativo")   
        print(type(resultado))     

else:
    print("Invalida")
