# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'
def first_half(s):
  metade = int(len(s)/2)
  return s[:metade]

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('First Half')
  test(first_half('WooHoo'), 'Woo')
  test(first_half('HelloThere'), 'Hello')
  test(first_half('abcdef'), 'abc')
  test(first_half('ab'), 'a')
  test(first_half(''), '')
  test(first_half('0123456789'), '01234')
  test(first_half('kitten'), 'kit')

if __name__ == '__main__':
  main()
  