# B. same_first_last #
# retorna True se a lista nums
# possui pelo menos um elemento
# e o primeiro elemento é igual
# ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
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
  print ('Same_first_last')
  test(same_first_last([1, 2, 3]), False)
  test(same_first_last([1, 2, 3, 1]), True)
  test(same_first_last([1, 2, 1]), True)
  test(same_first_last([7]), True)
  test(same_first_last([]), False)
  test(same_first_last([7, 7]), True)

if __name__ == '__main__':
  main()
  