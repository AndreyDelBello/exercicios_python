metros = float(input("Uma distancia em metros: "))

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000

print('A medida de {}m corresponde a:'.format(metros))
print(f'{km}km') #Quilometros
print(f'{hm}hm') #hectometros
print(f'{dam}dam') #decametros
print(f'{int(dm)}dm') #decimetros
print(f'{int(cm)}cm') #centimetros
print(f'{int(mm)}mm') #milimetros

