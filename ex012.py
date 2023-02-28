produto = float(input('Preço do produto: '))
v_desconto = int(input('Desconto do produto: '))

desconto = produto * v_desconto / 100
v_descontado = produto - desconto

print(f'O produto que custava R${produto:.2f}, \n'
      f'na promoção com desconto de {v_desconto}%, \n'
      f'vai custar R${v_descontado:.2f}')