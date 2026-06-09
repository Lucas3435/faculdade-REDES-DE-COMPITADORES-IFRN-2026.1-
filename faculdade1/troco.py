def ler_valor(mensagem):
    while True:
        entrada = input(mensagem)
        # Verifica se há mais de uma vírgula
        if entrada.count(",") > 1:
            print("erro: Você digitou mais de uma vírgula!")
            print("   use o formato correto: 100.000,00 (ponto para milhar, vírgula para centavos)")
            continue
        try:
            valor = float(entrada.replace(".", "").replace(",", "."))
            return valor
        except ValueError:
            print("erro: Digite um número válido!")
            continue

valor_conta = ler_valor("valor da conta: ")
valor_pago = ler_valor("valor pago: ")
troco_cent = round((valor_pago - valor_conta) * 100)
if troco_cent < 0:
    print("Pagamento insuficiente")
else:
    troco_reais = troco_cent // 100
    centavos = troco_cent % 100
    notas = [100, 50, 20, 10, 5, 2, 1]
    for n in notas:
        q = troco_reais // n
        troco_reais %= n
        print(f"{q} nota(s) de R$ {n}")
    if centavos:
        print(f"restam {centavos} centavo(s)")
