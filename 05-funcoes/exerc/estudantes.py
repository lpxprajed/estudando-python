estudantes = {
    "miguel": {"notas": [4,3,5,6]},
    "emmilly": {"notas": [7,7,8,9]},
    "pedro": {"notas": [7,4,3,3]}
}

def notas(x):
    maior_nota = max(x)
    menor_notas = min(x)
    media = sum(x) / len(x)
    if media >= 6:
        aprovado = "Sim"
    else:
        aprovado = "Não"
    
    return maior_nota,menor_notas, media, aprovado



for nome, dados in estudantes.items():
    maior,menor, media, aprovado = notas(dados["notas"])
    print(f"Aluno: {nome}")
    print(f"  Maior nota: {maior}")
    print(f"  Menor nota: {menor}")
    print(f"  Média: {media:.2f}")
    print(f"  Aprovado: {aprovado}")
    print("-" * 30)