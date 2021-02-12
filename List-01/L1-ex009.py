#Exercise 09 - List 01
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
print("Cálculo de aluguel de carro")
	
k = float(input('Quilêmetros percorridos (km): '))	
d = float(input('Quantidades de dias alugados: '))	
p = float((d*60) + ((k*15)/100)) 
	
print(f'O preço a pagar será de R${p:.2f}')