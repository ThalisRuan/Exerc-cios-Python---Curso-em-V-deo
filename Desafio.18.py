import math

angulo = float(input("Digite um angulo que voce deseja "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print("O sen de {} e {:.2f}".format(angulo,seno))
print("O cos de {} e {:.2f}".format(angulo,cos))
print("O tan de {} e {:.2f}".format(angulo,tan))   

