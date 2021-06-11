# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente


def soma(n1, n2):
    # MODO DO PROFESSOR
    vai1 = 0
    resposta = []

    for x, y in zip(n1, n2):
        soma = x + y + vai1

        if soma >= 10:
            vai1 = 1
            soma = soma % 10
        else:
            vai1 = 0

        resposta.append(soma)

    if vai1:
        resposta.append(vai1)

    return resposta


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('soma em listas invertidas')
    test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
    test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])


if __name__ == '__main__':
    main()
