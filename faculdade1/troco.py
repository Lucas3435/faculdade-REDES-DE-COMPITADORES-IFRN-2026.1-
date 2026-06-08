valor_conta = float(input("valor da conta: ").replace(",", "."))
valor_pago = float(input("valor pago: ").replace(",", "."))
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
