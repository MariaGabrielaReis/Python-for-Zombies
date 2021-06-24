# Maria Gabriela Garcia dos Santos Reis

from random import choice
import requests

# Criando o desenho da forca
forca = ['''
  +------+
         |
         |
         |
         |
         |
==========''', '''
  +------+
  |      |
         |
         |
         |
         |
==========''', '''
  +------+
  |      |
  O      |
         |
         |
         |
==========''', '''
  +------+
  |      |
  O      |
  |      |
         |
         |
==========''', '''
  +------+
  |      |
  O      |
 /|      |
         |
         |
==========''', '''
  +------+
  |      |
  O      |
 /|\     |
         |
         |
==========''', '''
  +------+
  |      |
  O      |
 /|\     |
 /       |
         |
==========''', '''
  +------+
  |      |
  O      |
 /|\     |
 / \     |
         |
==========''']

# capturando palavras para sortear na forca
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text.lower().split()
# len(palavras)


def escolhe():
    # fazendo com que a escolha da palavra seja aleatória 
    return choice(palavras)


def desenha():
    global certas
    global palavra_sorteada
    global erradas

    # imprimindo a posição da forca referente a quantia de erros
    print(forca[len(erradas)])

    # para letras já descobertas, tira o '_' e coloca a letra no lugar
    for letra in palavra_sorteada:
        if letra in certas:
            print(letra, end=" ")
        else:
            print("_", end=" ")


def chute(usadas):
    while True:
        
        if len(usadas) < 1:
            print("Para começar o jogo...")
        else:
            ja_era = ''
            for usada in usadas:
                ja_era = ja_era + usada + " " 
            print('\nLetras que já foram: ' + ja_era)

        
        letra_da_vez = input("\nChute uma letra: ")
        
        if letra_da_vez.isalpha():
            # se tiver mais de uma letra, não vale
            if len(letra_da_vez) > 1:
                print("Digite apenas uma letra de cada vez \n")
                continue
                        
            else:
                # se a letra já foi usada, não vale
                if letra_da_vez in usadas:
                    print("A letra digitada já foi tentada, escolha uma nova! \n")
                    continue
                else:
                    break
        else:
            # se não for letra
            print("Caractere inválido! Digite apenas uma LETRA \n")
            continue

    return letra_da_vez


def ganhou(palavra_sorteada, certas):
    # se o conjunto de letras da palavra sorteada for igual ao conjunto de 
    # letras das letras escolhidas, o usuário ganhou o jogo
    if set(palavra_sorteada) == set(certas):
        return True
    else:
        return False


def jogar_novamente():
    resposta = input("Jogar de novo?")
    if resposta.lower().strip() == 'sim':
       return True
    else:
        return False

# escolhendo a palavra
palavra_sorteada = escolhe()

# criando variáveis para letras certas e erradas
certas = ''
erradas = ''

while True:
    letra_da_vez = chute(certas + erradas)

    if letra_da_vez in palavra_sorteada:
        certas = certas + letra_da_vez
        desenha()

        if ganhou(palavra_sorteada, certas):
            print("\nParabéns, você ganhou o jogo!")
                
            if jogar_novamente():
                # escolhendo próxima palavra
                palavra_sorteada = escolhe()

                # apagando letras da última rodada
                certas = ''
                erradas = ''

                continue
            else: 
                print(f"Obrigada por jogar! Foi uma partida legal, né?")
                break
    else: 
        if len(erradas) >= len(forca)-2:
            # se acabaram as tentativas...
            print(forca[-1])
            print(f"Fim de jogo! Que pena, você perdeu! \nA palavra era {palavra_sorteada}")

            if jogar_novamente():
                # escolhendo próxima palavra
                palavra_sorteada = escolhe()

                # apagando letras da última rodada
                certas = ''
                erradas = ''

                continue
            else: 
                    print(f"Obrigada por jogar! Foi uma partida legal, né?")
                    break
        
        else:
            erradas = erradas + letra_da_vez
            desenha()

