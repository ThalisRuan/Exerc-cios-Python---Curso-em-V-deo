print('{:=^40}'.format(" LOJAS THALIS RUAN "))
preco = float(input("Digite o preco das compras R$ "))
print(''' FORMAS DE PAGAMENTO
[ 1 ] a vista - dinheiro/cheque
[ 2 ] a vista no carta - debito 
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais no cartao ''')
opcao = int(input("Qual opcao de pagamento? "))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao ==3:
    total = preco /2
    parcela = preco / 2 
    print("Sua parcela sera {}".format(parcela))    
elif opcao == 4 :
    total = preco + (preco * 10 /100) 
    totalparc = int(input("Qual o total de parcelas "))
    parcela = preco / totalparc
    print("Sua parcela sera {}".format(parcela))
print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final".format(preco,total))





