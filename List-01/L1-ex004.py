#Exercise 04 - List 01
#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
print("Cálculo de aumento de salário")

s = float(input('Salário: '))	
a = int(input('Porcentagem do aumento (%): ')) /100
	
print(f'O aumento de RS{(s*a):.2f} foi acrescentado, resultando RS{((s*a) +s):.2f}')