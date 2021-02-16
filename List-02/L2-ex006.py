#Exercise 06 - List 02
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# |a. + Salário Bruto : R$
# |b. - IR (11%) : R$
# |c. - INSS (8%) : R$
# |d. - Sindicato ( 5%) : R$
# |e. = Salário Liquido : R$

print('Tabela de taxas sobre o salário')
#entrada de dados
valor = float(input('Quanto você ganha por hora?'))
horas = int(input('Quantia de horas trabalhadas no mês: '))

#calculando salário bruto
salarioBruto = valor * horas

#calculando descontos
impostoRenda = salarioBruto  * 0.11
inss = salarioBruto  * 0.08
sindicato = salarioBruto  * 0.05
salarioLiquido = float(salarioBruto - (inss + sindicato + impostoRenda))

#mostrando em forma de tabela
print(f'|+ Salário Bruto: R${salarioBruto:.2f} \n |- IR(11%): R${impostoRenda:.2f} \n |- INSS(8%): R${inss:.2f} \n |- Sindicato(5%): R${sindicato:.2f} \n|= Salário Liquido: R${salarioLiquido:.2f}')
