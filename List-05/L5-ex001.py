''' Questão A.
O que o seguinte programa (dado na forma de pseucódigo) imprime? 
    x = 2
    y = 5
    se y > 8 então
        y = y * 2
    caso contrário,
        x = x * 2
    imprime (x + y)
Resposta: 9
'''

# declaração de variáveis
x = 2
y = 5

# aplicando a condição
if y > 8:
    y = y * 2
else:
    x = x * 2

print(x + y) # 9
