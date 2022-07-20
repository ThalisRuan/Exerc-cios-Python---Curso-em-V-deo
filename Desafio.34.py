salario = float(input("Digite o valor do seu salario para calcular o seu aumento "))
valor1 = salario * 10/100 + salario
valor2 = salario * 15/100 + salario
if salario >= 1250:
    print("O valor do seu salario com aumento sera R$ {} ".format(valor1))
else:
    print(" O valor do seu salario com aumento sera R$ {} ".format(valor2)) 