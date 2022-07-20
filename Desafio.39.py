from time import sleep

idade = int(input("Digite a sua idade para analisarmos "))
print("Analisando...")
sleep(4)
if idade > 18:
    print("Ja passou do prazo de voce se alistar, o praso para voce se alistar esta {} anos atrasado ".format(idade-18))
elif idade < 18:
    print("Voce esta proximo de se alistar, faltam {} para o seu alistamento ".format(18-idade))
elif idade == 18:
    print("Voce esta na idade de se alistar ")
    quit()
    

    
