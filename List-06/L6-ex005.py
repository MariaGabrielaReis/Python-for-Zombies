# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  if falando:
    if hora < 7 or hora > 20:
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
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False)
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)

if __name__ == '__main__':
  main()
  