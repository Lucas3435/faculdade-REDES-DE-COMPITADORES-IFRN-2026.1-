nomes = [
    "ALESSANDRA", "BERNARDO", "CLEMENTINA", "DOMINGOS", "ESMERALDA",
    "FRANCISCO", "GABRIELLE", "HENRIQUETA", "ISADORA", "JEREMIAS",
    "KATARINA", "LEONARDO", "MARIANA", "NICOLAU", "OLIMPIA",
    "PENELOPE", "QUINTILHA", "RAFAELLY", "SANDRINO", "TEODORO",
    "VALENTINA", "WILSON", "XIMENA", "YASMIN", "ZACHARY",
    "ALBERTO", "BARBARA", "CRISTIANO", "DIAMANTINA", "EMANUELLE",
    "FERNANDA", "GUILHERME", "HELENA", "IGOR", "JULIANNA",
    "KLEBER", "LUCIANA", "MAXIMILIANO", "NATALIA", "OTAVIO",
    "PATRICIA", "QUITERIA", "RODRIGO", "SILVANA", "THIAGO",
    "URBANO", "VICTORIA", "WANDERLEY", "XAVIER", "YASMIM"
]

def valor_nome(nome):
    soma = 0
    for letra in nome:
        soma += ord(letra) - ord('A') + 1
    return soma

valores = []
for nome in nomes:
    valores.append(valor_nome(nome))

valores.sort()

print(valores[31])
