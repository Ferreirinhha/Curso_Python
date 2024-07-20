import math

# control + spaço depois do inport faz ele mostrar sugestoes  
 
n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1) # para dizer a raiz quadrada do número

print(f'A raiz de {n1} = {raiz}')
print(f'A raiz de {n1} = {math.ceil(raiz)}') # para arredondar o número para cima
print(f'A raiz de {n1} = {math.floor(raiz)}') # para arredondar o número para baixo
