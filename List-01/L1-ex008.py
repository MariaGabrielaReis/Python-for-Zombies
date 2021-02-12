#Exercise 08 - List 01
#Faça agora o contrário, de Fahrenheit para Celsius.
print("Conversor: Celsius - Fahrenheit")
	
c = float(input('Temperatura em Celsius (ºC): '))	
f = float(((c*9)/5) + 32) 
	
print(f'A temperatura em Fahrenheit correspondente é {f:.1f} ºF')