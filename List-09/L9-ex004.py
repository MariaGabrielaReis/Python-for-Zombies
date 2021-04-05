# D. maior_ponta #
# Dada uma lista não vazia, cria uma nova lista onde todos
# os elementos são o maior das duas pontas
# obs.: não é o maior de todos, mas entre as duas pontas
# maior_ponta([1, 2, 3]) -> [3, 3, 3]
# maior_ponta([1, 3, 2]) -> [2, 2, 2]
def maior_ponta(nums):
  resposta = []
  if nums[0] > nums[-1]:
    for x in range(len(nums)):
      resposta.append(nums[-0])
  if nums[-1] >= nums[0]:
    for x in range(len(nums)):
      resposta.append(nums[-1])
  return resposta

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Maior_ponta')
  test(maior_ponta([1, 2, 3]), [3, 3, 3])
  test(maior_ponta([11, 5, 9]), [11, 11, 11])
  test(maior_ponta([2, 11, 3]), [3, 3, 3])
  test(maior_ponta([11, 3, 3]), [11, 11, 11])
  test(maior_ponta([3, 11, 11]), [11, 11, 11])
  test(maior_ponta([2, 2, 2]), [2, 2, 2])
  test(maior_ponta([2, 11, 2]), [2, 2, 2])
  test(maior_ponta([0, 0, 1]), [1, 1, 1])

if __name__ == '__main__':
  main()
  