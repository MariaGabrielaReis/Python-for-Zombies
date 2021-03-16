''' Questão D.
Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7.
Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
'''

# variável para contar os números sortudos
has2AndDoesNotHave7 = 0

# aplicação das repetições
for i in range(18644, 33088):
    if '2' in str(i) and not '7' in str(i):
            has2AndDoesNotHave7 += 1 # 7995 nºs satisfazem as condições

print(f'Para Daniela, entre 18644 e 33087 existem {has2AndDoesNotHave7} números sortudos')
