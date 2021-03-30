# F. make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tab, word):
  return f'<{tab}>{word}</{tab}>'

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Make Tags')
  test(make_tags('i', 'Yay'), '<i>Yay</i>')
  test(make_tags('i', 'Hello'), '<i>Hello</i>')
  test(make_tags('cite', 'Yay'), '<cite>Yay</cite>')
  test(make_tags('address', 'here'), '<address>here</address>')
  test(make_tags('body', 'Heart'), '<body>Heart</body>')
  test(make_tags('i', 'i'), '<i>i</i>')
  test(make_tags('i', ''), '<i></i>')

if __name__ == '__main__':
  main()
  