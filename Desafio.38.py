num1 = int(input("Digite um numero"))
num2 = int(input("Digite um numero"))

if num1 > num2 :
    print("O valor {} e maior que o valor {} ".format(num1,num2))
elif num2 < num1:
    print("O valor de {} e maior que o valor de {} ".format(num2,num1))
else :
    print("Nao existem valor maior, os dois numeros sao iguais ")
    
