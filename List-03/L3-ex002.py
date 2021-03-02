'''2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.''' 

print('Problema do usuário e senha')

# entrada de dados
user = input("Usuário: ")
password = input("Senha: ")

# verificando se os valores são iguais, caso sim, introdução de novos dados
while user == password:
    print("ERRO: Usuário e senha com mesmo valor! Por favor, altere uma das informações")
    user = input("Usuário: ")
    password = input("Senha: ")

print("Usuário e senha diferentes, tudo ok!")