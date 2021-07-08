print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 5
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):  # range(start, stop, [step])
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # String Interpolation
    chute_str = input("Digite um numero entre 1 e 10: ")
    print("Voce digitou", chute_str)
    numero_digitado = int(chute_str)

    if(numero_digitado < 1 or numero_digitado > 10):
        print("Voce deve digitar um numero entre 1 e 10!")
        continue

    acertou = numero_digitado == numero_secreto
    maior = numero_digitado > numero_secreto
    menor = numero_digitado < numero_secreto

    if(acertou):
        print("Voce acertou!")
        break
    elif(maior):
        print("Voce errou! O seu chute foi maior do que o numero secreto.")
    else:
        print("Voce errou! O seu chute foi menor do que o numero secreto.")

print("Fim do jogo")

"""
>>> print("Tentativa {} de {}".format(1, 3))

>>> print("Tentativa {1} de {0}".format(1, 3))
Tentativa 3 de 1

>>> print("R$ {}".format(1.59))
R$ 1.59

>>> print("R$ {:f}".format(1.59))
R$ 1.590000

>>> print("R$ {:.2f}".format(1.59))
R$ 1.59

>>> print("R$ {:.2f}".format(1.5))
R$ 1.50

>>> print("R$ {:.2f}".format(1.5))
R$ 1.50
>>> print("R$ {:.2f}".format(1234.50))
R$ 1234.50

>>> print("R$ {:7.2f}".format(1234.50))
R$ 1234.50
>>> print("R$ {:7.2f}".format(1.5))
R$    1.50

>>> print("R$ {:07.2f}".format(1.5))
R$ 0001.50

>>> print("R$ {:07d}".format(4))
R$ 0000004

>>> print("Data {:02d}/{:02d}".format(9, 4))
Data 09/04
>>> print("Data {:02d}/{:02d}".format(19, 11))
Data 19/11 

>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome}')
Meu nome é Matheus

>>> nome = 'Matheus'
>>> print(f'Meu nome é {nome.lower()}')
Meu nome é matheus
"""
