print("-="*20)
print('Analisador de Triângulos')
print("-="*20)

c1 = float(input('Digite o primeiro segmento: '))
c2 = float(input('Digite o segundo segmento: '))
c3 = float(input('Digite o terceiro segmento: '))

if (c1 + c2) > c3 and (c1 + c3) > c2 and (c2 + c3) > c1:
    print('Os segmentos acima PODEM formar um TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM formar um TRIÂNGULO!')
