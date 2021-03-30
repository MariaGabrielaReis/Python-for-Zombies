# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
  return s[-2:]*3

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Extra End')
  test(extra_end('Hello'), 'lololo')
  test(extra_end('ab'), 'ababab')
  test(extra_end('Hi'), 'HiHiHi')
  test(extra_end('Candy'), 'dydydy')
  test(extra_end('Code'), 'dedede')

if __name__ == '__main__':
  main()
  