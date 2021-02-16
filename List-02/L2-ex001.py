#Exercise 01 - List 02
#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
print('É um triangulo?')

#entrada de dados
l1 = int(input('Medida do lado 1: '))
l2 = int(input('Medida do lado 2: '))
l3 = int(input('Medida do lado 3: '))

#verificação da formação de triângulo
	
#se algum lado for igual a 0
if l1==0 or l2==0 or l3==0:
    print('OS valores não formam um triângulo')
    	
#se o lado 1 for o maior
elif l1>l2 and l1>l3:
    x = l2 + l3
	if x >= l1:
        #verificação do tipo do triângulo
        if l1==l2 or l2==l3 or l1==l3:
            print('É um triângulo isósceles')
        else:
            print('É um triângulo escaleno')
    else:
        print('Os valores não formam um triângulo')
       
#se o lado 2 for o maior	
elif l2>l1 and l2>l3:
    x = l1 + l3
    if x >= l2:
        #verificação do tipo do triângulo
        if l1==l2 or l2==l3 or l1==l3:
            print('É um triângulo isósceles')
        else:
            print('É um triângulo escaleno')
    else:
        print('Os valores não formam um triângulo')
        
#se o lado 3 for o maior
elif l3>l1 and l3>l2:
    x = l1 + l2
    if x >= l3:
        #verificação do tipo do triângulo
        if l1==l2 or l2==l3 or l1==l3:
            print('É um triângulo isósceles')
        else:
            print('É um triângulo escaleno')
    else:
        print('Os valores não formam um triângulo')
        
#casos de isósceles com o lado diferente menor
elif l1==l2 and l3<l1:
    x = l1 +l3
    if x>= l1:
        print('É um triângulo isósceles')
     
elif l1==l3 and l2<l1:
    x = l1 +l2
    if x>= l1:
        print('É um triângulo isósceles')
	
elif l2==l3 and l1<l2:
    x = l1 +l2
    if x>= l1:
        print('É um triângulo isósceles')
     	
#se todos os lados forem iguais
else:
    print('É um triângulo equilátero')