'''3.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento 
de 3%, e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.''' 

print('Cálculo de anos para igualdade de populações')

# populações dos dois países
populationCountryA = 80000
populationCountryB = 200000

#contador de anos
years = 0

# verificando se a taxa do país B continua superior
while populationCountryB > populationCountryA:
    # adicionando o crescmento de um ano para os dois países
    populationCountryB += (populationCountryB * 0.015)
    populationCountryA += (populationCountryA * 0.03)

    # adicionando um ano para que as populações se igualem ou o país A se torne maior
    years += 1

# resultado: 63 anos
print(f'Será preciso {years} ano(s) para que a população do país A ultrapasse ou se iguale a população do país B')
print("País A: ", populationCountryA)
print("País B: ", populationCountryB)