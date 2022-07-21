peso = float(input("Qual o seu peso "))
altura = float(input("Qual a sua altura "))
imc = peso/altura**2
print("O IMC DESSE PACIENTE E DE {:.2f} ".format(imc))
if imc <= 18.5:
    print("Voce esta ABAIXO DO PESO")
elif imc >= 18.5 and imc <=25:
    print("Voce esta no PESO IDEAL")
elif imc >= 25 and imc <= 30:
    print("voce esta em SOBREPESO")
elif imc >= 30 and imc <= 40:
    print("voce esta EM OBESIDADEEEEE")
else:
    print("Voce esta em OBESIDADE MORBIDA")