salario = float(input('Qual o salario do funcionario? '))
aumento = int(input('porcentagem de aumento: '))

novo = salario + (salario * aumento / 100)

print(f'Um funcionario que ganhava R${salario}, com {aumento}% de aumento, passa a raceber R${novo:.2f}')
