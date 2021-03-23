# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
  if a == 10 or b ==10:
    return True
  if a + b == 10:
    return True
  return False

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Dez')
  test(dez(9, 10), True)
  test(dez(9, 9), False)
  test(dez(1, 9), True)
  test(dez(10, 1), True)
  test(dez(10, 10), True)
  test(dez(8, 2), True)
  test(dez(8, 3), False)
  test(dez(10, 42), True)
  test(dez(12, -2), True)

if __name__ == '__main__':
  main()
  