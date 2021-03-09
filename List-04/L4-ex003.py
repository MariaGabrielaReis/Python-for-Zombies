''' 3.Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados dos dois outros vetores. Imprima os três vetores. '''

print('Misturando vetores de números aleatórios')

# importando a biblioteca para gerar nºs aleatórios
import random

# gerando números aleatórios
randomNumbers = random.sample(range(100), 10)
randomNumbers2 = random.sample(range(100), 10)
intercalated = []

# intercalando os valores em uma outra variável
for x in range(len(randomNumbers)):
    intercalated.append(randomNumbers[x])
    intercalated.append(randomNumbers2[x])

print("Lista original 1: ", randomNumbers)
print("Lista original 2: ", randomNumbers2)
print("Valores intercalados: ", intercalated)