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

# B. x_antes
# Dada uma lista de strings retorna uma lista onde
# todos os elementos que começam com x ficam sorteados antes
# Ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final


def x_antes(words):
    comeca = []
    nao_comeca = []

    for word in words:
        if word.startswith('x'):
            comeca.append(word)
        else:
            nao_comeca.append(word)

    return sorted(comeca) + sorted(nao_comeca)

# C. sort_last
# Dada uma lista de tuplas não vazias retorna uma tupla ordenada
# por ordem crescente do último elemento
# Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retorna
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use key=função que você definiu e que retorna o último elemento


def last(a): return a[-1]  # esta def serve para a letra C


def sort_last(tuples): return sorted(tuples, key=last)


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

    print()
    print('x_antes')
    test(x_antes(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(x_antes(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
