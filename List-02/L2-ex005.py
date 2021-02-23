#Exercise 05 - List 02
#Faça um Programa que leia três números e mostre o maior e o menor deles.
print('O maior e o menor nº dentre 3')
#entrada de dados
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

# JEITO DO PROFESSOR
# se o a for o maior
if a>=b and a>=c: print('Maior: ', a)
# se o b for o maior
elif b>=a and b>=c: print('Maior: ', b)
# se o c for o maior
else: print('Maior: ', c)
# se o a for o menor
if a<=b and a<=c: print('Menor: ', a)
# se o b for o menor
elif b<=a and b<=c: print('Menor: ', b)
# se o c for o menor
else: print('Menor: ', c)