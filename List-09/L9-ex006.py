# F. middle_way #
# sejam duas listas de inteiros a e b
# retorna uma lista de tamanho 2 contendo os elementos do
# meio de a e b, suponha que as listas tem tamanho ímpar
# middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]
def middle_way(a, b):
  resposta = []
  resposta.append(a[int(len(a)/2)])
  resposta.append(b[int(len(b)/2)])
  return resposta

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('middle_way')
  test(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
  test(middle_way([7, 7, 7], [3, 8, 0]), [7, 8])
  test(middle_way([5, 2, 9], [1, 4, 5]), [2, 4])
  test(middle_way([1, 9, 7], [4, 8, 8]), [9, 8])
  test(middle_way([1, 2, 3], [3, 1, 4]), [2, 1])
  test(middle_way([1, 2, 3], [4, 1, 1]), [2, 1])

if __name__ == '__main__':
  main()
  