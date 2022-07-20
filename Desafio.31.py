km = float(input("Digite o numero de KM da sua viagem  "))
valor = km * 0.5
valor2 = km * 0.45 
if km > 200.00:
    print("O valor a ser pago sera de {}  ".format(valor))
elif km < 200:
    print(" O valor a ser pago sera R$ {}  ".format(valor2))
