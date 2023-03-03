velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de velocidade')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')