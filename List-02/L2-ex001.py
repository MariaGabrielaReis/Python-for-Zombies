#Exercise 01 - List 02
#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
print('É um triangulo?')
#entrada de dados
a = int(input('Medida do lado 1: '))
b = int(input('Medida do lado 2: '))
c = int(input('Medida do lado 3: '))

#se os valores não formam um triângulo
if a > b + c or b > a + c or c > a + b:
    print('Os valores não formam um triângulo!')
#se todos os lados forem iguais
elif a == b == c:
    print('O triângulo é um Equilátero!')
#se 2 lados forem iguais
elif a == b or b == c or a == c:
    print('O triângulo é um Isóceles!')
#se todos os lados forem diferentes
else:
    print('O triângulo é um Escaleno!')