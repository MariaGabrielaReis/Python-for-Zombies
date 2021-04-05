# H. squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
  if is_summer:
    if temp >= 60 and temp <= 100:
      return True
    else:
      return False
  else:
    if temp >= 60 and temp <= 90:
      return True
    else:
      return False

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('squirrel_play')
  test(squirrel_play(70, False), True)
  test(squirrel_play(95, False), False)
  test(squirrel_play(95, True), True)
  test(squirrel_play(90, False), True)
  test(squirrel_play(90, True), True)
  test(squirrel_play(50, False), False)
  test(squirrel_play(50, True), False)
  test(squirrel_play(100, False), False)
  test(squirrel_play(100, True), True)
  test(squirrel_play(105, True), False)
  test(squirrel_play(59, False), False)	
  test(squirrel_play(59, True), False)	
  test(squirrel_play(60, False), True)

if __name__ == '__main__':
  main()
  