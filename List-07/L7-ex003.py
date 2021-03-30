# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums
def array_count9(nums):
  contador = 0
  for num in nums:
    if num == 9: 
      contador += 1
  return contador

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Array count 9')
  test(array_count9([1, 99, 9]), 1)
  test(array_count9([1, 9, 9]), 2)
  test(array_count9([1, 9, 9, 3, 9]), 3)
  test(array_count9([1, 2, 3]), 0)
  test(array_count9([]), 0)
  test(array_count9([4, 2, 4, 3, 1]), 0)
  test(array_count9([9, 2, 99, 3, 1]), 1)

if __name__ == '__main__':
  main()
  