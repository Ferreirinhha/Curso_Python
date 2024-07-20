"""
Crie um programa onde o usuáro digite uma expressão qualquer que usa parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.
"""
print('')
print('\033[1;33m=-\033[m' * 30)

expressao = str(input('Digite uma expressão numerica: ')).split()
print('')

cont_parentese_abrindo = 0
cont_parentese_fechando = 0

for i in expressao:
    for j in i:
        if j in '(':
            cont_parentese_abrindo += 1
        elif j in ')':
            cont_parentese_fechando += 1
    if i == '()':
        print('\033[1;4;31mExpressão errada.\033[m')
        print('\033[1;4;35mParênteses vazios!!!\033[m')
        break
else:
    if cont_parentese_abrindo == cont_parentese_fechando:
        print('\033[1;4;32mExpressão correta.\033[m')
    else:
        print('\033[1;4;31mExpressão errada.\033[m')
        print('\033[1;4;35mFeche os parênteses!!!\033[m')
print('')
print(f'Parenteses abrindo: {cont_parentese_abrindo}')
print(f'Parentese fechando: {cont_parentese_fechando}')
print('\033[1;33m=-\033m' * 30)
print('')

#Resolução do prof

exp = str(input('Digite sua expressão: '))
paren = list()

for simb in exp: # vai varrer a expressão, toda vez que tiver um parentese irá add na lista
    if simb == '(':
        paren.append('(')
    elif simb == ')': # , toda vez q tiver um parentese oposto, o parente atual na lista será add, simbolizando que um par foi fechado.
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
if len(paren) == 0:
    print('Expressão certa.')
else:
    print('Expressão Errada.')
