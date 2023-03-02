from random import randint
from time import sleep

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
maquina = randint(0, 5)

if num == maquina:
    print('Você acertou, Parabens!!!')
else:
    print('HAHAHA, treine mais, perdeu como sempre!')


