#Exercise 10 - List 01
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
print("Cálculo da redução de vida de fumantes")
	
c = int(input('Quantia de cigarros fumados por dia: '))
a = int(input('Há quantos anos você fuma? '))
	
# multiplica por dias do ano para saber a quantia de dias
# multiplica pela quantidade de cigarros de um dia 	
# multiplica por quantos minutos um cigarro tira da vida
# divide por 60 pra saber quantas horas dá
# divide por 24 pra saber quantos dias dá
d = int(((((365*a)*c)*10)/60)/24) 
	
print(f'Total de dias perdidos: {d} dias')