#Exercise 03 - List 01
#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
print("Cálculo de segundos")
	
d = int(input('Dias: '))	
h = int(input('Horas: ')) + (d*24)	
m = int(input('Minutos: ')) + (h*60)	
s = int(input('Segundos: ')) + (m*60)
	
print('Convertendo tudo dá ', s, 'segundos')