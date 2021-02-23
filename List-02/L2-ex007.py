#Exercise 07 - List 02
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
print('Cálculo de latas de tinta')
#entrada de dados
m3 = float(input('Área a ser pintada (em m3): '))

#descobrindo a quantia de latas necessárias
if m3 <= 54:
     #só precisa de uma e vai sobrar
    print(f'Será preciso 1 lata, totalizando R$80.00')
elif m3/54 == 0:
    #total de latas redondo
    print(f'Será preciso {(m3/54)} lata(s), totalizando R${((m3//54)*80):.2f}')
else:
    #caso sobre alguns metros
    print(f'Será preciso {(m3//54) + 1} lata(s), totalizando R${(((m3//54)+1)*80):.2f}')


# FORMA DO PROFESSOR
# entrada de dados
m = int(input('Metros: '))
# cálculo da quantidade de latas
latas = m // 54 if m % 54 == 0 else m // 54 + 1
print(f'Compre {latas} lata(s) pelo valor de RS{latas*80:.2f}')