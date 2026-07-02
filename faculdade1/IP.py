import socket

rede = socket.gethostbyname_ex(socket.getfqdn())
ips = rede[2]

for ip in ips:
    partes = ip.split(".")
    primeiro = int(partes[0])
    segundo = int(partes[1])

    if primeiro == 10:
        tipo = "classe A privado"
    elif primeiro == 127:
        tipo = "loopback"
    elif primeiro == 172 and 16 <= segundo <= 31:
        tipo = "classe B privado"
    elif primeiro == 169 and segundo == 254:
        tipo = "APIPA privado"
    elif primeiro == 192 and segundo == 168:
        tipo = "classe C privado"
    else:
        tipo = "não classificado"

    print(ip, "->", tipo)
