#Exercise 05 - List 02
#Faça um Programa que leia três números e mostre o maior e o menor deles.
print('O maior e o menor nº dentre 3')
#entrada de dados
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

#descobrindo se o maior é o primeiro
if n1>n2 and n1>n3:
    #descobrindo o menor dos que sobraram
    if n2<n3:
        print('O primeiro número, ', n1, ', é o maior. Já o menor é o segundo número, ', n2)
    else:
        print('O primeiro número, ', n1, ', é o maior. Já o menor é o terceiro número, ', n3)
        
#descobrindo se o maior é o segundo
if n2>n1 and n2>n3:
   #descobrindo o menor dos que sobraram
    if n1<n3:
        print('O segundo número, ', n2, ', é o maior. Já o menor é o primeiro número, ', n1)
    else:
        print('O segundo número, ', n2, ', é o maior. Já o menor é o terceiro número, ', n3)
    
#descobrindo se o maior é o terceiro
if n3>n1 and n3>n2:
    #descobrindo o menor dos que sobraram
    if n1<n2:
        print('O terceiro número, ', n3, ', é o maior. Já o menor é o primeiro número, ', n1)
    else:
        print('O terceiro número, ', n3, ', é o maior. Já o menor é o segundo número, ', n2)