numero_secreto = 14
cont = 0

while True:
    senha = int(input('Digite o numero secreto:'))
    print('')
    if senha == numero_secreto:
        print('Parabens')
    else:
        if cont == 0:
            print('está errado: tente denovo')
            print('')
            cont += 1
        elif cont == 1:
            print('Errou DENOVO? DAREI MAIS UMA CHANCE')
            print('')
            cont += 1
        elif cont == 2:
            print('NÃO É POSSIVEL, BURRO! VAI LOGO')
            print('')
            cont += 1
        else:
            print('FODASE, TCHAU!!!')
            print('')
            break
            
print('Fim.')