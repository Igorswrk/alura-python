print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 25

chute_str = input("Digite o seu numero: ")

print("Voce digitou", chute_str)

numero_digitado = int(chute_str)

acertou = numero_digitado == numero_secreto
maior = numero_digitado > numero_secreto
menor = numero_digitado < numero_secreto

if(acertou):
    print("Voce acertou!")
elif(maior):
    print("Voce errou! O seu chute foi maior do que o numero secreto.")
else:
    print("Voce errou! O seu chute foi menor do que o numero secreto.")

print("Fim do jogo")


