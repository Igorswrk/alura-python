import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))  # 0.0 1.0
total_de_tentativas = 3
pontos = 100

print("Qual nivel de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Defina o nivel: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou", chute_str)
    numero_digitado = int(chute_str)

    if(numero_digitado < 1 or numero_digitado > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue

    acertou = numero_digitado == numero_secreto
    maior = numero_digitado > numero_secreto
    menor = numero_digitado < numero_secreto

    if(acertou):
        print("Voce acertou e fez {} pontos!".format(pontos))
        break
    elif(maior):
        print("O seu chute foi maior que o número secreto")
        if (rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
    else:
        print("O seu chute foi menor que o número secreto")
        if (rodada == total_de_tentativas):
            print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
    pontos_perdidos = abs(numero_secreto - numero_digitado)
    pontos = pontos - pontos_perdidos

print("Fim do jogo")
