import random


def guess(x):
    guess = 0
    numToFind = random.randint(1, x)

    while guess != numToFind:
        guess = int(input('Escolha um número: '))
        if guess > numToFind:
            print('Nossa mas aí ce chutou alto d+')
        elif guess < numToFind:
            print('Nossa mas aí ce chutou baixo d+')
        else:
            print(f'Boaaaa, o numero era {numToFind}')


guess(10)
