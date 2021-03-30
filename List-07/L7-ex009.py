# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# without_end('Hello') -> 'ell'
# without_end('python') -> 'ytho'
# without_end('coding') -> 'odin'
def sem_pontas(s):
  sem_fim = s[:-1]
  sem_comeco_e_sem_fim = sem_fim[1:]
  return sem_comeco_e_sem_fim

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Sem Pontas')
  test(sem_pontas('Hello'), 'ell')
  test(sem_pontas('Python'), 'ytho')
  test(sem_pontas('coding'), 'odin')
  test(sem_pontas('code'), 'od')
  test(sem_pontas('ab'), '')
  test(sem_pontas('Chocolate!'), 'hocolate')
  test(sem_pontas('kitten'), 'itte')
  test(sem_pontas('woohoo'), 'ooho')

if __name__ == '__main__':
  main()
  