# G. date_fashion
# você e sua/seu namorado(a) vão a um restaurante
# eu e par são as notas das suas roupas de 0 a 10
# quanto maior a nota mais chique vocês estão vestidos
# o resultado é se vocês conseguiram uma mesa no restaurante:
# 0=não 1=talvez e 2=sim
# se a nota da roupa de um dos dois for menor ou igual a 2
# vocês não terão direito à uma mesa (0)
# se as notas são maiores, então caso um dos dois esteja
# bem chique (nota >= 8) então a resposta é sim (2)
# caso contrário a resposta é talvez (1)
# date_fashion(5, 10) -> 2
# date_fashion(5, 2) -> 0
# date_fashion(5, 5) -> 1
def date_fashion(eu, par):
  if eu <= 2 or par <= 2:
    return 0
  elif eu >= 8 or par >= 8:
    return 2
  else:
    return 1

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('date fashion')
  test(date_fashion(5, 10), 2)
  test(date_fashion(5, 2), 0)
  test(date_fashion(5, 5), 1)
  test(date_fashion(3, 3), 1)
  test(date_fashion(10, 2), 0)
  test(date_fashion(2, 9), 0)
  test(date_fashion(9, 9), 2)
  test(date_fashion(10, 5), 2)
  test(date_fashion(2, 2), 0)
  test(date_fashion(3, 7), 1)
  test(date_fashion(2, 7), 0)
  test(date_fashion(6, 2), 0)

if __name__ == '__main__':
  main()
  