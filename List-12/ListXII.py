# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
    if len(s) >= 3:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s

# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'


def not_bad(s):
    index_not = s.find('not')
    index_bad = s.find('bad')

    if index_not < index_bad and index_bad > 1:
        return s[:index_not] + 'good' + s[index_bad+3:]
    else:
        return s

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

# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três


def zf(n):
    zeros = 0
    n1 = str(n)  # converte em string
    n1 = n1[::-1]  # inverte as posições
    for number in n1:
        if number == '0':
            zeros += 1
        else:
            return zeros


# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19


def conta2(n):
    cont = 0
    for k in range(n):
        cont = cont + str(k).count('2')
    return cont

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
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('inicio_final')
    test(inicio_final('abcd', 'xy'), 'abxcdy')
    test(inicio_final('abcde', 'xyz'), 'abcxydez')
    test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

    print()
    print('zeros finais')
    test(zf(10100100010000), 4)
    test(zf(90000000000000000010), 1)

    print()
    print('conta 2')
    test(conta2(20), 2)
    test(conta2(999), 300)
    test(conta2(555), 216)

    print()
    print('inicio p2')
    test(inip2(7), 46)
    test(inip2(133), 316)
    test(inip2(1024), 10)


if __name__ == '__main__':
    main()
