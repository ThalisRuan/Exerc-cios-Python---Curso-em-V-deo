import random

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)

print(''' ESCOLHA UM NUMERO 

[0] PEDRA

[1] PAPEL

[2] TESOURA

''')

jogador = int(input("Qual e a sua jogada "))
print("-=" * 10)
print("O COMPUTADOR jogou {} " .format(itens[computador]))
print("O JOGADOR jogou {} " .format(itens[jogador]))
print("-=" * 10)

if computador == 0:
    if jogador == 0:
    elif jogador == 





