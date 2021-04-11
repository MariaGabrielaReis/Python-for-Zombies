# F. cat_dog #
# verifica se o aparece o mesmo número de vezes 'cat' e 'dog'
# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True
def cat_dog(s):
  if len(s) <= 2:
    return True
  else:
    cat = 0
    dog = 0
    for x in range(len(s)-1):
      if s[x] == 'c' and x <= len(s)-3:
        if s[x+1] == 'a':
          if s[x+2] == 't':
            cat += 1
      
      if s[x] == 'd' and x <= len(s)-3:
        if s[x+1] == 'o':
          if s[x+2] == 'g':
            dog += 1
    if cat == dog:
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
  print ('Cat_dog')
  test(cat_dog('catdog'), True)
  test(cat_dog('catcat'), False)
  test(cat_dog('1cat1cadodog'), True)
  test(cat_dog('catxxdogxxxdog'), False)
  test(cat_dog('catxdogxdogxcat'), True)
  test(cat_dog('catxdogxdogxca'), False)
  test(cat_dog('dogdogcat'), False)
  test(cat_dog('dogogcat'), True)
  test(cat_dog('dog'), False)
  test(cat_dog('cat'), False)
  test(cat_dog('ca'), True)
  test(cat_dog('c'), True)
  test(cat_dog(''), True)

if __name__ == '__main__':
  main()