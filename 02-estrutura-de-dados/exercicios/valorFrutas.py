frutas = {"maçã": 2.50,
          "banana": 1.50,
          "laranja": 3.00,
          "uva": 4.00,
          "abacaxi": 5.00}

while True:
 print(frutas.keys())
 fruta = input("Entre com uma fruta: ")
 
 if fruta in frutas:   
    print(frutas[fruta])
 elif fruta == "":
     break
 else:
    print("Fruta invalida")
    continue

