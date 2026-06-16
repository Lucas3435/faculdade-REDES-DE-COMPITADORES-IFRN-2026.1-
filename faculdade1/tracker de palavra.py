# tracker de palavras v2
# conta quantas vezes cada palavra aparece no texto e mostra em ordem decrescente.

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque non sapien et neque laoreet cursus at at nisl.
Vestibulum ut lacus sem. Suspendisse in sapien purus. Proin nec rhoncus orci. Mauris dapibus ex urna, non dapibus risus scelerisque in.
Praesent quis egestas metus, vitae sollicitudin turpis. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis odio massa, pulvinar eu maximus vitae, imperdiet non est. Fusce ultricies fringilla nunc eu fringilla.
Etiam eget tempor risus, non dictum mauris.
Vivamus quis elit commodo, fringilla libero in, convallis sem. Aenean porttitor gravida dolor, et faucibus ex egestas eget.
Cras fermentum pretium rutrum. Aliquam at lectus velit. Mauris tristique nec tortor nec commodo.
Etiam euismod finibus imperdiet. Praesent lobortis sodales tortor, non porttitor nunc fermentum eu. Nam varius a odio non porttitor.
Aenean pellentesque urna vel ante lobortis, tristique congue lorem auctor. Curabitur justo arcu, venenatis quis pulvinar in, ultrices aliquet justo.
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam erat volutpat. Maecenas egestas elit arcu, vel accumsan eros suscipit nec.
Donec orci diam, dignissim vitae mollis ut, venenatis nec justo. Nulla auctor non tortor nec vehicula. Suspendisse mattis libero at lectus volutpat auctor.
Mauris eget pulvinar ante."""

# normaliza o texto
texto = texto.lower()
for caractere in ",.;:":
    texto = texto.replace(caractere, "")

palavras = texto.split()

# conta as palavras
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

# ordena da maior para a menor contagem
resultado = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

# exibe o resultado
for palavra, quantidade in resultado:
    print(f"{palavra}: {quantidade}")
