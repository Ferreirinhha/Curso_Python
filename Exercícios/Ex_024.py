#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Qual o nome da sua cidade? ')

print(f'Sua cidade começa com Santos? {cidade[:5].upper() == 'SANTO'}')