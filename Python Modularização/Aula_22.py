# Modulos e Pacotes

# Modularização (construir modulos)
# Todo arquivo .py pode ser usado como modulos, contanto que tenha funções nele

from Uteis import fatorial

num = int(input('Digite um numero: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

# Pacotes: pasta que contem modulos que da para separar por assuntos

# Crair pacotes: Criar a pasta uteis e para cada assunto, criar uma pastas
# 
# Ex: cores
# Ex: datas
# Dentro de cada pasta tem que ter um arquivo chamado __init__.py 