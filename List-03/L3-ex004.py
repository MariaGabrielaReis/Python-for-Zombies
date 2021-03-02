'''4.A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... 
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. 
F1= 1, F2= 1, F3= 2, etc.''' 

print('Posição na sequência de Fibonacci')

# entrada de dados
positionFibonacci = int(input("Digite um número inteiro: "))

# definião do primeiro e segundo número da sequência de Fibonacci
before = 1
after = 1 

# iniciando contador em 2 pois já se tem o 1º e o 2º número da sequência, logo, não é preciso calcular
numberFibonacci = 2

# calculando a sequência até a posição escolhida
while numberFibonacci < positionFibonacci:
    before, after = after, before + after
    numberFibonacci += 1

print(f'A posição {positionFibonacci} da sequência de Fibonacci tem o valor de {after}')
