#Faça um programa que leia algo pelo teclado 
#e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

algo = input('Digite Algo: ')

print('Tipo primitivo desse valor é: ', type(algo))
print('É alfabético? ', algo.isalpha())
print('É decimal? ',algo.isdecimal())
print('É numérico? ', algo.isnumeric())
print('Só tem espaços? ', algo.isspace())
print('Está em maiusculo? ', algo.isupper())
print('Está em minuscula? ', algo.islower())
print('É alpha Numerico? ', algo.isalnum())
print('Está captalizada? ', algo.istitle()) #Minusculo e maiusculo
