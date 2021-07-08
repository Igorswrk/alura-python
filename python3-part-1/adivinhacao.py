import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))  # 0.0 1.0
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 10: ")
    print("Voce digitou", chute_str)
    numero_digitado = int(chute_str)

    if(numero_digitado < 1 or numero_digitado > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
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
