def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado


def soma_fatoriais_digitos(numero):
    soma = 0

    for digito in str(numero):
        soma += fatorial(int(digito))

    return soma


def verificar_curiosidade(numero):
    if numero == soma_fatoriais_digitos(numero):
        print(numero)
        return True
    return False


def calcular_soma_total(limite):
    soma_total = 0

    for numero in range(3, limite):
        if verificar_curiosidade(numero):
            soma_total += numero

    return soma_total


limite = 10000
soma = calcular_soma_total(limite)

print('Soma total:', soma)
