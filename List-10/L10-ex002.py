# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0
def lone_sum(a, b, c):
  if  a == b and b == c:
    return 0
  elif a == b:
    return c 
  elif a == c: 
    return b
  elif b == c:
    return a
  else:
    return a+b+c


def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Lone Sum')
  test(lone_sum(1, 2, 3), 6)
  test(lone_sum(3, 2, 3), 2)
  test(lone_sum(3, 3, 3), 0)
  test(lone_sum(9, 2, 2), 9)
  test(lone_sum(2, 2, 9), 9)
  test(lone_sum(2, 9, 2), 9)
  test(lone_sum(2, 9, 3), 14)
  test(lone_sum(4, 2, 3), 9)
  test(lone_sum(1, 3, 1), 3)

if __name__ == '__main__':
  main()