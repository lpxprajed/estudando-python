nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
corrigindo = list(map(lambda x,y: x.title() + " " + y.title(), nomes, sobrenomes))
print(corrigindo)

