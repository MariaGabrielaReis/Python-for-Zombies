''' Questão C.
Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7?
Resposta: 183
'''

# variável para contar os números pares e divisíveis por 7
evenAndDivisibleForSeven = 0

# aplicação das repetições
for i in range(1067,3628):
    if i % 2 == 0:
        if i % 7 == 0:
            evenAndDivisibleForSeven += 1 # 183 nºs satisfazem as condições
print(f'Entre 1067 e 3627, {evenAndDivisibleForSeven} números são pares e também divisíveis por 7.')
