#Faça uma taboada igual o desafio 9 mas usando o for.

print('')
print('\033[1;33m-=\033[m' * 25)
n1 = int(input('Você quer taboada de qual número: '))

print('')
for c in range(0, 11):
    print(f'{n1} * {c} = {n1 * c}')
print('\033[1;33m-=\033[m' * 25)
print('')