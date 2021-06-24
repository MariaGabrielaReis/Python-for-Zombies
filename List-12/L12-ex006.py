# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
    response = 0
    m = 0

    while response == 0:
        pot = str(2**m)
        if str(pot[:len(str(n))]) == str(n):
            response = m
        else:
            m += 1
    return response


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('inicio p2')
    test(inip2(65), 16)
    test(inip2(7), 46)
    test(inip2(133), 316)
    test(inip2(1024), 10)


if __name__ == '__main__':
    main()
