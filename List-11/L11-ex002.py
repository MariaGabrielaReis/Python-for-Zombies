# B. pontas
# Dada uma string s, retorna uma string com as duas primeiras e as duas
# últimas letras da string original s
# Assim 'palmeiras' retorna 'paas'
# No entanto, se a string tiver menos que 2 letras, retorna uma string vazia
def pontas(s):
  if len(s) < 2:
    return ''
  else:
    return s[:2] + s[-2:]


def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('pontas')
  test(pontas('palmeiras'), 'paas')
  test(pontas('algoritmos'), 'alos')
  test(pontas('a'), '')
  test(pontas('xyz'), 'xyyz')
  
if __name__ == '__main__':
  main()