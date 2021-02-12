#Exercise 05 - List 01
#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e opreço a pagar.
print("Cálculo de desconto")

p = float(input('Preço da mercadoria: '))
d = int(input('Porcentual do desconto (%): ')) /100
	
print(f'O desconto foi de RS{(p*d):.2f}, resultando RS{(p - (p*d)):.2f}')