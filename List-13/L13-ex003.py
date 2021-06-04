# C. sort_last
# Dada uma lista de tuplas não vazias retorna uma tupla ordenada
# por ordem crescente do último elemento
# Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retorna
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use key=função que você definiu e que retorna o último elemento


def sort_last(tuples): return sorted(tuples, key=last)


def last(a): return a[-1]


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
