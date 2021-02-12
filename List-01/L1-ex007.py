#Exercise 07 - List 01
#Converta uma temperatura digitada em Celsius para Fahrenheit.F = 9*C/5 + 32
print("Conversor: Fahrenheit - Celsius")

f = float(input('Temperatura em Fahrenheit (ºF): '))
c = float(((f -32)*5) / 9)
	
print(f'A temperatura em Celsius correspondente é {c:.1f} ºC')