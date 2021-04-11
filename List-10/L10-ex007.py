# G. count_code #
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(s):
  contador = 0
  for x in range(len(s)-1):
    if s[x] == 'c' and x <= len(s)-4:
      if s[x+1] == 'o':
        if s[x+3] == 'e':
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
  print ('Count_code')
  test(count_code('aaacodebbb'), 1)
  test(count_code('codexxcode'), 2)
  test(count_code('cozexxcope'), 2)
  test(count_code('cozfxxcope'), 1)
  test(count_code('xxcozeyycop'), 1)
  test(count_code('cozcop'), 0)
  test(count_code('abcxyz'), 0)
  test(count_code('code'), 1)
  test(count_code('ode'), 0)
  test(count_code('c'), 0)
  test(count_code(''), 0)
  test(count_code('AAcodeBBcoleCCccoreDD'), 3)
  test(count_code('AAcodeBBcoleCCccorfDD'), 2)
  test(count_code('coAcodeBcoleccoreDD'), 3)

if __name__ == '__main__':
  main()