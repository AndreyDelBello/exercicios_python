frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.count('A')
posicao = frase.find('A')
right_pos = frase.rfind('A')

print(f'A letra A aparece {frase} vezes na frase.')
print(f'A primeira letra A apareceu na posição {posicao+1}')
print(f'A ultima letra A apareceu na posição {right_pos}')



