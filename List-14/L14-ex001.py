# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
    return list(set(nums))


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('remove_iguais')
    test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
    test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
    test(remove_iguais([]), [])


if __name__ == '__main__':
    main()
