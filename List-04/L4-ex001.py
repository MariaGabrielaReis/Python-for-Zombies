''' 1.Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, 
sem usar as funções max e min. '''

print('Maior e menor de números sorteados')
# importando a biblioteca para gerar nºs aleatórios
import random

# gerando números aleatórios
randomNumbers = random.sample(range(100), 10)

# variáveis para armazenar o menor e o maior nº
bigger = smaller = randomNumbers[0]

# verificando qual nº é o maior e qual o menor
for x in randomNumbers:
    if x < smaller:
        smaller = x
    
    if x > bigger:
        bigger = x

print(f' Maior: {bigger} \n Menor: {smaller}')
