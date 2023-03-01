cidade = str(input('Digite a cidade natal: ')).strip()
cidade = cidade.lower()
cidade = cidade.split()

if cidade[0] == 'santo':
    print(True)
else:
    print(False)
#===== FAZENDO ========================== #