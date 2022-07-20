from ast import Continue
import random

numero = int(input("Digite um numero "))
numero1 = random.randrange(0,5)

if numero == numero1:
    print("voce acertou")
    quit()
else:
    print("voce errou, tente novamente")



