co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (co**2 + ca**2) ** (1/2)
#hipotenusa = math.sqrt(cateto1**2 + cateto2**2) -----> Alternativa importando o modulo 'math'

print(f'A hipotenusa vai medir: {hipotenusa:.2f}')

