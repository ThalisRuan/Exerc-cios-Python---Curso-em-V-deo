
dias = int(input("Quantos dias o carro foi alugado? "))
preco1 = dias * 60 
km = float(input("Quantos km foram rodados? "))
km1 = km * 0.15
total = km1 + preco1

print("O total a ser pego sera R$ {}".format(total))
