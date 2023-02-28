diaria = int(input('Quantos dias ele foi alugado? '))
km = float(input('Quantos kms o carro percorreu? '))

aluguel_diaria = diaria*60
km_rodado = km*0.15
uso_geral = aluguel_diaria + km_rodado

print(f'O total a pagar é de R${uso_geral:.2f}')