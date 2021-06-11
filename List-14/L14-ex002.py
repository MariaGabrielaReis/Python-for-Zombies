# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar

# MEU JEITO INICIAL
def cripto(frase):
    frase = frase.split()

    cripto = ""
    for i in range(len(frase)):
        cripto += str(sorted(list(set(frase[i]))))

    cripto = cripto.replace('[', "").replace(
        ']', " ").replace(', ', "").replace("'", "")

    return cripto[:-1]


def cripto(frase):
    # MEU MODO BASEADO NO DO PROFESSOR
    frase = frase.split()
    resp = []
    for x in frase:
        resp.append(''.join(sorted(set(x))))

    resp = ' '.join(resp)
    return resp


def cripto(frase):
    # MODO DO PROFESSOR
    return ' '.join([''.join(sorted(set(x))) for x in frase.split()])


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('cripto')
    test(cripto('ana e mariana gostam de banana'), 'an e aimnr agmost de abn')
    test(cripto('Batatinha quando nasce esparrama pelo chão'),
         'Bahint adnoqu acens aemprs elop choã')


if __name__ == '__main__':
    main()
