import random

while True:

    jogo = input('Escolha qual jogo você quer jogar, cara ou coroa(1), jogo da forca(2), adivinhe o número(3) ou slot machine(4)! Ou digite sair(5), para sair:').strip().lower()

    if jogo == '5' or jogo == 'sair':
        break

    if jogo == '1' or jogo == 'cara ou coroa':

        possibilidades = ('cara', 'coroa')

        jogar_novamente = True

        while jogar_novamente == True: 
            loop = True

            while loop == True:

                chute=input('Escolha Cara ou Coroa:').strip() .lower()

                if chute not in possibilidades:
                    print('Escolha inválida, tente novamente!')

                else: loop = False

            moeda = random.choice(possibilidades)

            if chute == moeda:
                print('Você Ganhou!')
                print(f'A moeda saiu:{moeda}')

            if chute != moeda:
                print(f'Você perdeu! Era: {moeda}')

            jogar_novamente = input('Deseja jogar novamente? y/n:').strip().lower()

            if jogar_novamente == 'n':
                jogar_novamente = False

            else: jogar_novamente = True

    if jogo == '3' or jogo == 'adivinhe o número':

        número_secreto = random.randint(1,100)

        tentativas = 0

        acertou = False

        while acertou == False:


            chute = int(input('Digite seu chute (1-100): '))

            if chute not in range(1,101):
                print('Escolha um número válido!')
                continue  

            tentativas = tentativas + 1

            if chute == número_secreto:
                print(f'Você acertou em {tentativas} tentativas, parabéns')
                acertou = True

            elif chute > número_secreto:
                print('O número é menor, tente novamente!')

            elif chute < número_secreto:
                print('O número é maior, tente novamente!')


        jogar_novamente = input('Deseja jogar novamente? y/n:').strip().lower()

        if jogar_novamente == 'n':
            jogar_novamente = False

    if jogo == '4' or jogo == 'slot machine':

        possibilidades = ['🍒', '🍉', '🔔', '💎', '7️⃣']

        saldo = 200

        jogar_novamente = True

        while jogar_novamente == True:

            print(f'Seu saldo atual é {saldo}')

            if saldo <= 0:
                print('Você zerou seu saldo! Tente novamente')
                break


            aposta = float(input('Quanto você quer apostar?'))

            if aposta > saldo:
                print('Você não pode apostar mais q seu saldo! Tente novamente')
                continue

            if aposta < 0:
                print('Digite um valor de aposta válido')
                continue


            roleta1 = random.choice(possibilidades)
            roleta2 = random.choice(possibilidades)
            roleta3 = random.choice(possibilidades)

            print('Girando roleta...')
            print(f'Roleta foi: {roleta1}, {roleta2}, {roleta3}')

            if roleta1 == roleta2 == roleta3:
                ganho = aposta * 20
                saldo = saldo + ganho
                print(f'Parabéns, você ganhou! Você tem {saldo}')

            else:
                saldo = saldo - aposta
                print(f'Você perdeu! Seu saldo atual é {saldo}')

            resposta = input('Deseja jogar novamente? y/n:').strip().lower()

            if resposta == 'n':
                jogar_novamente = False

    if jogo == '2' or jogo == 'jogo da forca':

        palavras = ['roblox', 'valorant', 'counterstrike', 'cyberpunk', 'computador', 'teclado', 'monitor', 'headset', 'processador', 'placadevideo']

        jogar_novamente = True


        while jogar_novamente == True:
            
            vidas = 6

            palavra_secreta = random.choice(palavras)

            progresso = ['_'] * len(palavra_secreta)

            while  vidas > 0 and '_' in progresso:
                print(vidas)
                print(progresso)

                chute = input('Escolha uma letra:').lower().strip()

                if len(chute) != 1:
                    print('Digite apenas UMA letra!')
                    continue

                if chute in palavra_secreta:
                    print('Parabéns, você acertou uma letra')

                    for i in range(len(palavra_secreta)):
                        if palavra_secreta[i] == chute:
                            progresso[i] = chute

                if chute not in palavra_secreta:
                    vidas = vidas - 1
                    print(f'Você errou! Você tem agora {vidas} vidas')

            if '_' not in progresso:
                print(f'Parabéns, você ganhou com {vidas} vidas sobrando!')

            else:
                print(f'Você perdeu, o boneco foi enforcado! A palavra era {palavra_secreta}')

            resposta = input('Deseja jogar novamente? y/n').strip().lower()

            if resposta == 'n':
                jogar_novamente = False