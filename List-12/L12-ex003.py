# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final
def inicio_final(a, b):
    if len(a) % 2 != 0:
        a_init = a[:((len(a)//2) + 1)]
        a_end = a[((len(a)//2) + 1):]
    else:
        a_init = a[:(len(a)//2)]
        a_end = a[(len(a)//2):]

    if len(b) % 2 != 0:
        b_init = b[:((len(b)//2) + 1)]
        b_end = b[((len(b)//2) + 1):]
    else:
        b_init = b[:(len(b)//2)]
        b_end = b[(len(b)//2):]

    return a_init + b_init + a_end + b_end


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('inicio_final')
    test(inicio_final('abcd', 'xy'), 'abxcdy')
    test(inicio_final('abcde', 'xyz'), 'abcxydez')
    test(inicio_final('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
