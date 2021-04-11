# D. double_char #
# retorna os caracteres da string original duplicados
# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'
def double_char(s):
  resposta = ""
  for caractere in s:
    resposta += caractere + caractere
  return resposta


def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print('%s obtido: %s esperado: %s'
        % (prefixo, repr(obtido), repr(esperado)))


def main():
  print('Double_char')
  test(double_char('The'), 'TThhee')
  test(double_char('AAbb'), 'AAAAbbbb')
  test(double_char('Hi-There'), 'HHii--TThheerree')
  test(double_char('Word!'), 'WWoorrdd!!')
  test(double_char('!!'), '!!!!')
  test(double_char(''), '')
  test(double_char('a'), 'aa')
  test(double_char('.'), '..')
  test(double_char('aa'), 'aaaa')


if __name__ == '__main__':
  main()
