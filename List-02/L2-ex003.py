#Exercise 03 - List 02
#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do Estado de São Paulo (50 quilos), deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
print('Cálculo de multa de excesso de peso de peixes')
peso = float(input('Peso: '))

# JEITO 1: PARCELA INTEIRA PARA CADA KG
# verificando se há excesso
if peso > 50.0:
    excesso = peso - 50
    # verificando se o excesso é quebrado ou redondo
    if excesso // 1 == excesso:
        multa = float(excesso * 4)
        print(f'O excesso de peso foi de {excesso:.1f}kg, logo, a multa aplicada será de {multa:.2f} reais')
    else:
    #se o excesso é quebrado, acrescenta uma parcela inteira
        multa = float((excesso // 1) * 4) + 4
        print(f'O excesso de peso foi de {excesso:.1f}kg, logo, a multa aplicada será de {multa:.2f} reais')
# sem excesso
else:
    excesso = 0
    multa = 0
    print('Peso dentro da norma! \n Excesso:', excesso, '\n Multa: ', multa)

  
# JEITO 2: PARCELA PARCIAL PARA CADA GRAMA
if peso > 50.0:
    excesso = (peso - 50) 
    gramasExcesso = excesso * 1000 #transforma os kg excedentes em gramas
    multa = (gramasExcesso * 0.4)/100
   
    print(f'O excesso de peso foi de {excesso:.1f}kg, logo, a multa aplicada será de R${multa:.2f}')  
# sem excesso
else:
    excesso = 0
    multa = 0
    print('Peso dentro da norma! \n Excesso:', excesso, '\n Multa: ', multa)