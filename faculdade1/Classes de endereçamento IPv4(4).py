def classificar_ipv4(a, b, c, d):
	if not all(0 <= n <= 255 for n in (a, b, c, d)):
		return "endereço inválido"

	if (a, b, c, d) == (0, 0, 0, 0):
		return "endereço default de rede"
	if a == 10:
		return "endereço reservado classe A"
	if a == 127:
		return "endereço de loopback"
	if a == 169 and b == 254:
		return "endereço de APIPA"
	if a == 172 and 16 <= b <= 31:
		return "endereço reservado classe B"
	if a == 192 and b == 168:
		return "endereço reservado classe C"
	if (a, b, c, d) == (255, 255, 255, 255):
		return "endereço de broadcast"
	if 1 <= a <= 126:
		return "endereço classe A"
	if 128 <= a <= 191:
		return "endereço classe B"
	if 192 <= a <= 223:
		return "endereço classe C"
	if 224 <= a <= 239:
		return "endereço de multicast"

	return "não classificado"


octeto1 = int(input())
octeto2 = int(input())
octeto3 = int(input())
octeto4 = int(input())

print(classificar_ipv4(octeto1, octeto2, octeto3, octeto4))
