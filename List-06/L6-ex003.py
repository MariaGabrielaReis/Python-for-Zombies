# C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
  if a == b:
    return (a+b)*2
  return a+b

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Soma dobro')
  test(soma_dobro(1, 2), 3)
  test(soma_dobro(3, 2), 5)
  test(soma_dobro(2, 2), 8)
  test(soma_dobro(-1, 0), -1)
  test(soma_dobro(0, 0), 0)
  test(soma_dobro(0, 1), 1)

if __name__ == '__main__':
  main()
