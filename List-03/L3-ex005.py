'''5.Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o 
algoritmo de Euclides''' 

print('Máximo Divisor Comum (MDC) de dois números')

# entrada de dados
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

# variáveis para receber divisões, assim não se perde os valores iniciais
n3, n4 = n1, n2

# calculando o MDC
while n3 % n4 != 0:
    n3, n4 = n4, n3 % n4

print(f'O Máximo Divisor Comum de {n1} e {n2} é {n4}')

