''' 
“The Python Software Foundation and the global Python community welcome and encourage participation 
by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working
to help each other live up to these principles. We want our community to be more diverse: whoever you 
are, and whatever your background, we welcome you.”

5.Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e 
que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de 
remover antes os caracteres especiais. '''


# variável com o texto
text = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

# tirando pontuação, deixando em minúsculas e separando as palavras
text = text.replace('.', ' ')
text = text.replace(',', ' ')
text = text.replace(':', ' ')
text = text.lower()
text = text.split()

# criando variável para as palavras que satisfazem as condições
wordsPython = []

def have_python(word): 
    for letter in word:
        if letter in 'python': 
            return True 
    return False

for word in text: 
    if have_python(word):
        if len(word) > 4:
            wordsPython.append(word)

print(wordsPython)