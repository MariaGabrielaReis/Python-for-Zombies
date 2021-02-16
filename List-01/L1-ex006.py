#Exercise 06 - List 01
#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
print("Cálculo de tempo de uma viagem")

d = float(input('Distância a ser percorrida (km): '))
v = int(input('Velocidade média esperada (km/h): '))
h = d/v

if h//1 == h:
	m = 0
else: 
	m = ((d/v) - (d//v))*60

print(f'O tempo esperado da viagem será de {h:.0f} hora(s) e {m:.0f} minuto(s)')