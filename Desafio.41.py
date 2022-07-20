idade = int(input("Digite a idade do atleta "))
if idade >= 0 and idade <=9:
    print("MIRIM")
elif idade >= 9 and idade <=14:
    print("INFANTIL")
elif idade >=14 and idade <=19:
    print("JUNIOR")
elif idade >=14 and idade <=20:
    print("SENIOR")
else:
    print("MASTER")