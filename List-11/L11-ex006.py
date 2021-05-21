# F. busca
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
def busca(frase, palavra):
    i = 0
    contador = 0

    while i < len(frase):
        if frase[i:i+len(palavra)] == palavra:
            contador += 1
        i += 1
    return contador


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s'
          % (prefixo, repr(obtido), repr(esperado)))


def main():
    print('busca')
    test(busca('ana e mariana gostam de banana', 'ana'), 4)
    test(busca('uma arara ou duas araras', 'ara'), 4)


if __name__ == '__main__':
    main()
