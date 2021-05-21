# E. palindrome
# Verifique se uma string é palíndrome
#   palindrome('asa') True
#   palindrome('casa') False 
def palindrome(s):
  if s == s[::-1]:
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
  print ('palindrome')
  test(palindrome('asa'), True)
  test(palindrome('casa'), False)
  
if __name__ == '__main__':
  main()