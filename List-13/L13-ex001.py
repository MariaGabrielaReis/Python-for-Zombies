# A. fim_igual
# Dada uma lista de strings, retorna o número de strings
# com tamanho >= 2 onde o primeiro e o último caracteres são iguais
# Exemplo: ['aba', 'xyz', 'aa', 'x', 'bbb'] retorna 3
def fim_igual(words):
    contador = 0
    for palavra in words:
        if len(palavra) >= 2:
            if palavra[0] == palavra[-1]:
                contador += 1
    return contador


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('fim_igual')
    test(fim_igual(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(fim_igual(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(fim_igual(['aaa', 'be', 'abc', 'hello']), 1)


if __name__ == '__main__':
    main()
