import random


num1 = int(input("Choose a number: "))
numToFind = random.randint(1, 2)

if numToFind == num1:
    print('Voce acertou')
else:
    print('Voce errou')


print(numToFind)
print(num1)
