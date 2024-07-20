"""
Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre

A media da idades

Nome do mais velho

e quantas mulheres tem menos de 20 anos
"""
mais_velho = 0
nome_mais_velho = ''
cont = 0
media = 0

print('')
print('\033[1;33m-=\033[m' * 30)
pessoas = int(input('Quantas pessoas serão entrevistadas: '))
print('')

for p in range(1, pessoas + 1):
    n1 = str(input(f'Nome da {p}° pessoa: ')).strip()
    idade = int(input(f'Idade da {p}° pessoa: '))
    sexo = str(input(f'Sexo da {p}° pessoa. [F] para Feminino e [M] para masculino: ')).upper().strip()
    print('')

    media += idade / pessoas
    #Verificar idade
    if p == 1:
        nome_mais_velho = n1
        mais_velho = idade
    if idade < 20 and sexo == 'F':
        cont += 1
        
    else:
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = n1
print(f'O mais velho é o: {nome_mais_velho} com {mais_velho} anos')
print(f'Media das idades: {media:.2f}')
print(f'Número de mulheres com menos de 20 anos: {cont}')
print('\033[1;33m-=\033[m' * 30)
print('')