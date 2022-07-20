
nota1 = float(input("Digite a nota do aluno "))
nota2 = float(input("Digite a nota do aluno "))
media = (nota1 + nota2) / 2 
print("Tirando {:.1f} e {:.1f}, a sua nota final sera {:.1f} ".format(nota1, nota2, media))

if 7 > media >= 5:
    print("Voce esta em RECUPERACAO")
elif media < 5:
    print("Voce esta REPROVADO")
else:
    print("O aluno esta APROVADO")

