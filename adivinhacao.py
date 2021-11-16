numero_secreto = 50
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas+1):
    print('tentativa {} de {}'.format(rodada, total_de_tentativas))

    chute = int(input('Digite o seu numero: '))
    print('Você digitou: ', chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('*********************************')
        print('      ***Você acertou!***')
        print('*********************************')
        break
    elif (maior):
        print("Você errou, seu chute foi maior")
    elif(menor):
        print("você errou, seu chute foi menor")
