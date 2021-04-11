# J. sum13 #
# retorna a soma dos números de uma lista
# 13 dá azar, você deverá ignorar o 13 e todos os números à sua direita
# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6
# sum13([13, 1, 2, 3, 4]) -> 0
def sum13(nums):
  soma = 0
  for num in nums:
    if num == 13:
      return soma
    else:
      soma += num
  return soma

  
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Sum13')
  test(sum13([1, 2, 2, 1]), 6)
  test(sum13([1, 1]), 2)
  test(sum13([1, 2, 2, 1, 13]), 6)
  test(sum13([1, 2, 13, 2, 1, 13]), 3)
  test(sum13([13, 1, 2, 13, 2, 1, 13]), 0)
  test(sum13([]), 0)
  test(sum13([13]), 0)
  test(sum13([13, 13]), 0)
  test(sum13([13, 0, 13]), 0)
  test(sum13([13, 1, 13]), 0)
  test(sum13([5, 7, 2]), 14)
  test(sum13([5, 13, 2]), 5)
  test(sum13([0]), 0)
  test(sum13([13, 0]), 0)

if __name__ == '__main__':
  main()