# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2

# MEU MODO
def derivada(coef):
    resp = []
    for x in range(len(coef)):
        resp.append(x * coef[x])
    return resp[1:]


def derivada(coef):
    # MODO DO PROFESSOR
    d = []
    for potencia, coeficiente in enumerate(coef):
        d.append(potencia*coeficiente)
    return d[1:]


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('derivada de polinômio')
    test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
    test(derivada([4, 16, 1]), [16, 2])


if __name__ == '__main__':
    main()
