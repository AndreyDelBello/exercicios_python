nome = str(input('Digite seu nome completo: ')).strip()
c_espacos = nome.count(' ')
first_name = nome.find(' ')
separa = nome.split()
print('Analisando seu nome...')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - c_espacos} letras')
print(f'Seu primeiro nome é {separa[0]} e ele tem {first_name} letras')

### A fazer =================================================================