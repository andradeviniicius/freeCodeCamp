import random


def guess(x):
    userInput = int(input(f'Escolha um valor entre 0 e {x}: '))
    while (userInput > x):
        userInput = int(input(f'Escolha um valor entre 0 e {x}: '))

    computerInput = 0

    low = 0
    high = x
    while (userInput != computerInput):
        computerInput = random.randint(low, high)
        print(f'o computador escolheu: {computerInput}')

        if (userInput > computerInput):
            print('O valor que ele escolheu é mt baixo')
            low = computerInput
        elif (userInput < computerInput):
            print('O valor que ele escolheu é mt alto')
            high = computerInput

    print(
        f'Finalemnte ele acertou, voce escolheu {userInput} e ele escolheu {computerInput}')


guess(1000)
