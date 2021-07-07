print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 25

chute_str = input("Digite o seu numero: ")

print("Voce digitou", chute_str)

numero_digitado = int(chute_str)

if numero_secreto == numero_digitado:
    print("Voce acertou!")
else:
    print("Voce errou!")

print("Fim do jogo")


