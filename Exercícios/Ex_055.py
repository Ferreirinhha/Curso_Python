#Crie um programa que leia o peso de 5 pessoas e diga qual foi o maior peso e o menor peso dentre eles.

peso_maior = 0
peso_menor = 0

print('')
print('\033[1;33m-=\033[m' * 30)
for c in range(1, 5):
    peso = float(input(f'Digite {c}° o seu peso: '))

    if c == 1:
        peso_maior = peso #Aqui damos um valor inicial para o peso maior ja que é o primeiro peso
        peso_menor = peso
    else:
        if peso > peso_maior: # com o peso inicial ja dado ele n mudara mais, a n ser que o proximo peso seja maior
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print(f'O maior peso é o {peso_maior} , o menor peso é o {peso_menor} ')
print('\033[1;33m-=\033[m' * 30)
print('')