import math
a = float(input('Digite o angulo que você deseja: '))

rad = math.radians(a)
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)

print(f'O Ângulo de {a} tem o SENO de {sen:.2f}')
print(f'O Ângulo de {a} tem o COSSENO de {cos:.2f}')
print(f'O Ângulo de {a} tem o TANGENTE de {tg:.2f}')