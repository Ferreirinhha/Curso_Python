"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, e calcule seu IMC
e mostre seu status, de acordo com a tabela a abaixo.

Abaixo de 18.5: Abaixo do peso

Entre 18.5 e 25: Peso ideal

25 até 30: Sobrepeso

30 até 40: Obesidade

Acima de 40: Obesidade Mórbida
"""
print('')
print('\033[1;33m-=\033[m' * 25)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

print('')

if imc < 18.5:
    print('\033[1;4;34mVocê está A BAIXO DO PESO!\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[1;4;32mSeu peso está IDEAL!\033[m')
elif imc > 25 and imc <= 30:
    print('\033[1;4;34mVocê está ACIMA DO PESO!\033[m')
elif imc > 30 and imc <= 40:
    print('\033[1;4;31mVocê está OBESO, cuidado!!!\033[m')
else:
    print('\033[1;4;31mVocê está com OBESIDADE MÓRBIDA, vá se cuidar URGENTE!!!\033[m')
print('\033[1;33m-=\033[m' * 25)
print('')