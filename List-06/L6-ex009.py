# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  if len(s)<=1:
    return s
  else:
    return s[-1] + s[1:-1] + s[0] 

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Troca letras')
  test(troca('code'), 'eodc')	    
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')
  
if __name__ == '__main__':
  main()
