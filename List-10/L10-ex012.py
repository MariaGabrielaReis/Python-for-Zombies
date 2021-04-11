# L. soma_na_lista #
# Verifica se um número é soma de dois elementos distintos de uma lista
# soma_na_lista(5, [1, 2, 3, 4]) -> True
# soma_na_lista(9, [1, 2, 3, 4]) -> False
# soma_na_lista(0, [1, 2, 3, 4]) -> False
# soma_na_lista(8, [1, 2, 3, 4]) -> False
# soma_na_lista(4, [2, 2, 2, 2]) -> False
# soma_na_lista(4, [2, 2, 1, 3]) -> True
def soma_na_lista(n, lista):
  for x in range(len(lista)):
    for i in range(len(lista)-1):
      if n == (lista[x] + lista[i]) and lista[x] != lista[i]:
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
  print ('Soma na lista')
  test(soma_na_lista(5, [1, 2, 3, 4]), True)
  test(soma_na_lista(9, [1, 2, 3, 4]), False)
  test(soma_na_lista(0, [1, 2, 3, 4]), False)
  test(soma_na_lista(8, [1, 2, 3, 4]), False)
  test(soma_na_lista(4, [2, 2, 2, 2]), False)
  test(soma_na_lista(4, [2, 2, 1, 3]), True)
  test(soma_na_lista(42, [40, 2, 3, 39]), True)

if __name__ == '__main__':
  main()