import random

palavras = ["galalau", "piton", "dinossauro", "sao paulo", "corinthians"]
sorteada = palavras [   random.randint(0, 4)   ]

digitada = "_" * len(sorteada)   

while digitada != sorteada:
    print(digitada)
    letra = input("digite uma letra: ")
    if letra in sorteada: 
        nova = ""
        for i in range (len(sorteada)):
            if letra == sorteada [i]:
                nova += letra
            else :
                nova += digitada [i]
        digitada = nova
    else:   print ("parabens voce acertou! a palavra era " + sorteada)
