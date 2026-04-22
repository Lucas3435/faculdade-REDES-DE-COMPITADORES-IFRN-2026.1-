valor_carro = float(input("Qual o valor do carro a segurar? R$ "))
idade_condutor = int(input("Qual a idade do condutor? "))

if idade_condutor < 18:
	print("Contratacao rejeitada.")
	raise SystemExit

valor_base = valor_carro * 0.05

if 18 <= idade_condutor <= 24:
	valor_base *= 1.20
elif idade_condutor > 60:
	valor_base *= 1.10

uso_veiculo = input("O uso do veiculo e para Trabalho (T) ou Lazer (L)? ").strip().upper()
while uso_veiculo not in ("T", "L"):
	uso_veiculo = input("Resposta invalida. Digite T para Trabalho ou L para Lazer: ").strip().upper()

if uso_veiculo == "T":
	valor_base += 300
else:
	valor_base -= 100

acidentes = int(input("Numero de acidentes no ultimo ano? "))
valor_base += acidentes * 300

if valor_base < 7000:
	print(f"Seu seguro pode ser contratado. Valor do seguro: R$ {valor_base:.2f}")
else:
	print("O seguro esta sob analise.")
