largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
litro = area/2

print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area:.3f}m².\n'
      f'Para pintar essa parede, você precisará de {litro}l de tinta.')