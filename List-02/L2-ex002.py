#Exercise 02 - List 02
#Determine se um ano é bissexto.
print('Descobrindo se o ano é bissexto')
# usando biblioteca
import calendar
ano = int(input('Digite o ano: '))

if calendar.isleap(ano):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto :(')

# usando cadeia de condições
ano = int(input('Digite o ano: '))
	
if ano % 4 == 0 or ano % 400 == 0:
    if ano % 100 == 0:
        print('O ano não é bissexto :(')
    else:
        print('O ano é bissexto!')
else:
    print('O ano não é bissexto :(')