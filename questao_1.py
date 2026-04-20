import random

numero_sorteado = random.randint(1, 100)
limite_inferior = 1
limite_superior = 100

# Tentativa 1
print(f"O número está entre {limite_inferior} e {limite_superior}. Digite sua tentativa:")
tentativa_1 = int(input())

if tentativa_1 == numero_sorteado:
    print(f"Parabéns! Você acertou! O número era {numero_sorteado}")
else:
    if tentativa_1 < numero_sorteado:
        limite_inferior = tentativa_1
    else:
        limite_superior = tentativa_1
    
    # Tentativa 2
    print(f"Errado! O número está entre {limite_inferior} e {limite_superior}. Digite sua tentativa:")
tentativa_2 = int(input())
    
    if tentativa_2 == numero_sorteado:
        print(f"Parabéns! Você acertou! O número era {numero_sorteado}")
    else:
        if tentativa_2 < numero_sorteado:
            limite_inferior = tentativa_2
        else:
            limite_superior = tentativa_2
        
        # Tentativa 3
        print(f"Errado! O número está entre {limite_inferior} e {limite_superior}. Digite sua tentativa:")
tentativa_3 = int(input())
        
        if tentativa_3 == numero_sorteado:
            print(f"Parabéns! Você acertou! O número era {numero_sorteado}")
        else:
            if tentativa_3 < numero_sorteado:
                limite_inferior = tentativa_3
            else:
                limite_superior = tentativa_3
            
            # Tentativa 4
            print(f"Errado! O número está entre {limite_inferior} e {limite_superior}. Digite sua tentativa:")
tentativa_4 = int(input())
            
            if tentativa_4 == numero_sorteado:
                print(f"Parabéns! Você acertou! O número era {numero_sorteado}")
            else:
                print(f"Você perdeu! O número era {numero_sorteado}. Você usou todas as 4 tentativas!")