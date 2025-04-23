ids = []
doces = 0
amargos = 0


for i in range(1,11):
    informe_id = int(input("ID: "))
    
    
    
    if informe_id % 2 == 0:
        doces +=1
    elif informe_id % 2 != 0:
        amargos +=1
    
    ids.append(informe_id)
    
print(ids)
print(doces)
print(amargos)    
