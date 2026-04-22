def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Erro: o valor deve ser maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Erro: o valor deve ser menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro: por favor, digite um numero inteiro valido.")


def ler_float(mensagem, minimo=None):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if minimo is not None and valor < minimo:
                print(f"Erro: o valor deve ser maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: por favor, digite um numero valido.")


def formatar_tempo(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return f"{horas:02d}:{minutos:02d}"


print(" Computador de Bordo Inteligente ")
print("Informe os dados da viagem no formato solicitado.")
print()

hora_partida = ler_inteiro("Hora de Partida (hora, 0 a 23): ", 0, 23)
minuto_partida = ler_inteiro("Hora de Partida (minuto, 0 a 59): ", 0, 59)

hora_chegada = ler_inteiro("Hora de Chegada (hora, 0 a 23): ", 0, 23)
minuto_chegada = ler_inteiro("Hora de Chegada (minuto, 0 a 59): ", 0, 59)

tempo_descanso = ler_inteiro("Tempo de Descanso (em minutos): ", 0)
combustivel_gasto = ler_float("Combustivel Gasto (em litros): ", 0)
preco_litro = ler_float("Preco do Litro (em R$): ", 0)
distancia_percorrida = ler_float("Distancia Percorrida (em Km): ", 0)

inicio_minutos = hora_partida * 60 + minuto_partida
fim_minutos = hora_chegada * 60 + minuto_chegada

if fim_minutos <= inicio_minutos:
    raise ValueError("Erro: a hora de chegada deve ser maior que a hora de partida.")

tempo_total_min = fim_minutos - inicio_minutos

if tempo_descanso > tempo_total_min:
    raise ValueError("Erro: o tempo de descanso nao pode ser maior que o tempo total da viagem.")

tempo_movimento_min = tempo_total_min - tempo_descanso

tempo_total_h = tempo_total_min / 60
tempo_movimento_h = tempo_movimento_min / 60

if tempo_total_h == 0:
    raise ValueError("Erro: tempo total da viagem invalido para calculos.")

velocidade_media_global = distancia_percorrida / tempo_total_h
custo_total = combustivel_gasto * preco_litro

if combustivel_gasto == 0:
    desempenho = 0.0
else:
    desempenho = distancia_percorrida / combustivel_gasto

if tempo_movimento_h == 0:
    consumo_litros_hora = 0.0
else:
    consumo_litros_hora = combustivel_gasto / tempo_movimento_h

print("\n=== Relatorio da Viagem ===")
print(f"Tempo Total de Viagem: {formatar_tempo(tempo_total_min)}")
print(f"Tempo em Movimento: {formatar_tempo(tempo_movimento_min)}")
print(f"Velocidade Media Global: {velocidade_media_global:.2f} Km/h")
print(f"Custo Total da Viagem: R$ {custo_total:.2f}")
print(f"Desempenho: {desempenho:.2f} Km/L")
print(f"Consumo: {consumo_litros_hora:.2f} L/h")