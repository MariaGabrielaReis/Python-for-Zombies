# E. hello_name
# seja uma string name
# hello_name('Bob') -> 'Hello Bob!'
# hello_name('Alice') -> 'Hello Alice!'
# hello_name('X') -> 'Hello X!'
def hello_name(name):
  return f'Hello {name}!'

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Hello Name')
  test(hello_name('Bob'), 'Hello Bob!')
  test(hello_name('Alice'), 'Hello Alice!')
  test(hello_name('X'), 'Hello X!')
  test(hello_name('Hello'), 'Hello Hello!')

if __name__ == '__main__':
  main()
  