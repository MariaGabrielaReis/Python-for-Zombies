# FATEC Professor Jessen Vidal
# Nome: Maria Gabriela Garcia dos Santos Reis
# Turma: 1º DSM /2021
# Disciplina: Algoritmos e Lógica de Programação
# -----------------------------------------------------------------------
# A. donuts
# Para um inteiro n retorna uma string na forma 'Número de donuts: <n>'
# onde n é o valor passado como argumento.
# Caso n >= 10 devo retornar 'muitos' em lugar do número.
# donuts(5) returns 'Número de donuts: 5'
# donuts(23) returns 'Número de donuts: muitos'
def donuts(n):
    if n >= 10:
        n = 'muitos'
    return f'Número de donuts: {n}'

# -----------------------------------------------------------------------
# B. pontas
# Dada uma string s, retorna uma string com as duas primeiras e as duas
# últimas letras da string original s
# Assim 'palmeiras' retorna 'paas'
# No entanto, se a string tiver menos que 2 letras, retorna uma string vazia


def pontas(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

# -----------------------------------------------------------------------
# C. fixa_primeiro
# Dada uma string s, retorna uma string onde todas as ocorrências
# do primeiro caracter são trocados por '*', exceto para o primeiro
# Assim 'abacate' retorna 'ab*c*te'
# Dica: use s.replace(stra, strb)


def fixa_primeiro(s):
    primeira_letra = s[0]
    s = s.replace(primeira_letra, '*')
    return primeira_letra + s[1:]

# -----------------------------------------------------------------------
# D. mistura2
# Sejam duas strings a e b
# Retorno uma string '<a> <b>' separada por um espaço
# com as duas primeiras letras trocadas de cada string
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'


def mistura2(a, b):
    a, b = b[:2] + a[2:], a[:2] + b[2:]
    return a + ' ' + b

# -----------------------------------------------------------------------
# E. palindrome
# Verifique se uma string é palíndrome
#   palindrome('asa') True
#   palindrome('casa') False


def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

# -----------------------------------------------------------------------
# F. busca
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4


def busca(frase, palavra):
    i = 0
    contador = 0

    while i < len(frase):
        if frase[i:i+len(palavra)] == palavra:
            contador += 1
        i += 1
    return contador

# -----------------------------------------------------------------------


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s'
          % (prefixo, repr(obtido), repr(esperado)))


def main():
    print('donuts')
    test(donuts(4), 'Número de donuts: 4')
    test(donuts(9), 'Número de donuts: 9')
    test(donuts(10), 'Número de donuts: muitos')
    test(donuts(99), 'Número de donuts: muitos')

    print()
    print('pontas')
    test(pontas('palmeiras'), 'paas')
    test(pontas('algoritmos'), 'alos')
    test(pontas('a'), '')
    test(pontas('xyz'), 'xyyz')

    print()
    print('fixa_primeiro')
    test(fixa_primeiro('babble'), 'ba**le')
    test(fixa_primeiro('aardvark'), 'a*rdv*rk')
    test(fixa_primeiro('google'), 'goo*le')
    test(fixa_primeiro('donut'), 'donut')

    print()
    print('mistura2')
    test(mistura2('mix', 'pod'), 'pox mid')
    test(mistura2('dog', 'dinner'), 'dig donner')
    test(mistura2('gnash', 'sport'), 'spash gnort')
    test(mistura2('pezzy', 'firm'), 'fizzy perm')

    print()
    print('palindrome')
    test(palindrome('asa'), True)
    test(palindrome('casa'), False)

    print()
    print('busca')
    test(busca('ana e mariana gostam de banana', 'ana'), 4)
    test(busca('uma arara ou duas araras', 'ara'), 4)


if __name__ == '__main__':
    main()
