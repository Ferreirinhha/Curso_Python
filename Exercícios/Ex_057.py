'''
Faça um programa qe leia o sexo de uma pessoa, mas só aceite M ou F.
Caso esteja errado, peça a digitação novamente, até o valor correto.
'''
print('')
print('\033[1;33m=-\033[m' * 30)
n1 = str(input('Digite seu nome: '))
sexo = str(input('Sexo [F] ou [M]: ')).upper().strip()

while sexo != 'F' and sexo != 'M':
    print('\033[1;31mERRO!!!\033[m')
    sexo = str(input('Digite [F] para Feminino ou [M] para Masculino: '))
print('Fim.')
print('\033[1;33m=-\033[m' * 30)
print('')

