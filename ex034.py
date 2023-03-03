salario = float(input('Qual o salário de um funcionario: '))

if salario > 1250.00:
    aumento = salario * (10 / 100)
    novo = salario + aumento
else:
    aumento = salario * (15 / 100)
    novo = salario + aumento

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.')
    