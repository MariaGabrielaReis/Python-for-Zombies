''' 2.Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os 
números ímpares na lista IMPAR. Imprima as três listas. '''

print('Ímpares e pares de números sorteados')

# importando a biblioteca para gerar nºs aleatórios
import random

# gerando números aleatórios
randomNumbers = random.sample(range(100), 20)

# listas para armazenar os nºs pares e ímpares
even = [] 
odd = []

for x in randomNumbers:
    even.append(x) if x % 2 == 0 else odd.append(x)

print("Lista original: ", randomNumbers)
print("Pares: ", even)
print("Ímpares:", odd)