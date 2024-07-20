"""
Crie um programa onde uma pessoa possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separado os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.
"""
# numeros = [[2,4,6,8,10], [1,3,5,7,9]]
numbers = [[], []]

for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}° valor: '))
    if valor % 2 == 0:
        numbers[0].append(valor)
    else:
        numbers[1].append(valor)
numbers[0].sort()
numbers[1].sort()
print(f'Lista de pares: {numbers[0]}')
print(f'Lista de ímpares: {numbers[1]}')
print(numbers)
