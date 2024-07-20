"""
Refaça o exercicio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:

Equilátero, Isóceles ou Escaleno.
"""
#Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem formar um triângulo.

print('')
print('\033[1;33m-=\033[m' * 25)

lado1 = float(input('Digite o tamanho de uma reta: '))
lado2 = float(input('Digite outro: '))
lado3 = float(input('Digite outro: '))

print('')

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    print('As três retas podem formar um triangulo')
    if lado1 == lado2 == lado3:
        print('Tiangulo \033[1;4;35mEquilátero\033[m, 3 lados iguais')
    elif lado1 != lado2 != lado3 != lado1:
        print('Triangulo \033[1;4;35mEscaleno\033[m, todos os lados diferentes')
    else:
        print('Triangulo \033[1;4;35mIsoceles\033[m, dois lados iguais')  
print('\033[1;33m-=\033[m' * 25)
print('')       