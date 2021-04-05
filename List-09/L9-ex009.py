# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocide <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0 
def pego_correndo(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed > 65 and speed <= 85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed > 60 and speed <= 80:
      return 1
    else:
      return 2

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Pego correndo')
  test(pego_correndo(60, False), 0)
  test(pego_correndo(65, False), 1)
  test(pego_correndo(65, True), 0)
  test(pego_correndo(80, False), 1)
  test(pego_correndo(85, False), 2)
  test(pego_correndo(85, True), 1)
  test(pego_correndo(70, False), 1)
  test(pego_correndo(75, False), 1)
  test(pego_correndo(75, True), 1)
  test(pego_correndo(40, False), 0)
  test(pego_correndo(40, True), 0)
  test(pego_correndo(90, False), 2)

if __name__ == '__main__':
  main()
  