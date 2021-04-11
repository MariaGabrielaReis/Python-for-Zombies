# A. near_ten #
# Seja um n não negativo, retorna True se o número está a distância de
# pelo menos dois de um múltiplo de dez. Use a função resto da divisão.
# near_ten(12) -> True
# near_ten(17) -> False
# near_ten(19) -> True
def near_ten(n):
  if n % 10 <= 2 or n % 10 >= 8:
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
  print ('Near_ten')
  test(near_ten(12), True)
  test(near_ten(17), False)
  test(near_ten(19), True)
  test(near_ten(31), True)
  test(near_ten(6), False)
  test(near_ten(10), True)
  test(near_ten(11), True)
  test(near_ten(21), True)
  test(near_ten(22), True)
  test(near_ten(23), False)
  test(near_ten(54), False)
  test(near_ten(155), False)
  test(near_ten(158), True)
  test(near_ten(3), False)
  test(near_ten(1), True)

if __name__ == '__main__':
  main()