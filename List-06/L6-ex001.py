# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
  if feriado or not dia_semana:
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
  print ('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)

if __name__ == '__main__':
  main()
  