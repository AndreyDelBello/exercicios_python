reais = float(input('Quanto dinheiro você tem na carteira: R$'))

dollar = reais / 5.21
euro = reais / 5.50

print(f'Com R${reais:.2f} você pode comprar {dollar:.2f}US$ e {euro:.2f}€')