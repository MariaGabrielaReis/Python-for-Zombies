# A. first_last6
# verifica se 6 é o primeiro ou último elemento da lista nums
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([3, 2, 1]) -> False
def first_last6(nums): #
  if nums[0] == 6 or nums[-1] == 6:
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
  print ('First_last6')
  test(first_last6([1, 2, 6]), True)
  test(first_last6([6, 1, 2, 3]), True)
  test(first_last6([3, 2, 1]), False)
  test(first_last6([3, 6, 1]), False)
  test(first_last6([3, 6]), True)
  test(first_last6([6]), True)
  test(first_last6([3]), False)

if __name__ == '__main__':
  main()
  