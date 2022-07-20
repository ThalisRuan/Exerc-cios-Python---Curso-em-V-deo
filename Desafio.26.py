import random

num = int(input("Digite um numero entre 0 e 5  "))
num1 = random.randint(0,5)
print(num1)
if num1 == num:
    print("Voce acertou, parabens")
    quit()
else:
    print("Voce errou, tente novamente")
