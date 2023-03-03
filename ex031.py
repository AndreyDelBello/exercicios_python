distancia = float(input('Digite a distancia de uma viagem em Km: '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')

if distancia > 200:
    preco = distancia * 0.45
    print(f'O preço da sua passagem será de R${preco:.2f}')
else:
    preco  = distancia * 0.50
    print(f'O preço da sua passagem será de R${preco:.2f}')