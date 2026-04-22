#Calculadora de media IFRN

print("Este programa tem como finalidade calcular a média das disciplinas e informar a situação do aluno: ")

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))

media = (nota1 * 2 + nota2 * 3) / 5

if media >= 60:
    print(f"Sua média é: {media:.1f}")
    print("Aluno aprovado por média.")
else: 
    print(f"Sua média é: {media:.1f}")
    print("Aluno em prova final.")
    
    notaf = float(input("Digite a nota da prova final: "))
    mediaf = (media + notaf) / 2 

    if mediaf >=60:
        print(f"Sua média é: {mediaf:.1f}")
        print("Aluno aprovado após média final.")
    else:
        print("Aluno reprovado")




