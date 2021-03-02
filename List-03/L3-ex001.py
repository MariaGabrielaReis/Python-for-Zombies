''' 1.Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido. '''

print('Recebendo uma nota válida')

# entrada de dados
score = int(input("Digite uma nota entre 0 e 10: "))

# verificando se a restrição foi obedecida, caso não, introdução de novos dados
while score>10 or score<0:
  score = int(input("Valor inválido, por favor insira uma nota entre 0 e 10:"))

print("Valor válido! A nota é ", score)